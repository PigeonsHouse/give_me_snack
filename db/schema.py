from typing import Any
from sqlalchemy import Column
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import String, DateTime, Integer
from sqlalchemy.sql.functions import func
from uuid import uuid4

@as_declarative()
class Base:
  id: Any
  __name__: Any

  @declared_attr
  def __tablename__(self) -> str:
    return self.__name__.lower()

def generate_uuid():
    return str(uuid4())

class User(Base):
    __tablename__ = 'users'
    user_id = Column(String, primary_key=True, default=generate_uuid)
    name = Column(String, unique=True)
    password_hash = Column(String, nullable=True)
    created_at = Column(DateTime, default=func.now())

class Duty(Base):
    __tablename__ = 'duty'
    user_id = Column(String, ForeignKey('users.user_id'), primary_key=True)
    order = Column(Integer)
    created_at = Column(DateTime, default=func.now())

class Snack(Base):
    __tablename__ = 'snacks'
    snack_id = Column(String, primary_key=True, default=generate_uuid)
    name = Column(String)
    created_at = Column(DateTime, default=func.now())

    evaluations = relationship('Evaluation')

class SuggestedSnack(Base):
    __tablename__ = 'suggested_snacks'
    snack_id = Column(String, ForeignKey('snacks.snack_id'), primary_key=True)
    created_at = Column(DateTime, default=func.now())

    favorites = relationship('Favorite')

class PurchasedSnack(Base):
    __tablename__ = 'purchased_snacks'
    snack_id = Column(String, ForeignKey('snacks.snack_id'), primary_key=True)
    created_at = Column(DateTime, default=func.now())

class Evaluation(Base):
    __tablename__ = 'evaluations'
    user_id = Column(String, ForeignKey('users.user_id'), primary_key=True)
    snack_id = Column(String, ForeignKey('snacks.snack_id'), primary_key=True)
    point = Column(Integer)
    created_at = Column(DateTime, default=func.now())

class Favorite(Base):
    __tablename__ = 'favorites'
    user_id = Column(String, ForeignKey('users.user_id'), primary_key=True)
    snack_id = Column(String, ForeignKey('suggested_snacks.snack_id'), primary_key=True)
    created_at = Column(DateTime, default=func.now())
