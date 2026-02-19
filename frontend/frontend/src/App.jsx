import { useState } from "react";

function App() {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [assignmentId, setAssignmentId] = useState("");
  const [studentId, setStudentId] = useState("");
  const [content, setContent] = useState("");

  const createAssignment = async () => {
    try {
      const res = await fetch("http://127.0.0.1:8000/create-assignment", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ title, description }),
      });

      if (!res.ok) {
        const err = await res.text();
        alert("Backend error: " + err);
        return;
      }

      alert("Assignment Created");
    } catch (error) {
      alert("Server not reachable");
    }
  };

  const submitAssignment = async () => {
    try {
      const res = await fetch("https://assignment-platform-1.onrender.com/submit-assignment", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          assignment_id: Number(assignmentId),
          student_id: Number(studentId),
          content,
        }),
      });

      if (!res.ok) {
        const err = await res.text();
        alert("Backend error: " + err);
        return;
      }

      const data = await res.json();
      alert(
        `Submitted!\nScore: ${data.score}\nPlagiarism: ${data.plagiarism}`
      );
    } catch (error) {
      alert("Server not reachable");
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>Assignment Platform</h1>

      <h2>Create Assignment</h2>
      <input placeholder="Title" onChange={(e) => setTitle(e.target.value)} />
      <br /><br />
      <input
        placeholder="Description"
        onChange={(e) => setDescription(e.target.value)}
      />
      <br /><br />
      <button onClick={createAssignment}>Create Assignment</button>

      <hr />

      <h2>Submit Assignment</h2>
      <input
        placeholder="Assignment ID"
        onChange={(e) => setAssignmentId(e.target.value)}
      />
      <br /><br />
      <input
        placeholder="Student ID"
        onChange={(e) => setStudentId(e.target.value)}
      />
      <br /><br />
      <textarea
        placeholder="Content"
        onChange={(e) => setContent(e.target.value)}
      />
      <br /><br />
      <button onClick={submitAssignment}>Submit Assignment</button>
    </div>
  );
}

export default App;