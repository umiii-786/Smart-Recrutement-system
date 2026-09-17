from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from ats.preprocess_text import preprocess_with_lemmatization
# from preprocess_text import preprocess_with_lemmatization


model = SentenceTransformer("all-mpnet-base-v2")

def find_ats(resume_text,job_description):
    print('finding')
    resume_text=preprocess_with_lemmatization(resume_text)
    print('processed resume')
    job_description=preprocess_with_lemmatization(job_description)

    print('preprocessed jd',job_description,' \n\n')
    print('preprocessed resume',resume_text)
    resume_emb = model.encode(resume_text)
    jd_emb = model.encode(job_description)
    score = cosine_similarity([resume_emb], [jd_emb])[0][0]
    print("Match Score:", score)
    return float(score)


# jd="""
# **Job Title: Python Backend Developer**

# **Location:** [City, Country] / Remote
# **Employment Type:** Full-Time

# ### Job Summary

# We are seeking a skilled and motivated Python Backend Developer to design, develop, and maintain scalable backend applications and APIs. The ideal candidate should have strong expertise in Python, backend frameworks, databases, and RESTful API development. The developer will work closely with frontend developers, DevOps engineers, and product teams to build secure, efficient, and high-performance systems.

# ### Key Responsibilities

# * Design, develop, test, and maintain backend applications using Python.
# * Build and manage RESTful APIs and microservices.
# * Develop server-side logic to support frontend applications.
# * Design and optimize relational and non-relational databases.
# * Integrate third-party APIs and external services.
# * Write clean, reusable, and well-documented code.
# * Implement authentication, authorization, and security best practices.
# * Optimize application performance, scalability, and reliability.
# * Perform debugging, troubleshooting, and code reviews.
# * Collaborate with cross-functional teams throughout the software development lifecycle.
# * Participate in deployment and maintenance processes.

# ### Required Skills

# * Strong proficiency in Python programming.
# * Experience with backend frameworks such as **Flask**, **Django**, or **FastAPI**.
# * Knowledge of REST API development and API documentation tools.
# * Experience with databases such as **PostgreSQL**, **MySQL**, **MongoDB**, or **SQLite**.
# * Familiarity with ORM tools such as SQLAlchemy or Django ORM.
# * Understanding of authentication methods such as JWT and OAuth.
# * Knowledge of Git and version control systems.
# * Familiarity with Docker and containerization technologies.
# * Understanding of software design patterns and clean coding practices.

# ### Preferred Skills

# * Experience with cloud platforms such as AWS, Azure, or Google Cloud.
# * Knowledge of CI/CD pipelines and DevOps practices.
# * Familiarity with Redis, Celery, and message queues.
# * Experience with microservices architecture.
# * Knowledge of unit testing frameworks such as PyTest.

# ### Educational Qualifications

# * Bachelor’s degree in Computer Science, Software Engineering, Information Technology, or a related field.

# ### Experience

# * 1–3 years of experience for Junior Python Backend Developer.
# * 3+ years of experience for Mid/Senior Python Backend Developer.

# ### Nice to Have

# * Experience in AI/ML model deployment.
# * Knowledge of MLOps tools such as MLflow, Docker, and Kubernetes.
# * Experience working with scalable and distributed systems.

# """

# resumeContent="""
# Developed AgroNex, an AI-powered web application for crop disease detection, crop
# recommendation, and agricultural guidance.
# Built a CNN model to classify crop diseases from images with high accuracy and real-time prediction
# support.
# Achieved 97.5% test accuracy and 99.1% train accuracy using Random Forest for crop
# recommendation. Implemented fertilizer prediction achieving 96.6% test accuracy and 95.5% train
# accuracy.
# Integrated Gemini API to provide chatbot-based real-time agricultural consultation. Added weather
# forecasting functionality via weather API to support data-driven farming decisions
# Linkedin umiii215020@gmail.com| (+92-313-3300-758) Github
# Nawabshah
# June 2024 – July 2024 |
# PROJECTS
# EXPERIENCE:
# HighTech Software (Remote) Web Developer Intern –
# HTML, CSS, JavaScript, nodejs
# Developed full-stack web applications using HTML, CSS, JavaScript, and nodejs.
# Implemented user authentication, form validation, and CRUD operations.
# Designed responsive, user-friendly interfaces for cross-device compatibility.
# Utilized Git and GitHub for version control and clean code management.
# Completed 10+ real-world tasks and mini-projects to strengthen development
# skills.
# Flask, Machine Learning (EDA, Feature Engineering, Random Forest), CNN View
# MLOps Pipeline, Machine Learning, DVC, MLflow ViewCode
# Developed an end-to-end machine learning system to predict employee churn using a modular and
# scalable architecture.
# Performed data preprocessing, feature engineering, and model training to build a robust predictive model.
# Implemented experiment tracking and model registry using MLflow (with DagsHub) to compare and select
# the best-performing model.
# Automated the complete ML pipeline using DVC, ensuring reproducibility with version-controlled
# workflows (dvc.yaml).
# Managed data versioning with DVC integrated with AWS S3 for efficient data handling.
# Applied MLOps best practices using Git/GitHub, with structured logging and monitoring across the pipeline.
# LangChain, YT API, Vector Database, LLMs ViewCode
# Developed a YouTube video chatbot capable of answering questions about the currently playing video using
# Retrieval-Augmented Generation (RAG).
# Extracted YouTube video transcripts through the YouTube API and built an automated document ingestion
# pipeline.
# Implemented transcript chunking, embedding generation, and semantic search using vector databases.
# Integrated Large Language Models (LLMs) with retrieved context to generate accurate, context-aware responses.
# Delivered real-time question answering with optimized retrieval performance for production-like usage.
# Muhammad Umair
# AgroNex
# YouTube Video RAG Chatbot PLugin
# Employee Churn Prediction with MLOPS Practices
# Portfolio Kaggle
# Quaid-e-Awam University of Engineering, Science and Technology 2022-2026
# B.E. in Software Engineering CGPA: 3.5
# IBM Machine Learning Certificate
# Ranked Among 3% nationwide in NSTC test secured 97.2 percentile .
# Education
# Achievements
# Technical Skills
# SoftSkills
# (Team Players) Technical and Management Member at CATCH VR
# Project, Where I helped in Managed Event, contribute in workshop.
# Programming Languages: Python, JavaScript
# Frameworks & Libraries: Flask, Express.js, Pandas, Scikit-learn, TensorFlow, pytorch, langchain,
# langgraph
# Databases: MySQL, MongoDB (Basic)
# Tools & Platforms: Git, DVC, MLFLOW, CI/CD , AWS (S3, EC2, IAM, ASG, ELB) , Docker (Basic)
# Other Skills: Data Analysis, REST APIs

# """
# find_ats(job_description=jd,resume_text=resumeContent)
