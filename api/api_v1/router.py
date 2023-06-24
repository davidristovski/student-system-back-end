from fastapi import APIRouter, Depends

from api.api_v1.handlers import course, grade_card, student, user
from api.api_v1.handlers.auth import auth_router
from api.deps.user import get_current_user

router = APIRouter()

router.include_router(
    course.course_router,
    prefix="/courses",
    dependencies=[Depends(get_current_user)],
    tags=["courses"],
)
router.include_router(
    student.student_router,
    prefix="/students",
    dependencies=[Depends(get_current_user)],
    tags=["students"],
)
router.include_router(
    grade_card.grade_card_router,
    prefix="/grade_cards",
    dependencies=[Depends(get_current_user)],
    tags=["grade_cards"],
)
router.include_router(user.user_router, prefix="/users", tags=["users"])
router.include_router(auth_router, prefix="/auth", tags=["auth"])
