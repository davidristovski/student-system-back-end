from typing import Optional

from sqlalchemy.orm import Session

from models.course import Course as CourseModel
from services.base import CRUDBase


class CourseService(CRUDBase):
    def __init__(self):
        self.model = CourseModel
        super().__init__(self.model)

    def get_by_name(self, *, db: Session, course_name: str) -> Optional[CourseModel]:
        return (
            db.query(self.model)
            .filter(self.model.course_name.like(f"%{course_name}%"))
            .one_or_none()
        )
