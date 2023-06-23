from fastapi_utils.guid_type import GUID, GUID_DEFAULT_SQLITE
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship

from database.base_class import Base


class Student(Base):
    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(GUID, primary_key=False, default=GUID_DEFAULT_SQLITE)
    first_name = Column(String(50), index=True, nullable=False)
    last_name = Column(String(50), index=True, nullable=False)
    date_of_birth = Column(Date, nullable=False)
    email = Column(String(50), unique=True, index=True, nullable=False)

    grade_cards = relationship(
        "GradeCard", cascade="all, delete-orphan", back_populates="student"
    )
