from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, PositiveInt

class SignUpPayload(BaseModel):
    name: str
    password: str

class SignInPayload(BaseModel):
    name: str
    password: str

class User(BaseModel):
    user_id: str
    name: str
    order: Optional[int] = Field(default=None)
    created_at: datetime = Field(default_factory=datetime.now())

    class Config:
        orm_mode = True

class AuthInfo(BaseModel):
    jwt: str

class PutDuties(BaseModel):
    source: PositiveInt
    destination: PositiveInt
