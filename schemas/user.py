from uuid import UUID

from pydantic import BaseModel, constr


class UserRequest(BaseModel):
    username: constr(min_length=5, max_length=24)
    password: constr(min_length=5, max_length=100)


class UserResponse(BaseModel):
    uuid: UUID
    username: str

    class Config:
        orm_mode = True
