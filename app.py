from fastapi import FastAPI,Request,Response,Form,Depends,HTTPException,UploadFile,File
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from pydantic import EmailStr
from database.user import create_user,get_user
from database.candidate import create_candidate,get_candidate
from database.company import create_company
from database.candidate_job import get_candidate_job,get_placed_candidates_by_job,create_candidate_job,update_candidate_job,update_candidate_video_path,execte_query
from database.job import create_job,get_all_jobs,get_jobs_by_id,update_job,get_jobs_by_company
from models.candidate import CandidateModel
from models.company import CompanyModel
from models.jobs import jobModel 
from middlewares.schema_validator import validate_candidate,validate_company,validate_job
from middlewares.util import checkApplied
from middlewares.auth import check_in_DB
from auth.password_hash import hash_password
import uuid
from auth.authenticate import create_access_token,verify_token
from jose import  JWTError
import json
import shutil
from langchain_community.document_loaders import PyPDFLoader
from ats.ats import find_ats
from interview.gen_question_answer import generate_question_answer
from interview.predict_confidence import FindSoftSkill
from interview.predict_hardskill import calculateHardSkill
import os
from moviepy import VideoFileClip 
import time
import asyncio
import numpy as np
import requests
import re

app=FastAPI()
app.mount('/static',StaticFiles(directory='static'),name="static")
templates=Jinja2Templates(directory='templates')





@app.middleware("http")
async def convert_token_into_user(request: Request, call_next):
    request.state.user = None  # default
    token = request.cookies.get('token')
    print('token is ',token)
    if token:
        try:
            payload = verify_token(token=token)
            print('payload is ',payload)
            request.state.user = payload  # store user info
        except JWTError:
            request.state.user = None

    response = await call_next(request)
    return response   


@app.middleware("http")
async def flash_middleware(request: Request, call_next):

    flash_message = request.cookies.get("flash")
    print('in the flash', flash_message)

    if flash_message:
        try:
            request.state.flash = json.loads(flash_message)
        except:
            request.state.flash = None
    else:
        request.state.flash = None

    response = await call_next(request)

    # delete after reading (one-time use)
    if flash_message:
        response.delete_cookie("flash")

    return response


@app.get('/')
def showLandingPage(request:Request):
    print(request.state.user)
    return templates.TemplateResponse(request=request,name="index.html",
                                      context={
                                            "user": request.state.user ,
                                            "flash":request.state.flash
    })

@app.get('/register')
def register_page(request:Request):
    return templates.TemplateResponse(request=request,name='register.html')


@app.post('/register/candidate')
def register_candidate(request: Request,response:Response ,
                       candidate: CandidateModel = Depends(validate_candidate),
                       check: bool = Depends(check_in_DB),
                       ):
  
    if check:
        response=RedirectResponse(url='/register',status_code=303)
        response.set_cookie('flash',value=json.dumps({"msg": "Already Registered", "type": "error"}))
        return 

    else:
        candidate=request.state.data  
        user_id=str(uuid.uuid4())
        user={
            "id":user_id,
            'email':candidate['email'],
            "password":candidate['password'],
            'assosiated_with':candidate['id'],
            'role':"Candidate"
        }

        del candidate['email'], candidate['password']
        print('in the register',candidate)
        create_candidate(**candidate)
        create_user(**user)
        del user['password']
        token=create_access_token(user)
        response=RedirectResponse(url='/',status_code=303)
        response.set_cookie('token',token)
        response.set_cookie('flash',value=json.dumps({"msg": "Registered successful", "type": "success"}))
     
    return response

@app.post('/register/company')
def register_company(   
                        request:Request,
                        response:Response ,
                        company: CompanyModel = Depends(validate_company),
                        check:bool=Depends(check_in_DB)
                     ):
    if check:
        response=RedirectResponse(url='/register',status_code=303)
        response.set_cookie('flash',value=json.dumps({"msg": "Already Registered a Company with This Email", "type": "error"}))
        return response

    else:
        print('route ka else ma hn')
        data=request.state.data
        user={
            "id":str(uuid.uuid4()),
            "email":data['email'],
            "password":data['password'],
            "role":'Company',
            "assosiated_with":data['id'],
        }
        del data['email'], data['password']
        # print(user)
        # print(data)
        create_user(**user)
        create_company(**data)
        del user['password']
        token=create_access_token(user)
        response=RedirectResponse(url='/dashboard',status_code=303)
        response.set_cookie('token',token)
        response.set_cookie('flash',value=json.dumps({"msg": "Registered Your Company Successful", "type": "success"}))
     
    return response

