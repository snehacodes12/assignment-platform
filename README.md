# Assignment Evaluation Platform

An AI-based assignment evaluation platform that enables instructors to create assignments, students to submit their work, and the system to evaluate submissions automatically.

## Features
. Assignment creation
. Student submission handling
. Automated evaluation
. Plagiarism checking
. Score and feedback generation

## Tech Stack

### Backend
. Python
. FastAPI
. SQLAlchemy
. SQLite

### Frontend
. React (Vite)
. JavaScript
. HTML
. CSS



## Project Structure
assignment-platform/
├── backend/
│   ├── main.py              # FastAPI entry point
│   ├── models.py            # Database models
│   ├── database.py          # Database configuration
│   ├── ai_engine.py         # Evaluation & plagiarism logic
│   ├── requirements.txt    # Backend dependencies
│   └── db.sqlite3           # SQLite database
│
├── frontend/
│   ├── package.json
│   ├── vite.config.js
│   ├── public/
│   │   └── index.html
│   └── src/
│       ├── assets/
│       ├── App.jsx
│       ├── main.jsx
│       └── App.css
│
├── docs/                    # Documentation & diagrams
├── .gitignore               # Git ignore rules
└── README.md                # Project documentation


## Backend setup

cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
Backend url
http://127.0.0.1:8000
Apps docs
http://127.0.0.1:8000/docs

## Frontend setup
cd frontend
npm install
npm run dev
 Frontend url
http://localhost:5173

Database Entities

Assignment
.id
.title
.description

Submission
.id
.assignment_id
.student_id
.content

Evaluation
.id
.submission_id
.plagiarism
.score
.feedback

Author
Sneha Codes



## Deployed Application

### Frontend (Vercel)
Live URL: https://assignment-platform-jmbf-j32a35qa1.vercel.app

The frontend is built using Vite + React and deployed on Vercel.
