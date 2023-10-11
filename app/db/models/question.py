from sqlalchemy import TIMESTAMP, Column, Integer, String, func

from app.db.database import Base


class Question(Base):
    __tablename__ = "questions"

    id: int = Column(Integer, primary_key=True)
    question: str = Column(String(512))
    answer: str = Column(String(256))
    created_at: str = Column(TIMESTAMP(timezone=True))
    added_at: str = Column(TIMESTAMP(timezone=True), default=func.now())
