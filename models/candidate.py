from pydantic import BaseModel,Field,EmailStr

class CandidateModel(BaseModel):
    name:str=Field(...,description="Enter the Username")
    email:EmailStr=Field(...,description="Enter the Valid Email")
    password:str=Field(...,description="Enter Password")
    internship:int=Field(...,description="specify internship you have done")
    certification:int=Field(...,description="specfiy certifications"),
    projects:int=Field(...,description="specify no of projects"),
    hsc:float=Field(...,description="marks in intermediate"),
    ssc:float=Field(...,description="marks in matric"),
    cgpa:float=Field(...,description="enter cgpa between 0 to 10",min=0,max=10)
