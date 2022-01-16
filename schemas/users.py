from datetime import datetime
from pydantic import BaseModel, Field

class SignUpPayload(BaseModel):
    name: str
    password: str

class SignInPayload(BaseModel):
    name: str
    password: str

class User(BaseModel):
    user_id: str
    name: str
    created_at: datetime = Field(default_factory=datetime.now())
    updated_at: datetime = Field(default_factory=datetime.now())

    class Config:
        orm_mode = True

class AuthInfo(BaseModel):
    jwt: str
