from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from api.deps.db import get_db_session
from api.deps.user import get_current_user
from core.security import create_access_token, create_refresh_token
from schemas.auth import TokenSchema
from schemas.user import UserRequest, UserResponse
from services.user import UserService

auth_router = APIRouter()
user_service = UserService()


@auth_router.post(
    "/login", status_code=status.HTTP_201_CREATED, response_model=TokenSchema
)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db_session),
):
    user = user_service.authenticate(
        db=db, username=form_data.username, password=form_data.password
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
        )

    return {
        "access_token": create_access_token(user.uuid),
        "refresh_token": create_refresh_token(user.uuid),
    }


@auth_router.post(
    "/check-token", status_code=status.HTTP_201_CREATED, response_model=UserResponse
)
def test_token(user: UserRequest = Depends(get_current_user)):
    return user
