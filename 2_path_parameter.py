from fastapi import FastAPI, HTTPException
import json

app = FastAPI()

@app.get("/")
def home():
    return "Well come to learning Fast API."

def load_student_data():
    with open("students.json", 'r') as file:
        data = json.load(file)

        return data

@app.get("/student")
def get_student_data():
    return load_student_data()


@app.get("/student/{student_id}")
def get_student_id(student_id: str):
    data = load_student_data()

    if student_id not in data:
        raise HTTPException(
            status_code=404,
            detail=f"Student {student_id} id don't exist in database."
        )

    return data[student_id]

