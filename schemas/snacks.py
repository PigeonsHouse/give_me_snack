from datetime import datetime
from pydantic import BaseModel, Field

class Snack(BaseModel):
    snack_id: str
    name: str
    created_at: datetime = Field(default_factory=datetime.now())
    updated_at: datetime = Field(default_factory=datetime.now())

    class Config:
        orm_mode = True

