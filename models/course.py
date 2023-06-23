from fastapi_utils.guid_type import GUID, GUID_DEFAULT_SQLITE
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database.base_class import Base


class Course(Base):
    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(GUID, primary_key=False, default=GUID_DEFAULT_SQLITE)
    course_name = Column(String(100), index=True, nullable=False)

    grade_cards = relationship(
        "GradeCard", cascade="all, delete-orphan", back_populates="course"
    )
