from fastapi import APIRouter

from .question import question_router

v1 = APIRouter(prefix="/api/v1")
v1.include_router(question_router)


__all__ = ('v1', )
