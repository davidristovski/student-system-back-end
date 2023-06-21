from errors.exceptions import validation_exception_handler
from routers.courses import router as courses_router
from routers.grade_cards import router as grade_cards_router
from routers.students import router as students_router
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError

app = FastAPI()
app.add_exception_handler(RequestValidationError, validation_exception_handler)

app.include_router(students_router)
app.include_router(courses_router)
app.include_router(grade_cards_router)
