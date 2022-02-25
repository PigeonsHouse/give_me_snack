from fastapi import APIRouter, Depends
from pytest import Session
from db.main import get_db

snack_router = APIRouter()

@snack_router.get('/purchased')
async def get_purchased_snack(db: Session = Depends(get_db)):
    pass
