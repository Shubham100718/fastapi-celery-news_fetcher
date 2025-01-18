from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "News Fetcher API is running"}

