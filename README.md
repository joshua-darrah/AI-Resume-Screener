# 🚀 AI Resume Screening System

> Intelligent Resume Screening & Candidate Matching Platform powered by NLP and Machine Learning.

---

## 🧭 Product Overview

AI Resume Screening System is a lightweight Applicant Tracking System (ATS) that helps recruiters automatically analyze resumes, extract relevant skills, and rank candidates against job descriptions using machine learning techniques.

It replaces manual screening with fast, consistent, and data-driven candidate evaluation.

---

## ✨ Key Capabilities

- 📄 Upload resumes (PDF / DOCX)
- 🧠 Extract structured resume data using NLP
- 🎯 Detect technical and soft skills automatically
- 📌 Match candidates to job descriptions
- 📊 Generate similarity-based ranking scores
- ⚡ Instant AI-powered evaluation results

---

## 🏗️ System Architecture

```
Candidate Resume
        ↓
Document Parser (PDF/DOCX)
        ↓
Text Processing Layer (NLP)
        ↓
Skill Extraction Engine
        ↓
Vectorization (TF-IDF)
        ↓
Similarity Engine (Cosine Similarity)
        ↓
Candidate Match Score
        ↓
Recruiter Dashboard Output
```

---

## 🧠 AI & Data Processing Pipeline

The system uses a hybrid NLP approach:

- Rule-based skill extraction for precision
- TF-IDF vectorization for text representation
- Cosine similarity for relevance scoring

This ensures both speed and interpretability.

---

## 🛠️ Tech Stack

### Backend
- Python
- Flask

### Machine Learning / NLP
- Scikit-learn
- spaCy
- NLTK
- TF-IDF
- Cosine Similarity

### Document Processing
- pdfplumber
- python-docx

### Frontend
- HTML
- CSS

---

## 📁 Project Structure

```
AI-Resume-Screener/
│
├── app.py
├── requirements.txt
│
├── templates/
│   └── index.html
│
├── uploads/
│
├── utils/
│   ├── matcher.py
│   ├── resume_parser.py
│   ├── skill_extractor.py
│   └── skills.py
│
└── models/
```

---

## ⚙️ How It Works

1. Upload a resume (PDF or DOCX)
2. System extracts raw text from document
3. NLP engine identifies relevant skills
4. Recruiter enters job description
5. AI computes similarity score
6. Candidates are ranked based on match percentage

---

## 📊 Scoring Logic

The system calculates similarity between resume and job description using:

- TF-IDF vectorization
- Cosine similarity measurement

### Score Interpretation

| Score | Meaning |
|------|--------|
| 0.80 – 1.00 | Strong match |
| 0.50 – 0.79 | Moderate match |
| 0.00 – 0.49 | Weak match |

---

## 💡 Example

### Job Description
```
Python Flask developer with SQL and machine learning experience.
```

### Resume
```
Software engineer experienced in Python, Flask, SQL, and ML systems.
```

### Result
```
Match Score: 87%
```

---

## 🚀 Getting Started

### 1. Clone repository
```bash
git clone https://github.com/joshua-darrah/AI-Resume-Screener
```

### 2. Move into project
```bash
cd AI-Resume-Screener
```

### 3. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 5. Run application
```bash
python app.py
```

### 6. Open in browser
```
http://127.0.0.1:5000
```

---

## 🔮 Roadmap

### Phase 1 (Current)
- Resume parsing system
- Skill extraction engine
- TF-IDF matching

### Phase 2
- Multi-candidate ranking system
- Database integration (PostgreSQL)
- Recruiter dashboard UI

### Phase 3
- Semantic search using transformers (BERT)
- AI-generated interview questions
- Resume feedback engine

### Phase 4
- Full SaaS deployment
- Authentication system
- Cloud hosting (AWS / Render)

---

## 📈 Potential Use Cases

- HR recruitment automation
- Internship screening systems
- University placement portals
- Freelance talent matching platforms

---

## 🎯 Learning Impact

This project demonstrates practical knowledge in:

- Machine learning applications in NLP
- Real-world backend system design
- Document processing pipelines
- AI-based ranking systems
- Full-stack Python development

---

## 👤 Author

**Joshua Darrah**

- GitHub: https://github.com/joshua-darrah  
- LinkedIn: https://www.linkedin.com/in/joshuadarrah/

---

## 📄 License

MIT License — open for learning and improvement.

---

## ⭐ Closing Note

This project is designed as a foundation for scalable AI recruitment systems. It can be extended into a production-ready SaaS platform with advanced ML and cloud infrastructure.
