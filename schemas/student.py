from datetime import date
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, validator

MINIMUM_STUDENT_AGE = 10


class StudentRequest(BaseModel):
    first_name: str
    last_name: str
    date_of_birth: date  # ISO 8601 format
    email: str

    @validator("date_of_birth")
    def is_ten_years_or_older(cls, date_of_birth: date) -> Optional[date]:
        age_difference = date.today().year - date_of_birth.year
        if age_difference < MINIMUM_STUDENT_AGE:
            raise ValueError("Student must be at least 10 years old.")
        return date_of_birth


class StudentResponse(BaseModel):
    uuid: UUID
    first_name: str
    last_name: str
    date_of_birth: date
    email: str

    class Config:
        orm_mode = True
