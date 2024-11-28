from fastapi import FastAPI

from pydantic import BaseModel, EmailStr


app = FastAPI()

class CreateUser(BaseModel):
    email: EmailStr


@app.get("/")
def get_index():
    return {
        "message": "Hello World"
    }

@app.get("/hello/")
def hello(name: str = "World"):
    return {"message": f"Hello, {name.title()}"}


@app.post("/users/")
def create_user(user: CreateUser):
    return {
        "message": "success",
        "email": user.email
    }

@app.get("/items/")
def list_items():
    return ["Items", "Item2"]


@app.get("/items/{item_id}")
def get_item_by_id(item_id: int):
    return {"item": {"item_id": item_id}}