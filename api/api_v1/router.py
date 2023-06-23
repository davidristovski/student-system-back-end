from fastapi import APIRouter
from api.api_v1.handlers import courses
from api.api_v1.handlers import students
from api.api_v1.handlers import grade_cards

router = APIRouter()

router.include_router(courses.course_router, prefix="/courses", tags=["courses"])
router.include_router(students.student_router, prefix="/students", tags=["students"])
router.include_router(grade_cards.grade_card_router, prefix="/grade_cards", tags=["grade_cards"])
