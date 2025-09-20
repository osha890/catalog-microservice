from typing import TYPE_CHECKING

from sqlalchemy import String, Numeric, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models import Base
from core.models.mixins import IdIntPkMixin

from decimal import Decimal

if TYPE_CHECKING:
    from core.models import Category


class Product(Base, IdIntPkMixin):
    name: Mapped[str] = mapped_column(String(50), unique=True)
    description: Mapped[str | None] = mapped_column(Text)
    price: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    category_id: Mapped[int] = mapped_column(
        ForeignKey("categories.id", ondelete="RESTRICT"),
    )

    category: Mapped["Category"] = relationship(
        "Category",
        back_populates="products",
    )

    def __str__(self):
        return f"Product: {self.name}"

    def __repr__(self):
        return f"Product: {self.name}"
