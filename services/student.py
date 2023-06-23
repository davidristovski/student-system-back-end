from models.student import Student as StudentModel
from services.base import CRUDBase


class StudentService(CRUDBase):
    def __init__(self):
        self.model = StudentModel  # easier for autocomplete!
        super().__init__(self.model)
