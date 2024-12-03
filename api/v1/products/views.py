from functools import partial

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from models import db_helper

from . import crud
from .dependicies import product_by_id
from .schemas import Product, ProductCreate, ProductUpdate, ProductUpdatePartial

router = APIRouter()


@router.get("/", response_model=list[Product])
async def get_products(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_products(session=session)


@router.get("/{product_id}/", response_model=Product)
async def get_product_by_id(product: Product = Depends(product_by_id)):
    return product


@router.post("/", response_model=Product, status_code=status.HTTP_201_CREATED)
async def create_product(
    product_in: ProductCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_product(session, product_in)


@router.put("/{product_id}")
async def update_product(
    product_update: ProductUpdate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
    product: Product = Depends(product_by_id),
):
    return await crud.product_update(session, product, product_update)


@router.patch("/{product_id}")
async def update_product_partial(
    product_update: ProductUpdatePartial,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
    product: Product = Depends(product_by_id),
):
    return await crud.product_update(session, product, product_update, partial=True)


@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
    product: Product = Depends(product_by_id),
) -> None:
    await crud.product_delete(session, product)
