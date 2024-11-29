from fastapi import APIRouter

from . import crud, schemas

router = APIRouter()


@router.post("/")
def create_user(user: schemas.CreateUser):
    return crud.create_user(user_in=user)
