from typing import Annotated

from fastapi import Depends, HTTPException, Path
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from api.product.crud import get_product
from core.db_helper import db_helper
from core.models import Product


async def get_product_by_id(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    product_id: Annotated[int, Path],
) -> Product:
    product = await get_product(
        session=session,
        product_id=product_id,
    )
    if product is not None:
        return product

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Product with ID {product_id} not found",
    )