@app.get('/login')
def login(request:Request):
    return templates.TemplateResponse(request=request,name='login.html',context={
        "flash":request.state.flash
    })

@app.post('/login')
def login(email:EmailStr=Form(...),password:str=Form(...)):
    password=hash_password(password)
    result=get_user(email=email)
    if result['success']:
        user=result['success'][0]
        del user['password']
        token=create_access_token(user)
        route='/dashboard' if user['role']=='Company' else '/'
        response=RedirectResponse(route,status_code=303)
        response.set_cookie('token',token)
        response.set_cookie(key='flash',value=json.dumps({"msg": "Login Successfully", "type": "success"}))
        return response

    else :
        response=RedirectResponse('/login',status_code=303)
        response.set_cookie('flash',value=json.dumps({"msg": "Invalid Credentials", "type": "success"}))
        return response

@app.get('/logout')
def logout_user(response:Response):
    response=RedirectResponse('/')
    response.set_cookie('token',None)
    response.set_cookie('flash',value=json.dumps({"msg": "Logout Successful", "type": "success"}))
    return response


@app.get('/jobs')
def show_jobs(request:Request):
        print(request.state.user)
    # if request.state.user and request.state.user['role']=="Candidate":
        jobs=get_all_jobs()
        print(jobs)
        for job in jobs:
            job["created_at"] = job["created_at"].isoformat()
        return templates.TemplateResponse(request=request,name="jobs.html",context={"jobs":jobs,'user':request.state.user})
    
    # else:
        # return RedirectResponse('/login')

@app.get('/job/{job_id}')
def particular_job(request:Request,job_id:str,check: bool = Depends(checkApplied)):
    job=get_jobs_by_id(job_id)
    query=f"select count(job_id) from candidate_job where job_id='{job_id}';"
    no_of_applications=execte_query(query)
    no_of_applications=no_of_applications['success'][0]['count(job_id)']


    qualified_candidates = []
    print(request.state.user)
    if request.state.user['role'] == "Company":
        qualified_candidates=get_placed_candidates_by_job(job_id=job_id)
        
        print(qualified_candidates)
    return templates.TemplateResponse(request=request,name='each_job.html',
                                      context={
                                        "user":request.state.user,
                                        "job":job['success'][0],
                                        "check":check,
                                        "no_of_applications":no_of_applications,
                                        "flash":request.state.flash,
                                        "qualified_candidates":qualified_candidates
                                      })


@app.post('/job/{job_id}/apply')
def apply_to_particular_job(request:Request,job_id:str,
                                check: bool = Depends(checkApplied),
                                resume: UploadFile = File(...)):
    if request.state.user and request.state.user['role']=='Candidate':

        if check==False:
            file_path = f"uploads/{resume.filename}"
            print(file_path)
            print(resume.filename)
            
            with open(file_path, "wb") as buffer:
                shutil.copyfileobj(resume.file, buffer)
            
            user=request.state.user
            candidate_id=user['assosiated_with']
            create_candidate_job(candidate_id=candidate_id,job_id=job_id,resume_path=file_path)
            response=RedirectResponse(f'/job/{job_id}',status_code=303)
            response.set_cookie('flash',value=json.dumps({"msg": "Applied SuccessFully", "type": "success"}))
            return response
        else:
            response=RedirectResponse(f'/job/{job_id}',status_code=303)
            response.set_cookie('flash',value=json.dumps({"msg": "Already Applied", "type": "error"}))
            return response
        
    else:
        return RedirectResponse(f'/job/{job_id}',status_code=303)


def load_resume(path:str):
    loader = PyPDFLoader(path)
    pages = loader.load()
    content=""
    for page in pages:
        cleaned = re.sub(r'(?<=\w) (?=\w)', '', page.page_content)
        content=content+cleaned
    print(content)
    return content


