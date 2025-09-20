import asyncio
from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from api.category.schemas import CategoryCreate, CategoryPartial
from core.db_helper import db_helper
from core.models import Category


async def create_category(
    session: AsyncSession,
    category_create: CategoryCreate,
) -> Category:
    category = Category(**category_create.model_dump())
    session.add(category)
    await session.commit()
    await session.refresh(category)
    return category


async def get_all_categories(
    session: AsyncSession,
) -> Sequence[Category]:
    stmt = select(Category).order_by(Category.id)
    result = await session.scalars(stmt)
    return result.all()


async def get_category(
    session: AsyncSession,
    category_id: int,
) -> Category | None:
    return await session.get(Category, category_id)


async def update_category(
    session: AsyncSession,
    category: Category,
    category_update: CategoryPartial,
) -> Category:
    for name, value in category_update.model_dump(exclude_unset=True).items():
        setattr(category, name, value)
    await session.commit()
    return category


async def delete_category(
    session: AsyncSession,
    category: Category,
) -> None:
    await session.delete(category)
    await session.commit()


# async def main():
#     async with db_helper.session_factory() as session:
#         category = await create_category(session, CategoryCreate(name="Test"))
#         print(f"create: {category}")
#         id_ = category.id
#         category = await get_category(session=session, category_id=id_)
#         print(f"get: {category}")
#         categories = await get_all_categories(session=session)
#         print(f"get all: {categories}")
#         await update_category(
#             session=session,
#             category=category,
#             category_update=CategoryPartial(name="UpdatedTest"),
#         )
#         category = await get_category(session=session, category_id=id_)
#         print(f"upd: {category}")
#         await delete_category(session=session, category=category)
#         category = await get_category(session=session, category_id=id_)
#         print(f"delete: {category}")
#
#
# if __name__ == "__main__":
#     asyncio.run(main())
