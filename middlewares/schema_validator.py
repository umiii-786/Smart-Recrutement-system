from fastapi import Request,Form,HTTPException
from pydantic import ValidationError,HttpUrl
from models.candidate import CandidateModel
from models.company import CompanyModel
from models.jobs import jobModel

def validate_candidate(request: Request,name: str = Form(...),email: str = Form(...),
                       password: str = Form(...),
                       internship:int=Form(...),
                       certification:int=Form(...),
                       projects:int=Form(...),
                       hsc:float=Form(...),
                       ssc:float=Form(...),
                       cgpa:float=Form(...)
                       
                       ):
    
    data = {"name": name, "email": email,
            "password": password,
            "internship":internship,
            "certification":certification,
            "projects":projects,
            "hsc":hsc,
            "ssc":ssc,
            "cgpa":cgpa
            }
    try:
        print('in the candidate validation',data)
        obj = CandidateModel(**data)
        print('obj is',obj)
        request.state.data = obj.dict()   # ✅ attach to request
        return obj
    except ValidationError as e:
        messages = [err['msg'] for err in e.errors()]
        raise HTTPException(status_code=500, detail=" ".join(messages))

def validate_company(request: Request,company_name: str = Form(...),
                     email: str = Form(...),password: str = Form(...),
                     industry:str=Form(...), size:str=Form(...),
                     logo_url:str=Form(...)
                     ):
    data = {
            "company_name": company_name,
            "email": email, 
            "password": password,
            "industry":industry,
            "size":size,
            "logo_url":HttpUrl(logo_url)
            }
    print('in the company validate ',data)
    try:
        obj = CompanyModel(**data)
        obj.logo_url=str(obj.logo_url)
        request.state.data = obj.dict()   # ✅ attach to request
        return obj
    except ValidationError as e:
        messages = [err['msg'] for err in e.errors()]
        raise HTTPException(status_code=500, detail=" ".join(messages))

def validate_job(request:Request,company_id:str=Form(...),title:str=Form(...),department:str=Form(...),location:str=Form(...),
               type:str=Form(...),description:str=Form(...)):
    job={
        'company_id':company_id,
        'title':title,
        'department':department,
        "location":location,
        "description":description,
        "job_type":type
    }
    try:
        obj = jobModel(**job)
        request.state.data = obj.dict()   # ✅ attach to request
        return obj
    except ValidationError as e:
        messages = [err['msg'] for err in e.errors()]
        raise HTTPException(status_code=500, detail=" ".join(messages))
