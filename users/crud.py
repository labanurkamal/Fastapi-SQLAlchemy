"""
CREATE
READ
UPDATE
DELETE
"""

from . import schemas


def create_user(user_in: schemas.CreateUser):
    user = user_in.model_dump()
    return {"success": True, "user": user}
