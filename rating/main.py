from fastapi import FastAPI

app = FastAPI()


@app.get("/ratings")
def get_ratings():
    return [
        {"book": "Service Mesh in Action", "rating": 5},
        {"book": "Service Mesh in Action", "rating": 4},
    ]
