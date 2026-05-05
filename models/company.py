from pydantic import BaseModel,Field,EmailStr,HttpUrl
from typing import Literal,Annotated

class CompanyModel(BaseModel):
    company_name:str=Field(...,description="name of company like xeven solutions")
    email:EmailStr=Field(...,description="email for company account")
    industry:str=Field(...,description="industry that company capture like Tech/Finance")
    size:Annotated[Literal['1-10','11-50','51-200','200+'],Field(...,description="Size of Company")]
    password:str=Field(...,description="password for company account")
    logo_url:HttpUrl=Field(...,description="link of company logo")

