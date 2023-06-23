from fastapi_utils.guid_type import GUID, GUID_DEFAULT_SQLITE
from sqlalchemy import Column, Integer, String

from database.base_class import Base


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(GUID, primary_key=False, default=GUID_DEFAULT_SQLITE)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(50), unique=True, index=True, nullable=False)
    password = Column(String(128))
