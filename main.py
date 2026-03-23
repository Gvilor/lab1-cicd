from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Numbers(BaseModel):
    a: float
    b: float


@app.get("/")
def read_root():
    return {"message": "Hello, CI/CD Lab UPDATED"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/sum")
def calculate_sum(numbers: Numbers):
    return {"result": numbers.a + numbers.b}


@app.get("/multiply")
def multiply(a: float, b: float):
    return {"result": a * b}