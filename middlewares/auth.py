from database.user import get_user
from fastapi import Request
import uuid
from auth.password_hash import hash_password

def check_in_DB(request:Request):
    result=get_user(email=request.state.data['email'])
    if result['success']:
        return True
    
    else:
        print(result['success'],'in else')
        data=request.state.data
        hashed_password=hash_password(data['password'])
        del data["password"]
        data['id']= str(uuid.uuid4())
        data['password']=hashed_password
        print('data is ',data)
        request.state.data=data
        return False
