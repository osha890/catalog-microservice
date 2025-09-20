from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from core.models import Base
from core.models.mixins import IdIntPkMixin


class Category(Base, IdIntPkMixin):
    __tablename__ = "categories"

    name: Mapped[str] = mapped_column(String(50))
