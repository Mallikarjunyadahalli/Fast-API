from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/")
def home():
    return {"wellcome to Learning Path Parameter."}

def load_student_data():
    with open("students.json", 'r') as file:
        return json.load(file)

@app.get("/student")
def student_data():
    return load_student_data()

# Path parameter ---> Student ID is the path parameter
@app.get("/student/{student_id}")
def get_student_id(student_id: str):
    data = load_student_data()
    return data[student_id]



    