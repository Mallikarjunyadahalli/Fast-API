from fastapi import FastAPI

import json

app = FastAPI()

"""
HTTP Mthods

1. GET --> To just show or display any message on the website or page or on the application.



"""

@app.get("/")
def greet():
    return {"Hello Dosto swagath se abhi."}
    
@app.get("/hello")
def hello_page():
    return {"This is Hello page bro."}


# Helper Function
def load_data():
    with open("students.json", 'r') as file:
        return json.load(file)

@app.get("/student")
def students_data():
    return load_data()