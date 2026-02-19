from fastapi import FastAPI
from database import Base, engine, SessionLocal
from models import Assignment, Submission, Evaluation
from ai_engine import evaluate_assignment
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def root():
    return {
        "message": "Assignment Platform Backend is running",
        "docs": "/docs"
    }

class CreateAssignmentRequest(BaseModel):
    title: str
    description: str


class SubmitAssignmentRequest(BaseModel):
    assignment_id: int
    student_id: int
    content: str

Base.metadata.create_all(bind=engine)

@app.post("/create-assignment")
def create_assignment(data: CreateAssignmentRequest):
    db = SessionLocal()
    assignment = Assignment(
        title=data.title,
        description=data.description
    )
    db.add(assignment)
    db.commit()
    return {"message": "Assignment created"}

@app.post("/submit-assignment")
def submit_assignment(data: SubmitAssignmentRequest):
    db = SessionLocal()

    submission = Submission(
        assignment_id=data.assignment_id,
        student_id=data.student_id,
        content=data.content
    )
    db.add(submission)
    db.commit()

    previous = [s.content for s in db.query(Submission).all()]
    plagiarism, score, feedback = evaluate_assignment(
        data.content, previous
    )

    evaluation = Evaluation(
        submission_id=submission.id,
        plagiarism=plagiarism,
        score=score,
        feedback=feedback
    )
    db.add(evaluation)
    db.commit()

    return {
        "plagiarism": plagiarism,
        "score": score,
        "feedback": feedback
    }