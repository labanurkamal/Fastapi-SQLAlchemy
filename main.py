from fastapi import FastAPI

from items import router as item_router
from users.views import router as users_router

app = FastAPI()


@app.get("/")
def get_index():
    return {"message": "Hello World"}


@app.get("/hello/")
def hello(name: str = "World"):
    return {"message": f"Hello, {name.title()}"}


app.include_router(users_router, prefix="/users", tags=["USERS"])
app.include_router(item_router, prefix="/items", tags=["ITEMS"])
