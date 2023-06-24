from typing import Optional

from sqlalchemy.orm import Session

from core.security import verify_password
from models.user import User as UserModel
from services.base import CRUDBase


class UserService(CRUDBase):
    def __init__(self):
        super().__init__(UserModel)

    def get_by_username(self, *, db: Session, username: str) -> Optional[UserModel]:
        return (
            db.query(self.model).filter(self.model.username == username).one_or_none()
        )

    def authenticate(
        self, *, db: Session, username: str, password: str
    ) -> Optional[UserModel]:
        db_user = self.get_by_username(db=db, username=username)
        if not db_user:
            return None
        if not verify_password(password=password, hashed_pass=db_user.password):
            return None
        return db_user
