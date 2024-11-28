from typing import Annotated

from fastapi import APIRouter, Path

router = APIRouter()

@router.get("/")
def list_items():
    return ["Items", "Item2"]


@router.get("/{item_id}/")
def get_item_by_id(item_id: Annotated[int, Path(ge=1, lt=1_000_000)]):
    return {"item": {"item_id": item_id}}