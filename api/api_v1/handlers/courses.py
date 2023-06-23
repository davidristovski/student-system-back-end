from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from api.deps.db import get_db_session
from services.course import CourseService
from schemas.course import CourseRequest, CourseResponse

course_router = APIRouter()
course_service = CourseService()


@course_router.get("/", status_code=status.HTTP_200_OK, response_model=List[CourseResponse])
def get_all_courses(db: Session = Depends(get_db_session)):
    courses = course_service.get_all(db=db)
    return courses


@course_router.post("/", status_code=status.HTTP_201_CREATED, response_model=CourseResponse)
def create_course(course: CourseRequest, db: Session = Depends(get_db_session)):
    db_course = course_service.get_by_name(db=db, course_name=course.course_name)
    if db_course:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Course already exists in the system.",
        )
    return course_service.create_record(db=db, record=course)


@course_router.delete("/{course_uuid}", status_code=status.HTTP_204_NO_CONTENT)
def delete_course(course_uuid: UUID, db: Session = Depends(get_db_session)):
    db_course = course_service.get_by_uuid(db=db, uuid=course_uuid)
    if not db_course:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Course does not exist in the system.",
        )
    return course_service.delete_record(db=db, obj=db_course)
