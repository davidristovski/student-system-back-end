from uuid import UUID

from pydantic import BaseModel


class CourseRequest(BaseModel):
    course_name: str


class CourseResponse(BaseModel):
    uuid: UUID
    course_name: str

    class Config:
        orm_mode = True
