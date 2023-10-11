from datetime import datetime

from pydantic import BaseModel, Field, model_validator


class QuestionSchemaAdd(BaseModel):
    id: int
    question: str
    answer: str
    created_at: datetime

    class Config:
        from_attributes = True

    @model_validator(mode='before')
    def parse_created_at(cls, values):
        values['created_at'] = datetime.fromisoformat(values['created_at'])
        return values


class QuestionRequest(BaseModel):
    questions_num: int


class QuestionResponse(BaseModel):
    question: str = Field(default=None)
    answer: str = Field(default=None)
    created_at: datetime = Field(default=None)
