from typing import Optional

from sqlalchemy.orm import Session

from models.student import Student as StudentModel
from services.base import CRUDBase


class StudentService(CRUDBase):
    def __init__(self):
        super().__init__(StudentModel)

    def get_by_email(self, *, db: Session, email: str) -> Optional[StudentModel]:
        return db.query(self.model).filter(self.model.email == email).one_or_none()
