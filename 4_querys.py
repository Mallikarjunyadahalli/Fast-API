from fastapi import FastAPI

app = FastAPI()

@app.get("/items/")

async def read_items(q: str | None = None):
    if q:
        return {"message": f"Searching for {q}"}
    return {"message": "Returning all items"}
