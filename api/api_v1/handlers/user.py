from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from api.deps.db import get_db_session
from api.deps.user import get_current_user
from core.security import hash_password
from models.user import User as UserModel
from schemas.user import UserRequest, UserResponse
from services.user import UserService

user_router = APIRouter()
user_service = UserService()


@user_router.get("/", status_code=status.HTTP_200_OK, dependencies=[Depends(get_current_user)], response_model=List[UserResponse])
def get_users(db: Session = Depends(get_db_session)):
    return user_service.get_all(db=db)


@user_router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserResponse)
def create_user(user: UserRequest, db: Session = Depends(get_db_session)):
    db_user = user_service.get_by_username(db=db, username=user.username)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="A user with this username already exist.",
        )
    user_record = UserRequest(
        **{
            "username": user.username,
            "password": hash_password(user.password),
        }
    )
    return user_service.create_record(db=db, record=user_record)
