from fastapi import FastAPI

app = FastAPI(title="NLP Powered Toy")

@app.get("/")
def home():
    return {"message": "NLP Powered Toy API is running!"}