from fastapi import APIRouter

from . import schemas, crud

router = APIRouter()

@router.post("/")
def create_user(user: schemas.CreateUser):
    return crud.create_user(user_in=user)