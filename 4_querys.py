from fastapi import FastAPI,  HTTPException, Path

app = FastAPI()

@app.get("/items/")

async def read_items(q: str | None = None):
    if q:
        return {"message": f"Searching for {q}"}
    return {"message": "Returning all items"}


def get_studenet_info():
    with open("students.json", 'r') as file:
        data = json.load(file)
        return data

@app.get("/student")
def display_student_data():
    return get_studenet_info()

@app.get("/student/{student_id}")
def studnet_id(student_id: str = Path(..., description="The ID of the Student", examples=["2001"] )):
    # ... -----> It means Infortant.
    data = get_studenet_info()

    if student_id not in data:
        raise HTTPException(
            status_code=404,
            detail=f"Student ID '{student_id}' not exist in student database."
        )

    return data[student_id]