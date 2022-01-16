from pydantic import BaseModel

class DeleteDetailModel(BaseModel):
    detail: str
