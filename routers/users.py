from typing import List
from fastapi.exceptions import HTTPException
from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm.session import Session
from cruds.duties import add_duty_as_admin, add_duty_myself, delete_duty_by_duty_num, get_duties_list, swap_duties_by_order_number
from db.main import get_db
from schemas.main import DeleteDetailModel
from schemas.users import AuthInfo, PutDuties, SignInPayload, SignUpPayload, User as UserSchema
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

@user_router.post('/duties/{specified_user_id}', response_model=UserSchema)
async def add_duty(specified_user_id: str, db: Session = Depends(get_db), user_id: str = Depends(get_current_user)):
	duty = None
	if specified_user_id == user_id:
		duty = add_duty_myself(db, specified_user_id)
	else:
		duty = add_duty_as_admin(db, specified_user_id, user_id)
	return duty

@user_router.put('/duties', response_model=List[UserSchema], dependencies=[Depends(get_current_user)])
async def swap_duties(payload: PutDuties, db: Session = Depends(get_db)):
	duties_list = swap_duties_by_order_number(db, payload.source, payload.destination)
	return duties_list

@user_router.get('/duties', response_model=List[UserSchema])
async def response_duties_list(db: Session = Depends(get_db)):
	duties_list = get_duties_list(db)
	return duties_list

@user_router.delete('/duties/{duty_num}', response_model=DeleteDetailModel, dependencies=[Depends(get_current_user)])
async def delete_duty(duty_num: int, db: Session = Depends(get_db)):
	return delete_duty_by_duty_num(db, duty_num)