@app.get('/job/{job_id}/progress')
def check_job_progress(request: Request, job_id: str,applied:bool=Depends(checkApplied)):
    if request.state.user  and applied and request.state.user['role']=='Candidate':
        user = request.state.user
        candidate_id = user['assosiated_with']  # keep as-is if correct in DB

        # Get Job
        job = get_jobs_by_id(job_id=job_id)
        if not job['success']:
            raise HTTPException(status_code=500, detail="Invalid Job-Id")

        jd = job['success'][0]['description']
        # Get Candidate Job Record

        job_and_candidate = get_candidate_job(job_id=job_id, candidate_id=candidate_id)
        if not job_and_candidate['success']:
            raise HTTPException(status_code=500, detail="Invalid Candidate Id")

        record = job_and_candidate['success'][0]
        print('record founded')
        print(record)
        # If ATS score not calculated
        ats_score = record['ats_score']
        if record['ats_score'] is None:
            resume_path = record['resume_path']
            resume = load_resume(resume_path)
            print(resume)
            print("finding_ats")
            ats_score = find_ats(
                resume_text=resume,
                job_description=jd
            )


            # (Optional but recommended) Save ATS score in DB
            update_candidate_job(candidate_id=candidate_id,job_id=job_id,ats_score=ats_score)
            print("founded_ats and saved it")

        if record['probablities'] is not None:
            record['probablities']=json.loads(record['probablities'])

        print(record)
        # Final Response
        return templates.TemplateResponse(
            request=request,
            name="job_progress.html",
            context={
                'ats_score':ats_score,
                "job_candidate":record,
                'user':user,
                "job":job['success'][0],
            }
        )
    
    else:
        return RedirectResponse(f'/job/{job_id}')
        

@app.get('/job/{job_id}/interview')
def showInterviewPage(request: Request, job_id: str):
    if request.state.user and request.state.user['role']=='Candidate':
        result = get_jobs_by_id(job_id=job_id)

        if not result['success']:
            raise HTTPException(status_code=401)

        job = result['success'][0]
        raw_questions = job.get('questions')

        if raw_questions is not None:

            if isinstance(raw_questions, str):
                questions = json.loads(raw_questions)
            else:
                questions = raw_questions

        else:
            questions = generate_question_answer(job['description'])
            update_job(job_id=job_id, questions=questions)
        return templates.TemplateResponse(
            request=request,
            name="job_interview.html",
            context={
                "job_id": job_id,
                "questions": questions
            }
        )
    
    else:
        return RedirectResponse(f'/job/{job_id}')


@app.post('/job/{job_id}/interview')
def get_particular_job_interview(request: Request,job_id: str,question_no: int = Form(...),video: UploadFile = File(...)):
    if request.state.user and request.state.user['role']=='Candidate':    
        user_id = request.state.user['assosiated_with']
        # Create folders
        os.makedirs("videos", exist_ok=True)
        os.makedirs("audios", exist_ok=True)

        base_name = f"{job_id}_cid_{user_id}_q{question_no}"

        video_path = f"videos/{base_name}.mp4"
        audio_path = f"audios/{base_name}.mp3"
        video_no_audio_path = f"videos/{base_name}_noaudio.mp4"

        # 💾 Save uploaded video
        with open(video_path, "wb") as buffer:
            shutil.copyfileobj(video.file, buffer)

        # ✅ CLOSE upload file explicitly
        video.file.close()

        clip = None

        try:
            # 🎬 Load video
            clip = VideoFileClip(video_path)

            # 🎤 Extract audio
            if clip.audio is not None:
                clip.audio.write_audiofile(audio_path, logger=None)
                clip.audio.close()   # ✅ IMPORTANT
            else:
                audio_path = None

            # 🎥 Save video without audio
            no_audio_clip = clip.without_audio()
            no_audio_clip.write_videofile(
                video_no_audio_path,
                audio=False,
                logger=None
            )
            no_audio_clip.close()   # ✅ IMPORTANT

            update_candidate_video_path(candidate_id=user_id,job_id=job_id,video_path=video_no_audio_path)

        except Exception as e:
            print("Error:", e)

            # cleanup on failure
            if os.path.exists(video_path):
                try:
                    os.remove(video_path)
                except:
                    pass

            return {"error": str(e)}

        finally:
            # ✅ Proper cleanup
            try:
                if clip:
                    clip.close()
            except:
                pass

            # ⏳ wait a bit to release OS lock
            time.sleep(0.5)

            # 🧹 remove original uploaded file
            if os.path.exists(video_path):
                try:
                    os.remove(video_path)
                except Exception as e:
                    print("Delete error:", e)

        return {
            "msg": "Processed successfully",
            "question_no": question_no,
            "audio_path": audio_path,
            "video_no_audio_path": video_no_audio_path
        }
    
    else:
        return RedirectResponse(f'/job/{job_id}')



async def handle_interview_hard_and_soft(video_url:str,audio_url:str,question:str):
    rating=await FindSoftSkill(video_url)
    hard_score= await calculateHardSkill(audio_path=audio_url,question=question)
    print('hardskill -> ',hard_score,' --> rating :',rating)
    return rating,hard_score

    


