from fastapi import Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


def validation_exception_handler(request: Request, exc: RequestValidationError):
    error_messages = []
    for error in exc.errors():
        field_name = ".".join(error["loc"])
        error_message = error["msg"]
        error_type = error["type"]
        error_info = {"field": field_name, "message": error_message, "type": error_type}
        error_messages.append(error_info)

    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"errors": error_messages},
    )
