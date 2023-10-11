from typing import Optional

from app.repository.interfaces import AbstractRepository
from app.schemas.question import QuestionResponse, QuestionSchemaAdd
from app.services import get_questions


class QuestionService:
    def __init__(self, repo_model: AbstractRepository):
        self.repo: AbstractRepository = repo_model()

    async def get_last_record(self) -> Optional[QuestionResponse]:
        return await self.repo.fetch_last()

    async def add_records(self, quantity: int) -> None:
        questions = await get_questions(quantity)
        for question in questions:
            existing_record = await self.repo.get_existing_record(question.get('id'))
            if existing_record is None:
                record = QuestionSchemaAdd(**question)
                await self.repo.add_record(record)

