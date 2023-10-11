from fastapi import FastAPI
from fastapi.exceptions import ResponseValidationError

from app.exceptions import response_validation_exception_handler
from app.routers import v1

app = FastAPI(title='Quiz')

app.include_router(v1)

app.add_exception_handler(
    ResponseValidationError,
    response_validation_exception_handler,
)

origins = ["*"]


@app.get("/api/ping/")
async def ping():
    return "pong"
