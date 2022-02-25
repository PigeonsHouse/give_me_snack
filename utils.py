from typing import Optional
import jwt
from fastapi import HTTPException, Header
from sqlalchemy.orm.session import Session
from cruds.users import gen_password_hash, get_user_by_name
from db.schema import User
from schemas.users import User as UserSchema
from datetime import datetime, timedelta
import os

SECRET = os.environ.get('SECRET', 'jwt_secret')

BASE_TEMPARETURE = 25

SCORE_TEMPARETURE_LIST = [7, 31, 61, 193, 521]

def generate_token(db: Session, name: str, password: str) -> str:
	user: User = get_user_by_name(db, name)
	password_hash = gen_password_hash(password)
	if user.password_hash != password_hash:
		raise HTTPException(status_code=401, detail='authentication failed')

	exp_datetime = datetime.now() + timedelta(10)

	jwt_payload = {
		'exp': exp_datetime.timestamp(),
		'user_id': user.user_id
	}

	encoded_jwt = jwt.encode(jwt_payload, SECRET, algorithm='HS256')

	return encoded_jwt

def decode_token(token: str) -> UserSchema:
	user_dict = jwt.decode(token, SECRET, algorithms=['HS256'])
	user_id = user_dict['user_id']
	return user_id

def get_current_user(jwt_token: str = Header(None)) -> Optional[str]:
	print('authorization: ', jwt_token)
	if jwt_token.find("Bearer ") != 0:
		raise HTTPException(status_code=400, detail="jwt_token is invarid")
	try:
		token = jwt_token.split(' ')[1]
		user_id = decode_token(token)
		return user_id
	except:
		return None
