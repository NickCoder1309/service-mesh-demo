from fastapi import FastAPI
import requests

app = FastAPI()


@app.get("/")
def home():
    data = requests.get("http://catalog-service:8000/books").json()
    return data