@app.get('/job/{job_id}/interview/result')
def find_particular_interview_result(request:Request,job_id:str):
        
    if  request.state.user  and request.state.user['role']=='Candidate':
        candidate_id=request.state.user['assosiated_with']
        job_and_candidate = get_candidate_job(job_id=job_id, candidate_id=candidate_id)
        if not job_and_candidate['success']:
            raise HTTPException(status_code=500, detail="Invalid Candidate Id or job id")
        
        record = job_and_candidate['success'][0]

        # Particular Job fetching
        result = get_jobs_by_id(job_id=job_id)

        if not result['success']:
            raise HTTPException(status_code=401)

        job = result['success'][0]
        raw_questions = job.get('questions')
        questions=json.loads(raw_questions)
        print(questions)
        videos_path=record['interview_video_paths']
        videos_path=videos_path.split(',')
        ratings=[]
        hardskill_scores=[]
        for i, v_path in enumerate(videos_path):
            base_name = f"{job_id}_cid_{candidate_id}_q{i}"
            audio_path = f"audios/{base_name}.mp3"
            print(i,'==>',questions[i])
            rating,hardskill_score = asyncio.run(handle_interview_hard_and_soft(video_url=v_path,audio_url=audio_path,question=questions[i]))
            ratings.append(rating)
            hardskill_scores.append(hardskill_score)
            print("\nFinal Output:", ' rating -> ' ,rating,' -> ',hardskill_score) 

        ratings=np.array(ratings)
        hardskill_score=np.array(hardskill_score)
        avg_rating=np.mean(ratings)
        avg_hardskill=np.mean(hardskill_score)
        update_candidate_job(candidate_id=candidate_id,job_id=job_id,
                            softskill=avg_rating,amptitude_score=avg_hardskill
                            )
        
        response=RedirectResponse(f'/job/{job_id}/progress')
        return response
    
    else:
        return RedirectResponse(f'/job/{job_id}')


@app.get('/job/{job_id}/finalResult')
def getFinalResult(request:Request,job_id:str):

    if request.state.user and request.state.user['role']=='Candidate':
        candidate_id=request.state.user['assosiated_with']
        result=get_candidate_job(job_id=job_id,candidate_id=candidate_id)
        
        if not result['success']:
            raise HTTPException(status_code=401,detail='candidate_job not founded')
        
        candidate=get_candidate(id=candidate_id)

        if not candidate['success']:
            raise HTTPException(status_code=401,detail='candiate not founded')
        
        candidate=candidate['success'][0]
        record=result['success'][0]
        data={
                "cgpa": candidate['cgpa'],
                "internship":candidate['internship'],
                "certification": candidate['certification'],
                "projects": candidate['projects'],
                "apptitude_score":record['amptitude_score'],
                "softskill_rating": record['softskill'],
                "ExtracurricularActivities": 0,
                "placementT": 1,
                "SSC": candidate['ssc'],
                "HSC": candidate['hsc']        
        }
        print(data)
        url='http://127.0.0.1:80/predict'
        headers = {
            "Content-Type": "application/json"
        }

        response = requests.post(url, json=data, headers=headers)

        # Get JSON response
        result = response.json()
        print(result)
        response=RedirectResponse(f'/job/{job_id}/progress')
        if  record['result'] is None or record['probablities'] is None:
            update_candidate_job(candidate_id=candidate_id,job_id=job_id,
                                result=result['prediction'],
                                probablities=json.dumps(result['probability'])
                                ) 
            return response
            
        else:
            return response
        
    else:
        return RedirectResponse(f'/job/{job_id}')

    


# Company Routes

@app.get('/dashboard')
def companyPage(request:Request):
    if request.state.user and request.state.user['role']=='Company':
        cpId=request.state.user['assosiated_with']
        jobs=get_jobs_by_company(company_id=cpId)
        print(jobs)
        return templates.TemplateResponse(request=request, name="company/dashboard.html",context={
            'jobs':jobs
        })
    else:
        return RedirectResponse('/login')


@app.get('/company/create_job')
def show_create_job_page(request:Request):
    if request.state.user and request.state.user['role']=='Company':
        return templates.TemplateResponse(request=request,name='company/create_job.html',context={
            "user":request.state.user
        })
    else:
        return RedirectResponse('/login')


@app.post('/company/create_job')
def job_creation_route(request:Request,job: jobModel = Depends(validate_job)):
    if request.state.user and request.state.user['role']=='Company':
        try:
            data=request.state.data
            data['id']=str(uuid.uuid4())
            print(create_job(**data))   
            response=RedirectResponse(url='/company/create_job',status_code=303)
            response.set_cookie('flash',value=json.dumps({"msg": "Job Created Successfully", "type": "success"}))

            return response
        
        except Exception as e:
            print('error ma hn')
            raise HTTPException(status_code=500, detail=e)
        
    else:
        return RedirectResponse('/login')



