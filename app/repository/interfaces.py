from abc import ABC, abstractmethod
from typing import Dict, Optional

from sqlalchemy import insert, select

from app.db.database import async_session_maker
from app.schemas.question import QuestionResponse, QuestionSchemaAdd


class AbstractRepository(ABC):
    @abstractmethod
    async def get_existing_record(self, record_id: int):
        raise NotImplementedError

    @abstractmethod
    async def add_record(self, data: dict):
        raise NotImplementedError

    @abstractmethod
    async def fetch_last(self):
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    async def get_existing_record(self, record_id: int) -> Optional[Dict]:
        async with async_session_maker() as session:
            stmt = select(self.model).where(self.model.id == record_id)
            result = await session.execute(stmt)
            return result.scalar_one_or_none()

    async def add_record(self, data: QuestionSchemaAdd) -> None:
        async with async_session_maker() as session:
            stmt = insert(self.model).values(dict(data))
            await session.execute(stmt)
            await session.commit()

    async def fetch_last(self) -> Optional[QuestionResponse]:
        async with async_session_maker() as session:
            stmt = select(self.model).order_by(self.model.added_at.desc()).limit(1)
            result = await session.execute(stmt)
            return result.scalar_one_or_none()
