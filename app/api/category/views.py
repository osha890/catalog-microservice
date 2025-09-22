from typing import Annotated, Sequence

from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from starlette.status import HTTP_204_NO_CONTENT

from api.category import crud as category_crud
from api.category.dependencies import get_category_by_id
from api.category.schemas import CategoryCreate, CategoryPartial, CategoryRead
from core.config import settings
from core.db_helper import db_helper
from core.models import Category

router = APIRouter(
    prefix=settings.api.categories,
    tags=["Categories"],
)


@router.get(
    "/",
    response_model=Sequence[CategoryRead],
)
async def get_all_categories(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    return await category_crud.get_all_categories(
        session=session,
    )


@router.post(
    "/",
    response_model=CategoryRead,
    status_code=status.HTTP_201_CREATED,
)
async def create_category(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    category_create: CategoryCreate,
):
    return await category_crud.create_category(
        session=session,
        category_create=category_create,
    )


@router.get(
    "/{category_id}",
    response_model=CategoryRead,
)
async def get_category(
    category: Annotated[Category, Depends(get_category_by_id)],
):
    return category


@router.patch(
    "/{category_id}",
    response_model=CategoryRead,
)
async def update_category(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    category: Annotated[Category, Depends(get_category_by_id)],
    category_update: CategoryPartial,
):
    return await category_crud.update_category(
        session=session,
        category=category,
        category_update=category_update,
    )


@router.delete(
    "/{category_id}",
    status_code=HTTP_204_NO_CONTENT,
)
async def delete_category(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    category: Annotated[Category, Depends(get_category_by_id)],
):
    return await category_crud.delete_category(
        session=session,
        category=category,
    )
