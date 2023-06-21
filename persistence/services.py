from typing import List, Optional, Type, TypeVar
from uuid import UUID

from sqlalchemy.orm import Session

from persistence.models.course import Course as CourseModel
from persistence.models.grade_card import GradeCard as GradeCardModel
from persistence.models.student import Student as StudentModel

ModelType = TypeVar("ModelType")
CreateSchemaType = TypeVar("CreateSchemaType")


class CRUDBase:
    def __init__(self, model: Type[ModelType]):
        self.model = model

    def get_by_uuid(self, *, db: Session, uuid: UUID):
        return db.query(self.model).filter(self.model.uuid == uuid).one_or_none()

    def get_all(self, db: Session) -> Optional[List[Type[ModelType]]]:
        return db.query(self.model).all()

    def create_record(self, db: Session, record: CreateSchemaType) -> ModelType:
        db_obj = self.model(**record.dict())
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def delete_record(self, db: Session, obj: ModelType) -> None:
        db.delete(obj)
        db.commit()


class StudentService(CRUDBase):
    def __init__(self):
        self.model = StudentModel  # easier for autocomplete!
        super().__init__(self.model)

    def get_by_email(self, *, db: Session, email: str) -> Optional[StudentModel]:
        return db.query(self.model).filter(self.model.email == email).one_or_none()


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
