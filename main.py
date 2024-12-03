from contextlib import asynccontextmanager

from fastapi import FastAPI

from api.v1 import router as router_v1
from models import Base, db_helper
from items import router as item_router
from users.views import router as users_router
from core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):

    yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
def get_index():
    return {"message": "Hello World"}


@app.get("/hello/")
def hello(name: str = "World"):
    return {"message": f"Hello, {name.title()}"}


app.include_router(router=router_v1, prefix=settings.api_v1_prefix)
app.include_router(users_router, prefix="/users", tags=["USERS"])
app.include_router(item_router, prefix="/items", tags=["ITEMS"])
