from sqlalchemy import Column, Integer, String, Enum, Date, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime
import enum


class ShiftTypeEnum(enum.Enum):
    FULL_DAY = "Full Day (8 Hours)"
    HALF_DAY = "Half Day (4 Hours)"

class DTR(Base):
    __tablename__ = "dtr"

    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    shift_type = Column(Enum(ShiftTypeEnum), nullable=False)
    time_in = Column(DateTime, default=datetime.now, nullable=False)
    estimated_time_out = Column(DateTime, nullable=False)
    time_out = Column(DateTime, nullable=True)


    user = relationship("User", back_populates="dtr_records")

    __table_args__ = (
        UniqueConstraint(
            "user_id",
            "date",
            name="user_id_constraint",
        ),
    )


# RELATIONSHIP