from typing import Annotated, Sequence

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from api.product import crud as product_crud
from api.product.dependencies import get_product_by_id
from api.product.schemas import ProductCreate, ProductPartial, ProductRead
from core.config import settings
from core.db_helper import db_helper
from core.models import Product

router = APIRouter(
    prefix=settings.api.products,
    tags=["Products"],
)


@router.get(
    "/",
    response_model=Sequence[ProductRead],
)
async def get_all_products(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    return await product_crud.get_all_products(
        session=session,
    )


@router.post(
    "/",
    response_model=ProductRead,
    status_code=status.HTTP_201_CREATED,
)
async def create_product(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    product_create: ProductCreate,
):
    return await product_crud.create_product(
        session=session,
        product_create=product_create,
    )


@router.get(
    "/{product_id}",
    response_model=ProductRead,
)
async def get_product(
    product: Annotated[Product, Depends(get_product_by_id)],
):
    return product


@router.patch(
    "/{product_id}",
    response_model=ProductRead,
)
async def update_product(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    product: Annotated[Product, Depends(get_product_by_id)],
    product_update: ProductPartial,
):
    return await product_crud.update_product(
        session=session,
        product=product,
        product_update=product_update,
    )


@router.delete(
    "/{product_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_product(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    product: Annotated[Product, Depends(get_product_by_id)],
):
    await product_crud.delete_product(
        session=session,
        product=product,
    )
