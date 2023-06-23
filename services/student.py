from services.base import CRUDBase
from models.student import Student as StudentModel
from sqlalchemy.orm import Session
from typing import Optional


class StudentService(CRUDBase):
    def __init__(self):
        self.model = StudentModel  # easier for autocomplete!
        super().__init__(self.model)

    def get_by_email(self, *, db: Session, email: str) -> Optional[StudentModel]:
        return db.query(self.model).filter(self.model.email == email).one_or_none()
