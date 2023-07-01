from fastapi import FastAPI

app = FastAPI()

@app.post("/send")
def hello():
    return {"message": "Endpoint de FastAPI"}
