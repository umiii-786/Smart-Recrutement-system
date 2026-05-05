from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from ats.preprocess_text import preprocess_with_lemmatization


model = SentenceTransformer("all-mpnet-base-v2")

def find_ats(resume_text,job_description):
    resume_text=preprocess_with_lemmatization(resume_text)
    job_description=preprocess_with_lemmatization(job_description)
    resume_emb = model.encode(resume_text)
    jd_emb = model.encode(job_description)
    score = cosine_similarity([resume_emb], [jd_emb])[0][0]
    print("Match Score:", score)
    return float(score)

