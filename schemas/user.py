from uuid import UUID

from pydantic import BaseModel, EmailStr, Field, constr


class UserRequest(BaseModel):
    email: EmailStr
    username: constr(min_length=5, max_length=24)
    password: constr(min_length=5, max_length=100)


class UserResponse(BaseModel):
    uuid: UUID
    username: str
    email: EmailStr

    class Config:
        orm_mode = True
