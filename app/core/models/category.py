from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models import Base
from core.models.mixins import IdIntPkMixin

if TYPE_CHECKING:
    from core.models import Product


class Category(Base, IdIntPkMixin):
    __tablename__ = "categories"

    name: Mapped[str] = mapped_column(String(50), unique=True)

    products: Mapped[list["Product"]] = relationship(
        "Product",
        back_populates="category",
    )

    def __str__(self):
        return f"Category: {self.name}"

    def __repr__(self):
        return f"Category: {self.name}"
