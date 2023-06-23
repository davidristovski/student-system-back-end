from typing import List, Optional, Type, TypeVar
from uuid import UUID

from sqlalchemy.orm import Session

ModelType = TypeVar("ModelType")
CreateSchemaType = TypeVar("CreateSchemaType")


class CRUDBase:
    def __init__(self, model: Type[ModelType]):
        self.model = model

    def get_by_id(self, *, db: Session, user_id: int) -> Optional[ModelType]:
        return db.query(self.model).filter(self.model.id == user_id).one_or_none()

    def get_by_uuid(self, *, db: Session, uuid: UUID):
        return db.query(self.model).filter(self.model.uuid == uuid).one_or_none()

    def get_by_email(self, *, db: Session, email: str) -> Optional[ModelType]:
        return db.query(self.model).filter(self.model.email == email).one_or_none()

    def get_all(self, *, db: Session) -> Optional[List[Type[ModelType]]]:
        return db.query(self.model).all()

    def create_record(self, *, db: Session, record: CreateSchemaType) -> ModelType:
        db_obj = self.model(**record.dict())
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def delete_record(self, *, db: Session, obj: ModelType) -> None:
        db.delete(obj)
        db.commit()
