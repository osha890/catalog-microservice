import asyncio
from decimal import Decimal
from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from api.product.schemas import ProductCreate, ProductPartial
from core.db_helper import db_helper
from core.models import Product


async def create_product(
    session: AsyncSession,
    product_create: ProductCreate,
) -> Product:
    product = Product(**product_create.model_dump())
    session.add(product)
    await session.commit()
    await session.refresh(product)
    return product


async def get_all_products(
    session: AsyncSession,
) -> Sequence[Product]:
    stmt = select(Product).order_by(Product.id)
    result = await session.scalars(stmt)
    return result.all()


async def get_product(
    session: AsyncSession,
    product_id: int,
) -> Product | None:
    return await session.get(Product, product_id)


async def update_product(
    session: AsyncSession,
    product: Product,
    product_update: ProductPartial,
) -> Product:
    for name, value in product_update.model_dump(exclude_unset=True).items():
        setattr(product, name, value)
    await session.commit()
    return product


async def delete_product(
    session: AsyncSession,
    product: Product,
) -> None:
    await session.delete(product)
    await session.commit()


# async def main():
#     async with db_helper.session_factory() as session:
#         product = await create_product(
#             session,
#             ProductCreate(
#                 name="MegaTestProduct",
#                 price=Decimal(10.00),
#                 category_id=2,
#             ),
#         )
#         print(f"create: {product}")
#         id_ = product.id
#         product = await get_product(session=session, product_id=id_)
#         print(f"get: {product}")
#         products = await get_all_products(session=session)
#         print(f"get all: {products}")
#         await update_product(
#             session=session,
#             product=product,
#             product_update=ProductPartial(name="UpdatedTestProduct"),
#         )
#         product = await get_product(session=session, product_id=id_)
#         print(f"upd: {product}")
#         await delete_product(session=session, product=product)
#         product = await get_product(session=session, product_id=id_)
#         print(f"delete: {product}")
#
#
# if __name__ == "__main__":
#     asyncio.run(main())
