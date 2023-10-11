from fastapi import APIRouter, BackgroundTasks

from app.repository import QuestionRepository
from app.schemas.question import QuestionRequest, QuestionResponse

question_router = APIRouter(prefix="/questions", tags=["Questions"])


@question_router.post('/', response_model=QuestionResponse)
async def get_question(
        data: QuestionRequest,
        questions: QuestionRepository,
        background_tasks: BackgroundTasks,
):
    background_tasks.add_task(questions.add_records, data.questions_num)
    return await questions.get_last_record()
