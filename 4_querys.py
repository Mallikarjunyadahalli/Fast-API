"""

? -> After this our query is present.
course = Python -> This is key-value pair.

"""

# https://127.0.0.8000/filter?course=Python 

from fastapi import FastAPI, Query
import json

app = FastAPI()

@app.get("/")
def home():
    return "Learning Fast API"

def load_student_data():
    with open("students.json", 'r') as file:
        data = json.load(file)

        return data

@app.get("/student")
def get_student_data():
    return load_student_data()

@app.get("/filter")
def filter_student_course(course: str = Query(..., description="Student course only", examples=['python', 'data science'])):
    data = load_student_data()

    filter = {}

    if course is None:
        return data

    for student_key, value in data.items():
        if value['course'] == course:
            filter[student_key] = value

    return filter