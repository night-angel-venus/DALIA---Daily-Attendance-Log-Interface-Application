from sqlalchemy import Column, Integer, String, Enum
from database import Base
from sqlalchemy.orm import relationship
import enum


class UserRoleEnum(enum.Enum):
    USER = "User"
    ADMIN = "Admin"

class User(Base):
    __tablename__ = "users"

    # COLUMNS
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    password_hash = Column(String(50), nullable=False)
    role =Column(Enum(UserRoleEnum), default=UserRoleEnum.USER)


    dtr_records = relationship("DTR", back_populates="user")