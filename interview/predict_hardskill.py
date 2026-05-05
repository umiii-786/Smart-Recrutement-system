import os
import base64
import requests
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel,Field
from fastapi import HTTPException


class Answer_Correctness(BaseModel):
     score:int=Field(...,description="score in between 0 to 100")


load_dotenv()
# Configure Gemini

GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')
# genai.configure(api_key=GOOGLE_API_KEY)

# Load model
# model = genai.GenerativeModel("gemini-2.5-flash")


async def calculateHardSkill(audio_path,question):
   text=speech_to_text(audio_path)
   if(text):
    print(text)
    score=calculate_score(question=question,text=text)
    return score
   else:
       raise HTTPException(status_code=500,detail="Something Error occured while generating text from audio")
       
    

def calculate_score(question,text):

    prompt = PromptTemplate(template="""
        You are an expert AI interviewer.

        Evaluate the candidate's answer.

        Question:
        {question}

        Candidate Answer:
        {text}

        Scoring Criteria:
        - Relevance
        - Correctness
        - Completeness

        Rules:
        - Return ONLY a number between 0 and 100
        - Do NOT return text
        - Do NOT explain

        Score:
        """,
        input_variables=['question','text']
    )

    model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")
    structured_model=model.with_structured_output(Answer_Correctness)
    chain=prompt | structured_model
    result=chain.invoke({'question':question,'text':text})
    print(result)
    return result.score



def speech_to_text(audio_path):
    with open(audio_path, "rb") as f:
        audio_bytes = f.read()

    audio_base64 = base64.b64encode(audio_bytes).decode("utf-8")

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={GOOGLE_API_KEY}"

    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "inline_data": {
                            "mime_type": "audio/wav",
                            "data": audio_base64
                        }
                    },
                    {
                        "text": "Transcribe this audio into English text only."
                    }
                ]
            }
        ]
    }

    response = requests.post(url, json=payload)
    result = response.json()

    # Safety check (avoid crashes)
    try:
        return result["candidates"][0]["content"]["parts"][0]["text"]
    except Exception:
        return ""

# def speech_to_text(audio_path):
#     with open(audio_path, "rb") as f:
#         audio_bytes = f.read()

#     audio_base64 = base64.b64encode(audio_bytes).decode("utf-8")

#     response = model.generate_content(
#         [
#             {
#                 "inline_data": {
#                     "mime_type": "audio/wav",
#                     "data": audio_base64
#                 }
#             },
#             "Transcribe this audio into English text only."
#         ]
#     )

#     return response.text


