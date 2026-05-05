from fastapi import Request
from database.candidate_job import get_candidate_job

def checkApplied(request:Request,job_id:str):
    print('check applied ma')
    candidate_id=request.state.user['assosiated_with']
    print(candidate_id)
    print(job_id)
    result=get_candidate_job(job_id=job_id,candidate_id=candidate_id)
    print(result)
    if result['success']:
        return True
    else:
        return False
