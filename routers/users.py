from fastapi.exceptions import HTTPException
from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm.session import Session
from db.main import get_db
from schemas.main import DeleteDetailModel
from schemas.users import AuthInfo, SignInPayload, SignUpPayload, User as UserSchema
from cruds.users import create_user, delete_user_by_id, get_user_by_id
from utils import generate_token, get_current_user

user_router = APIRouter()

@user_router.post('/signup', response_model=UserSchema)
async def signup(payload: SignUpPayload, db: Session = Depends(get_db)):
  user = create_user(db, payload.name, payload.password)
  return user

@user_router.post('/signin', response_model=AuthInfo)
async def signin(payload: SignInPayload, db: Session = Depends(get_db)):
  auth_info = { 'jwt': generate_token(db, payload.name, payload.password) }
  return auth_info

@user_router.get('/me', response_model=UserSchema)
async def get_me(db: Session = Depends(get_db), user_id: str = Depends(get_current_user)):
  if user_id is None:
    raise HTTPException(status_code=403, detail="jwt_token is invarid")
  user = get_user_by_id(db, user_id)
  return user

@user_router.delete('', response_model=DeleteDetailModel)
async def delete_user(db: Session = Depends(get_db), user_id: str = Depends(get_current_user)):
  if user_id is None:
    raise HTTPException(status_code=403, detail="jwt_token is invarid")
  delete_user_by_id(db, user_id)
  return {'detail': 'OK'}
