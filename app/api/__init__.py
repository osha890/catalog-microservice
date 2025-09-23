from fastapi import APIRouter

from api.category.views import router as category_router
from api.product.views import router as product_router
from core.config import settings

router = APIRouter(
    prefix=settings.api.prefix,
)

router.include_router(category_router)
router.include_router(product_router)
