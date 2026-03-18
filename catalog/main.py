from fastapi import FastAPI
import requests

app = FastAPI()


@app.get("/books")
def get_books():
    reviews = requests.get("http://review-service:8000/reviews").json()
    ratings = requests.get("http://rating-service:8000/ratings").json()

    return {
        "books": [
            {
                "title": "Service Mesh in Action",
                "reviews": reviews,
                "ratings": ratings,
            }
        ]
    }
