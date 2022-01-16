from fastapi import APIRouter
from .users import user_router
from .snacks import snack_router

router = APIRouter()

router.include_router(user_router, prefix='/users', tags=['users'])
router.include_router(snack_router, prefix='/snacks', tags=['snacks'])
