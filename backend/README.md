## Database Schema (ER Diagram)
## Database Schema (ER Diagram)

The system consists of three main entities:

### Assignment
- id (Primary Key)
- title
- description

### Submission
- id (Primary Key)
- assignment_id (Foreign Key → Assignment.id)
- student_id
- content

### Evaluation
- id (Primary Key)
- submission_id (Foreign Key → Submission.id)
- plagiarism
- score
- feedback

### Relationships
- One Assignment can have many Submissions (1-to-Many)
- Each Submission has exactly one Evaluation (1-to-1)

### ER Diagram (Textual Representation)

Assignment
-----------
id (PK)
title
description

    |
    | 1-to-many
    |
Submission
-----------
id (PK)
assignment_id (FK)
student_id
content

    |
    | 1-to-1
    |
Evaluation
-----------
id (PK)
submission_id (FK)
plagiarism
score
feedback