from typing import Optional
from uuid import UUID

from sqlalchemy.orm import Session

from models.grade_card import GradeCard as GradeCardModel
from services.base import CRUDBase


class GradeCardService(CRUDBase):
    def __init__(self):
        self.model = GradeCardModel
        super().__init__(self.model)

    def get_by_student_and_course_uuid(
        self, *, db: Session, student_uuid: UUID, course_uuid: UUID
    ) -> Optional[GradeCardModel]:
        return (
            db.query(self.model)
            .filter(
                self.model.student_uuid == student_uuid,
                self.model.course_uuid == course_uuid,
            )
            .one_or_none()
        )
