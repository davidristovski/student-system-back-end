from enum import Enum
from uuid import UUID

from pydantic import BaseModel

MINIMUM_STUDENT_AGE = 10


class GradeEnum(str, Enum):
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    F = "F"


class GradeCardRequest(BaseModel):
    course_uuid: UUID
    student_uuid: UUID
    grade: GradeEnum


class GradeCardResponse(BaseModel):
    uuid: UUID
    course_name: str
    student_name: str
    grade: GradeEnum

    class Config:
        orm_mode = True
