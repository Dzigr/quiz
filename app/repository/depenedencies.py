from typing import Annotated

from fastapi import Depends

from app.db.models.question import Question
from app.repository.interfaces import AbstractRepository, SQLAlchemyRepository
from app.repository.service import QuestionService


class QuestionRepositoryModel(SQLAlchemyRepository):
    model = Question


def get_question_repo():
    return QuestionService(QuestionRepositoryModel)


QuestionRepository = Annotated[AbstractRepository, Depends(get_question_repo)]
