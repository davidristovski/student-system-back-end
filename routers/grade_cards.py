from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from persistence.database.session import get_db_session
from persistence.services import CourseService, StudentService, GradeCardService
from schemas.grade_card import GradeCardResponse, GradeCardRequest

router = APIRouter(prefix="/grade_cards", tags=["grade_cards"])


student_service = StudentService()
course_service = CourseService()
grade_card_service = GradeCardService()


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[GradeCardResponse])
def get_all_grade_cards(db: Session = Depends(get_db_session)):
    grade_cards = grade_card_service.get_all(db=db)
    return [
        GradeCardResponse(
            **{
                "uuid": grade_card.uuid,
                "course_name": grade_card.course.course_name,
                "student_name": f"{grade_card.student.first_name} {grade_card.student.last_name}",
                "grade": grade_card.grade,
            }
        )
        for grade_card in grade_cards
    ]


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=GradeCardResponse)
def create_grade_card(
    grade_card: GradeCardRequest, db: Session = Depends(get_db_session)
):
    db_student = student_service.get_by_uuid(db=db, uuid=grade_card.student_uuid)
    if not db_student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Student not found"
        )
    db_course = course_service.get_by_uuid(db=db, uuid=grade_card.course_uuid)
    if not db_course:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Course not found"
        )
    db_grade_card = grade_card_service.get_by_student_and_course_uuid(
        db=db, student_uuid=grade_card.student_uuid, course_uuid=grade_card.course_uuid
    )
    if db_grade_card:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="Grade card already exists"
        )
    db_grade_card = grade_card_service.create_record(db=db, record=grade_card)
    return GradeCardResponse(
        **{
            "uuid": db_grade_card.uuid,
            "course_name": db_grade_card.course.course_name,
            "student_name": f"{db_grade_card.student.first_name} {db_grade_card.student.last_name}",
            "grade": grade_card.grade,
        }
    )


@router.delete("/{grade_card_uuid}", status_code=status.HTTP_204_NO_CONTENT)
def delete_grade_card(grade_card_uuid: UUID, db: Session = Depends(get_db_session)):
    db_grade_card = grade_card_service.get_by_uuid(db=db, uuid=grade_card_uuid)
    if not db_grade_card:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Grade card does not exist in the system.",
        )
    return grade_card_service.delete_record(db=db, obj=db_grade_card)
