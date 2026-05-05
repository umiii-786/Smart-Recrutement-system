from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel
from typing import List
from dotenv import load_dotenv

load_dotenv()
class Question(BaseModel):
    questions:List[str]


def generate_question_answer(jd:str):
    # 1. Define the prompt template
    prompt= PromptTemplate(
        input_variables=["job_description"],
        template="""
            Based on the following job description, generate exactly 1 interview questions that assess the candidate’s hard/technical skills.

            Requirements:
            - Each question must be answerable within 30 seconds.
            - Questions should be precise, practical, and directly related to the core technical skills required for the role.
            - Avoid theoretical or opinion-based questions; focus on applied knowledge.
            - Questions should reflect real-world tasks or scenarios relevant to the job.
            - Do not include explanations or answers—only list the questions.

            Job Description:
            {job_description}
            """
    )

    model_name="gemini-2.5-flash"
    model = ChatGoogleGenerativeAI(
        model=model_name
    )
    structured_model=model.with_structured_output(schema=Question)
    chain=prompt | structured_model 

    results=chain.invoke({"job_description":jd})
    return results.questions

