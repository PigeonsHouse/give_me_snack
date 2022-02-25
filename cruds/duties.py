from typing import List
from fastapi.exceptions import HTTPException
from sqlalchemy.orm.session import Session
from cruds.users import get_user_by_id
from db.schema import Duty, User
from schemas.main import DeleteDetailModel
from schemas.users import User as UserSchema

def add_duty_as_admin(db: Session, user_id: str, admin_user_id: str) -> UserSchema:
	duty_orm = db.query(Duty).get(admin_user_id)
	if duty_orm is None:
		raise HTTPException(status_code=403, detail='permission denied')
	return add_duty_myself(db, user_id)

def add_duty_myself(db: Session, user_id: str) -> UserSchema:
	user_orm = db.query(User).get(user_id)
	if user_orm is None:
		raise HTTPException(status_code=400, detail='user is not found')
	duty_orm = db.query(Duty).get(user_id)
	if duty_orm is not None:
		raise HTTPException(status_code=400, detail='you are already exist')
	duties_count = db.query(Duty).count()
	order = duties_count + 1
	new_duty_orm = Duty(
		user_id = user_id,
		order = order
	)
	db.add(new_duty_orm)
	db.commit()
	user = UserSchema.from_orm(user_orm)
	user.order = order
	return user

def swap_duties_by_order_number(db: Session, src: int, dest: int) -> List[UserSchema]:
	src_duty_orm = db.query(Duty).filter(Duty.order == src).first()
	dest_duty_orm = db.query(Duty).filter(Duty.order == dest).first()
	if src_duty_orm is None or dest_duty_orm is None:
		raise HTTPException(status_code=400, detail='duty is not found')
	src_duty_orm.order = dest
	dest_duty_orm.order = src
	db.commit()
	return get_duties_list(db)

def get_duties_list(db: Session) -> List[UserSchema]:
	duties_orm_list = db.query(Duty).order_by(Duty.order).all()
	duty_users_list = []
	for duty_orm in duties_orm_list:
		user = get_user_by_id(db, duty_orm.user_id)
		duty_users_list.append(user)
	return duty_users_list

def delete_duty_by_duty_num(db: Session, duty_num: int) -> DeleteDetailModel:
	duty_orm = db.query(Duty).filter(Duty.order == duty_num).first()
	if duty_orm is None:
		raise HTTPException(status_code=400, detail='duty is not found')
	db.delete(duty_orm)
	duty_orms = db.query(Duty).filter(Duty.order > duty_num).all()
	for duty_orm in duty_orms:
		duty_orm.order -= 1
	db.commit()
	return {'detail': 'OK'}
