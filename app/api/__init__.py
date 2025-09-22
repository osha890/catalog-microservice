from fastapi import APIRouter

from api.category.views import router as category_router
from core.config import settings

router = APIRouter(
    prefix=settings.api.prefix,
)

router.include_router(category_router)
