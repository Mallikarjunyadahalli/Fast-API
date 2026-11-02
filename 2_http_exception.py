from fastapi import FastAPI, HTTPException
import json

app = FastAPI()

@app.get("/")
def home():
    return "WEllcome to learning Fast API."

def get_studenet_info():
    with open("students.json", 'r') as file:
        data = json.load(file)
        return data

@app.get("/student")
def display_student_data():
    return get_studenet_info()

@app.get("/student/{student_id}")
def studnet_id(student_id: str):
    data = get_studenet_info()

    if student_id not in data:
        raise HTTPException(
            status_code=404,
            detail=f"Student ID '{student_id}' not exist in student database."
        )

    return data[student_id]

