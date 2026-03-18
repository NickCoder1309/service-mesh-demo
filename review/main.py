from fastapi import FastAPI

app = FastAPI()


@app.get("/reviews")
def get_reviews():
    return [
        {"book": "Service Mesh in Action", "review": "Great book"},
        {"book": "Service Mesh in Action", "review": "Very useful"},
    ]
