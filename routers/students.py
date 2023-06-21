from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from persistence.database.session import get_db_session
from persistence.services import StudentService
from schemas.student import StudentRequest, StudentResponse

router = APIRouter(prefix="/students", tags=["students"])

student_service = StudentService()


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[StudentResponse])
def get_all_students(db: Session = Depends(get_db_session)):
    students = student_service.get_all(db=db)
    return students


@router.get(
    "/{student_uuid}", status_code=status.HTTP_200_OK, response_model=StudentResponse
)
def get_student(student_uuid: UUID, db: Session = Depends(get_db_session)):
    db_student = student_service.get_by_uuid(db=db, uuid=student_uuid)
    if not db_student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student does not exist in the system.",
        )
    return db_student


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=StudentResponse)
def create_student(student: StudentRequest, db: Session = Depends(get_db_session)):
    db_student = student_service.get_by_email(db=db, email=student.email)
    if db_student:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Student already exists in the system.",
        )
    return student_service.create_record(db=db, record=student)


@router.delete("/{student_uuid}", status_code=status.HTTP_204_NO_CONTENT)
def delete_student(student_uuid: UUID, db: Session = Depends(get_db_session)):
    db_student = student_service.get_by_uuid(db=db, uuid=student_uuid)
    if not db_student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student does not exist in the system.",
        )
    return student_service.delete_record(db=db, obj=db_student)
