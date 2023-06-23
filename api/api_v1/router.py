from fastapi import APIRouter

from api.api_v1.handlers import course, grade_card, student, user
from api.auth.oauth2 import auth_router

router = APIRouter()

router.include_router(course.course_router, prefix="/courses", tags=["courses"])
router.include_router(student.student_router, prefix="/students", tags=["students"])
router.include_router(
    grade_card.grade_card_router, prefix="/grade_cards", tags=["grade_cards"]
)
router.include_router(user.user_router, prefix="/users", tags=["users"])
router.include_router(auth_router, prefix="/auth", tags=["auth"])
