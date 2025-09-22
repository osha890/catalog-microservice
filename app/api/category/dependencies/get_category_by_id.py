from typing import Annotated

from fastapi import HTTPException
from fastapi.params import Depends, Path
from sqlalchemy.ext.asyncio import AsyncSession

from api.category.crud import get_category
from core.db_helper import db_helper
from core.models import Category


async def get_category_by_id(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    category_id: Annotated[int, Path],
) -> Category:
    category = await get_category(
        session=session,
        category_id=category_id,
    )
    if category is not None:
        return category

    raise HTTPException(
        status_code=404,
        detail=f"Category with ID {category_id} not found",
    )
