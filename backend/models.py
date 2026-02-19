from sqlalchemy import Column, Integer, String, Text, ForeignKey
from database import Base

class Assignment(Base):
    __tablename__ = "assignments"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(Text)

class Submission(Base):
    __tablename__ = "submissions"

    id = Column(Integer, primary_key=True)
    assignment_id = Column(Integer, ForeignKey("assignments.id"))
    student_id = Column(Integer)
    content = Column(Text)

class Evaluation(Base):
    __tablename__ = "evaluations"

    id = Column(Integer, primary_key=True)
    submission_id = Column(Integer, ForeignKey("submissions.id"))
    plagiarism = Column(String)
    score = Column(Integer)
    feedback = Column(Text)