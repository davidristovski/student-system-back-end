from fastapi_utils.guid_type import GUID, GUID_DEFAULT_SQLITE
from sqlalchemy import Column, Integer, ForeignKey, Enum
from sqlalchemy.orm import relationship

from database.base_class import Base


class GradeCard(Base):
    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(GUID, primary_key=False, default=GUID_DEFAULT_SQLITE)
    course_uuid = Column(GUID, ForeignKey("course.uuid"))
    student_uuid = Column(GUID, ForeignKey("student.uuid"))
    grade = Column(Enum("A", "B", "C", "D", "F"), nullable=False)

    student = relationship("Student", back_populates="grade_cards")
    course = relationship("Course", back_populates="grade_cards")
