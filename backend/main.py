from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to Tradient Backend"}

@app.get("/health")
def health():
    return {"status": "OK"}
