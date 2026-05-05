
from pydantic import BaseModel,Field
from typing import Literal,Annotated

class jobModel(BaseModel):
    company_id:str=Field(...,description='id of company')
    title:str=Field(...,description="job title"),
    department:Annotated[Literal[ "Engineering","Design","Marketing","Sales", "Human Resources","Technology"],
                         Field(...,description="department")
                         ]
    location:str=Field(...,description="Mentioned the Location"),
    description:str=Field(...,description="Enter the job description"),
    job_type:Annotated[Literal["Full-time","Part-time"],Field(...,description="choose Full-time,Part-time")]