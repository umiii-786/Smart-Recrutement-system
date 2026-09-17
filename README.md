<div align="center">

# 🎯 HireAI — Hybrid AI Recruitment System

### *A Hybrid AI Approach for Automating and Optimizing the Recruitment Process*

**An end-to-end recruitment platform that screens resumes, measures interview confidence, grades technical knowledge, and predicts placement — in one unified, data-driven pipeline.**

<br>

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-D00000?style=for-the-badge&logo=keras&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![LightGBM](https://img.shields.io/badge/LightGBM-02569B?style=for-the-badge)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)

![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white)
![MLflow](https://img.shields.io/badge/MLflow-0194E2?style=for-the-badge&logo=mlflow&logoColor=white)
![DVC](https://img.shields.io/badge/DVC-13ADC7?style=for-the-badge&logo=dvc&logoColor=white)

<br>

![Status](https://img.shields.io/badge/Status-All_Modules_Implemented-success?style=flat-square)
![Modules](https://img.shields.io/badge/AI_Modules-4-blueviolet?style=flat-square)
![Degree](https://img.shields.io/badge/Final_Year_Project-QUEST_Nawabshah-informational?style=flat-square)
![License](https://img.shields.io/badge/License-Academic-lightgrey?style=flat-square)

<br>

<img src="assets/ui/landingPageFYP.png" alt="HireAI landing page" width="100%">

</div>

---

## 📑 Table of Contents

| | Section |
|---|---|
| 1 | [Overview](#-overview) |
| 2 | [The Problem](#-the-problem) |
| 3 | [Our Solution](#-our-solution) |
| 4 | [What Makes This Different](#-what-makes-this-different) |
| 5 | [System Architecture](#-system-architecture) |
| 6 | [The Four AI Modules](#-the-four-ai-modules) |
| 7 | [Results & Model Performance](#-results--model-performance) |
| 8 | [Data Insights](#-data-insights) |
| 9 | [Platform Walkthrough](#-platform-walkthrough) |
| 10 | [Database Design](#-database-design) |
| 11 | [Tech Stack](#-tech-stack) |
| 12 | [Getting Started](#-getting-started) |
| 13 | [Project Structure](#-project-structure) |
| 14 | [Limitations & Future Work](#-limitations--future-work) |
| 15 | [Team](#-team) |

---

## 🔍 Overview

**HireAI** is a Final Year Project built at the Department of Software Engineering, Quaid-e-Awam University of Engineering, Science & Technology (QUEST), Nawabshah.

It replaces the slow, subjective, manual stages of early-round recruitment with a **four-stage AI pipeline**. A candidate applies once, and the system automatically:

1. **Matches** their resume against the job description using semantic embeddings
2. **Measures** their interview confidence from facial expressions using a CNN
3. **Grades** their technical answers using speech-to-text and an LLM
4. **Predicts** whether they should be placed — using a model trained on real historical placement outcomes

Every stage produces a **transparent, numeric score** the recruiter can inspect, rather than one opaque black-box verdict.

---

## ❗ The Problem

Traditional early-stage hiring breaks down in four specific ways:

| Problem | Impact |
|---|---|
| 🐌 **Manual resume screening is slow** | Recruiters spend hours per role reading resumes that vary wildly in format |
| ⚖️ **Human judgement is inconsistent** | Two reviewers rate the same candidate differently; unconscious bias creeps in |
| 🎭 **No structured way to assess confidence** | Interview presence is judged on gut feeling, never measured |
| 📋 **No objective technical check early on** | Whether a candidate *actually knows the job* isn't verified until late rounds |

The result: high HR workload, delayed hiring, and decisions that are harder to justify or audit.

---

## 💡 Our Solution

<div align="center">
<img src="assets/architecture/system-architecture.png" alt="System architecture" width="100%">
<br><em>Complete system architecture — from candidate and recruiter portals through the four-module processing layer to the final output</em>
</div>

<br>

The candidate's journey runs through three visible phases:

```
  📄 Apply & Upload              🎥 AI Virtual Interview           📊 Final Prediction
  ─────────────────              ──────────────────────           ───────────────────
  Resume + Profile      ──►      Video answers recorded    ──►    All scores fused
  ATS similarity score           Confidence + Hard-skill          Placed / Not Placed
  (gate to next phase)           scored independently             + probability + advice
```

---

## ⭐ What Makes This Different

Most AI hiring systems in the literature focus on **one** slice of the problem — resume matching *or* video analysis *or* placement prediction. HireAI addresses all of them, and makes one deliberate design choice that sets it apart:

> ### 🔑 The resume does not decide who gets hired.
>
> In HireAI, resume similarity is a **gate**, not a verdict. It only determines whether a candidate advances to the interview stage — it is **deliberately excluded** from the final placement model.
>
> **Why this matters:** a resume is a self-reported document. Anyone can overstate skills or write persuasively. Systems that let resume wording directly drive the hiring score have no mechanism to catch inflated claims.
>
> The final decision in HireAI is made only from signals that are **harder to fake**:
> - 🎯 **Hard-skill score** — earned by actually answering technical questions
> - 😊 **Confidence score** — measured from the candidate's own interview video
> - 🎓 **Verified academic & experience record** — CGPA, HSC/SSC marks, internships, projects, certifications
>
> This mirrors how hiring genuinely works: *a resume gets you noticed; your knowledge, performance, and track record get you hired.*

<br>

| Design Principle | How HireAI Implements It |
|---|---|
| 🧩 **Full-funnel coverage** | Four coordinated modules span screening → interview → skill test → decision |
| 🔎 **Transparent, not black-box** | Each module reports its own score before fusion — recruiters see *why*, not just *what* |
| ⚖️ **Balanced decision-making** | Soft skills, hard skills, and academic record all contribute — no single signal dominates |
| 🧪 **Validated on real data** | Trained on real facial-expression images and real historical placement outcomes, not simulated profiles |
| 📈 **Experiment-tracked** | MLflow + DVC used for reproducible training runs and data versioning |

---

## 🏗️ System Architecture

The platform is organised into four layers:

| Layer | Responsibility |
|---|---|
| **Presentation** | Candidate web portal + Company/Recruiter dashboard |
| **Processing** | The four AI modules (resume, confidence, hard-skill, final decision) |
| **Data & Storage** | MySQL application database + model/artifact storage |
| **External Services** | Gemini Speech-to-Text API, LLM via LangChain |

---

## 🧠 The Four AI Modules

### 1️⃣ Resume Screening — Semantic ATS Matching

<table>
<tr><td width="58%">

Rather than counting keywords, this module compares the **meaning** of a resume against the **meaning** of the job description.

**Pipeline**
- Text cleaning, normalization, tokenization
- Stop-word removal and lemmatization
- Embedding generation via **Sentence-Transformers**
- **Cosine similarity** between resume and job-description vectors
- Threshold check → shortlist or reject

**Output:** ATS compatibility score (0–100%)

**Role in the system:** ✅ a *gate* to the next phase — intentionally **not** an input to the final placement model

</td><td width="42%">
<img src="assets/workflows/resumeWorflow.jfif" alt="Resume screening workflow" width="100%">
</td></tr>
</table>

---

### 2️⃣ Confidence Detection — Facial Expression CNN

<table>
<tr><td width="58%">

Measures how confident a candidate appears during their recorded interview, turning a subjective impression into a reproducible number.

**Pipeline**
- Video frame sampling
- Face detection & alignment (**OpenCV**)
- Resizing, normalization, data augmentation
- Deep feature extraction via fine-tuned **CNN**
- Binary classification → Confident / Unconfident

**Architectures compared:** Custom CNN · **EfficientNetV2B0** ✅ · MobileNetV3-Large · ResNet50

**Output:** Confidence score (0–100%)

</td><td width="42%">
<img src="assets/workflows/confidenceModuleFlow.png" alt="Confidence detection workflow" width="100%">
</td></tr>
</table>

---

### 3️⃣ Hard-Skill Evaluation — Speech-to-Text + LLM Grading

<table>
<tr><td width="58%">

Checks whether the candidate can **actually do the job**, not just how they present — the component most comparable systems omit entirely.

**Pipeline**
- Audio extracted from interview video
- Transcription via **Gemini Speech-to-Text**
- Each answer paired with its question
- **LLM (via LangChain)** scores each answer 0–100
- **Median** aggregation across all answers (robust to outliers)
- Threshold comparison → pass / fail

**Output:** Hard-skill score (0–100)

</td><td width="42%">
<img src="assets/workflows/HardskillFlow.jfif" alt="Hard-skill evaluation workflow" width="100%">
</td></tr>
</table>

---

### 4️⃣ Final Decision Model — Placement Prediction

<table>
<tr><td width="58%">

A supervised classifier trained on **historical placement outcomes** that fuses every prior signal into one auditable decision.

**Input features**
- 😊 Confidence score *(soft skill)*
- 🎯 Hard-skill score *(technical ability)*
- 🎓 CGPA, HSC & SSC marks
- 💼 Internships, Projects, Certifications
- 🏅 Extracurricular activities

**Algorithms compared:** Gradient Boosting · XGBoost · **LightGBM** ✅ · Stacked Meta-Model

**Output:** `Placed` / `NotPlaced` + prediction probability + improvement guidance

</td><td width="42%">
<img src="assets/workflows/FinalFlow.jfif" alt="Final decision workflow" width="100%">
</td></tr>
</table>

---

## 📊 Results & Model Performance

### Confidence Detection — Model Comparison

Four architectures were fine-tuned and evaluated on a held-out test set. **EfficientNetV2B0** was selected not for raw accuracy alone, but for showing the **smallest train–test gap** — the strongest evidence of genuine generalization rather than overfitting.

| Model | Test Accuracy | Test F1 | Selected |
|---|:---:|:---:|:---:|
| Custom CNN | — | — | |
| **EfficientNetV2B0** | **0.82** | **0.82** | ✅ |
| MobileNetV3-Large | — | — | |
| ResNet50 | — | — | |

> 📌 *Full per-model classification reports, accuracy/loss curves and confusion matrices for all four architectures are included under `assets/results/confidence/`.*

**Selected model (EfficientNetV2B0) — detailed metrics**

| Split | Accuracy | Macro F1 | Support |
|---|:---:|:---:|:---:|
| Train | 0.88 | 0.88 | 28,707 |
| **Test** | **0.82** | **0.82** | **7,178** |

<div align="center">
<table>
<tr>
<td><img src="assets/results/confidence/efficientnet-accuracy.png" width="100%"><br><em>Training vs validation accuracy</em></td>
<td><img src="assets/results/confidence/efficientnet-loss.png" width="100%"><br><em>Training vs validation loss</em></td>
</tr>
<tr>
<td><img src="assets/results/confidence/efficientnet-confusion-matrix.png" width="100%"><br><em>Test confusion matrix</em></td>
<td><img src="assets/results/confidence/efficientnet-classification-report.png" width="100%"><br><em>Classification report</em></td>
</tr>
</table>
</div>

---

### Placement Prediction — Model Comparison

All models were tuned via hyperparameter search with cross-validation and tracked in **MLflow**.

| Model | CV Accuracy | Train Accuracy | **Test Accuracy** | Test F1 | Selected |
|---|:---:|:---:|:---:|:---:|:---:|
| Gradient Boosting | 0.831 | 0.865 | 0.791 | 0.750 | |
| XGBoost | 0.830 | 0.881 | 0.789 | 0.747 | |
| **LightGBM** | **0.828** | **0.849** | **0.795** | **0.754** | ✅ |
| Stacked Meta-Model | — | 0.87 | 0.79 | 0.78 | |

**Why LightGBM?** It achieved the **highest test accuracy** while maintaining the **narrowest train–test gap (≈0.055)** of the boosted models — XGBoost, by contrast, showed a 0.09 gap, indicating more overfitting. The stacked meta-model added complexity without beating LightGBM on test accuracy.

**LightGBM — selected configuration**

```python
{
  'colsample_bytree': 0.8,  'learning_rate': 0.1,
  'max_depth': 5,           'n_estimators': 100,
  'num_leaves': 31,         'reg_alpha': 0,
  'reg_lambda': 1,          'subsample': 0.8
}
```

| Metric | Train | Test |
|---|:---:|:---:|
| Accuracy | 0.849 | **0.795** |
| Precision | 0.839 | 0.745 |
| Recall | 0.864 | 0.763 |
| F1 Score | 0.852 | **0.754** |

<div align="center">
<img src="assets/results/placement/lightgbm-confusion-matrix.png" alt="LightGBM confusion matrix" width="58%">
<br><em>LightGBM confusion matrix on the held-out test set</em>
</div>

---

## 📈 Data Insights

Exploratory analysis of the placement dataset confirmed that the features chosen for the final model genuinely relate to placement outcomes.

<div align="center">
<img src="assets/results/placement/feature-correlation.png" alt="Feature correlation heatmap" width="78%">
<br><em>Correlation heatmap — aptitude score (0.52), HSC marks (0.51), projects (0.47) and SSC marks (0.47) show the strongest relationships with placement status</em>
</div>

<br>

<div align="center">
<table>
<tr>
<td width="50%"><img src="assets/results/placement/class-distribution.png" width="100%"><br><em>Target class balance — 58.3% NotPlaced / 41.7% Placed</em></td>
<td width="50%"><img src="assets/results/placement/hardskill-vs-placement.png" width="100%"><br><em>Hard-skill score vs. placement outcome</em></td>
</tr>
<tr>
<td width="50%"><img src="assets/results/placement/softskill-vs-placement.png" width="100%"><br><em>Soft-skill rating vs. placement outcome</em></td>
<td width="50%"><img src="assets/results/placement/cgpa-extracurricular-impact.png" width="100%"><br><em>Impact of CGPA & extracurricular activities</em></td>
</tr>
</table>
</div>

<div align="center">
<img src="assets/results/placement/projects-certs-internships.png" alt="Placement rate by projects, certifications and internships" width="78%">
<br><em>Placement rate across projects, certifications and internships</em>
</div>

> 💡 **Key takeaway:** placement outcomes correlate most strongly with *demonstrated* attributes — test performance, academic marks, and completed projects — reinforcing the design decision to exclude self-reported resume text from the final model.

---

## 🖥️ Platform Walkthrough

### Landing Page
<img src="assets/ui/landingPageFYP.png" alt="Landing page" width="100%">

### Job Discovery — Candidate View
<img src="assets/ui/jobs_page_Fyp.png" alt="Jobs page" width="100%">

### Recruiter Dashboard
<img src="assets/ui/companyDashboardPic.png" alt="Company dashboard" width="100%">

*Live posting metrics, application volume, pending AI interviews and shortlisted candidates at a glance.*

### Phase 1 — Live ATS Feedback
<table>
<tr>
<td width="50%"><img src="assets/ui/ats-phase1.png" width="100%"><br><em>✅ Shortlisted — similarity above threshold</em></td>
<td width="50%"><img src="assets/ui/ats-rejected.png" width="100%"><br><em>❌ Not shortlisted — with transparent score</em></td>
</tr>
</table>

### Complete Application Journey
<div align="center">
<img src="assets/ui/final-prediction.png" alt="Final prediction screen" width="68%">
<br><em>All three phases with a full score breakdown and actionable improvement guidance rather than a bare rejection</em>
</div>

> 🎓 Note the candidate-facing feedback: *"You are a strong candidate, but we suggest focusing on your Hard Skills."* The system is designed as **decision support with feedback**, not a silent filter.

---

## 🗄️ Database Design

<div align="center">
<img src="assets/architecture/er-diagram.png" alt="ER diagram" width="88%">
</div>

| Table | Purpose |
|---|---|
| `user` | Authentication and role management (candidate / company) |
| `company` | Employer profile — name, industry, size, logo |
| `jobs` | Postings with description, location, type, interview questions |
| `candidate` | Academic & experience record — CGPA, HSC, SSC, internships, certifications, projects |
| `candidate_job` | **Junction table** storing every score: `ats_score`, `softskill`, `amptitude_score`, `result`, `probablities`, resume & video paths |

---

## 🛠️ Tech Stack

<table>
<tr><td width="24%"><b>🤖 AI / ML</b></td><td>Python · TensorFlow · Keras · Scikit-learn · LightGBM · XGBoost · OpenCV · Sentence-Transformers</td></tr>
<tr><td><b>🗣️ LLM / Speech</b></td><td>Gemini Speech-to-Text API · LangChain orchestration</td></tr>
<tr><td><b>📊 MLOps</b></td><td>MLflow (experiment tracking) · DVC (data versioning) · DagsHub</td></tr>
<tr><td><b>🎨 Frontend</b></td><td>HTML · CSS · JavaScript · Tailwind CSS</td></tr>
<tr><td><b>⚙️ Backend / DB</b></td><td>MySQL · FastAPI</td></tr>
<tr><td><b>🧰 Tooling</b></td><td>VS Code · Jupyter Notebook · Google Colab · Kaggle · Git</td></tr>
</table>

---

## 🚀 Getting Started

### Prerequisites

```bash
Python 3.10+      MySQL 8.0+      Git      pip / venv
```

### Installation

```bash
# 1 — Clone the repository
git clone <your-repository-url>
cd hybrid-ai-recruitment-system

# 2 — Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3 — Install dependencies
pip install -r requirements.txt

# 4 — Configure environment variables
cp .env.example .env
```

### Environment Configuration

```env
# Database
DB_HOST=localhost
DB_PORT=3306
DB_NAME=hireai
DB_USER=your_username
DB_PASSWORD=your_password

# External Services
GEMINI_API_KEY=your_gemini_api_key

# Model Thresholds
ATS_SCORE_THRESHOLD=0.60
HARDSKILL_PASS_THRESHOLD=50
```

### Database Setup

```bash
mysql -u root -p -e "CREATE DATABASE hireai;"
mysql -u root -p hireai < database/schema.sql
```

### Run the Application

```bash
uvicorn app.main:app --reload
```

Then open **http://localhost:8000**

### Reproduce Model Training

```bash
# Pull versioned datasets
dvc pull

# Train the confidence detection model
python src/confidence_detection/train.py

# Train the placement prediction model
python src/placement_prediction/train.py

# Inspect experiment runs
mlflow ui
```

> ⚠️ Update paths and commands above to match your actual repository layout before publishing.

---

## 📁 Project Structure

```
hybrid-ai-recruitment-system/
│
├── 📂 assets/                        # Diagrams, screenshots, result plots
│   ├── architecture/                 # System architecture, ER diagram
│   ├── workflows/                    # Per-module flowcharts
│   ├── ui/                           # Platform screenshots
│   └── results/                      # Model evaluation outputs
│       ├── confidence/
│       └── placement/
│
├── 📂 src/
│   ├── resume_screening/             # Module 1 — Sentence-BERT + cosine similarity
│   ├── confidence_detection/         # Module 2 — CNN facial expression model
│   ├── hardskill_evaluation/         # Module 3 — Gemini STT + LangChain LLM
│   └── placement_prediction/         # Module 4 — LightGBM final decision model
│
├── 📂 app/                           # FastAPI backend + routes
├── 📂 frontend/                      # HTML / CSS / JS / Tailwind interfaces
├── 📂 database/                      # Schema and migrations
├── 📂 notebooks/                     # EDA and experimentation
├── 📂 models/                        # Trained model artifacts
│
├── 📄 requirements.txt
├── 📄 dvc.yaml
├── 📄 .env.example
└── 📄 README.md
```

---

## ⚠️ Limitations & Future Work

We believe an honest account of limitations is part of good engineering.

### Current Limitations

| Limitation | Detail |
|---|---|
| 👁️ **Visual-only confidence** | Confidence is inferred from facial expressions alone; vocal tone and body language are not yet modelled |
| 🌍 **Cultural expression variance** | The facial-expression dataset may not represent all demographics equally — expression norms differ across cultures |
| 📼 **Recording quality dependence** | Poor lighting or low-resolution video degrades face detection and therefore confidence accuracy |
| 🤖 **LLM grading not yet human-validated** | Hard-skill scores have not been formally benchmarked against expert human graders |
| 📉 **Moderate placement accuracy** | ~0.795 test accuracy is useful as decision support, but not sufficient for fully autonomous hiring |
| 🎯 **Domain scope** | Evaluated primarily on technology/engineering roles |

### Planned Future Work

- 🎙️ **Voice-based confidence detection** — fuse vocal tone and speech fluency with the existing visual signal
- 👨‍💼 **Human-expert validation** — benchmark LLM hard-skill scores against expert graders to quantify agreement
- 📊 **Larger real-world interview datasets** — validate beyond the current dataset scale
- ⚖️ **Formal fairness auditing** — measure and report demographic performance gaps explicitly
- 🔌 **HRMS / ATS integration** — deployment-ready APIs for existing HR software
- 🌐 **Multilingual support** — extend speech-to-text and evaluation beyond English

---

## 👥 Team

<div align="center">

### Project Supervisor
**Engr. Mir Muhammad Junoo**
*Department of Software Engineering, QUEST Nawabshah*

<br>

### Development Team

| Name | Roll No. | Role |
|---|:---:|---|
| **Muhammad Umair** | 22-SW-01 | Group Leader |
| **Musaib Memon** | 22-SW-56 | Member |
| **Amanullah Pirzada** | 22-SW-27 | Member |

<br>

**Department of Software Engineering**
*Quaid-e-Awam University of Engineering, Science & Technology, Nawabshah*

</div>

---

## 📚 Project Documentation

| Document | Description |
|---|---|
| 📕 **Thesis** | Complete project thesis with methodology, experiments and results |
| 📊 **Presentation** | Final defence slide deck |
| 🖼️ **Poster** | Conference-style project poster |

---

## 📄 License

This project was developed as an academic Final Year Project at QUEST Nawabshah. Please contact the team before reuse or redistribution.

---

<div align="center">

### ⭐ If you find this project interesting, consider giving it a star!

**Built with dedication at QUEST Nawabshah** 🎓

</div>
