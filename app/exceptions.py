from fastapi import status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse


async def response_validation_exception_handler(request, exc):
    message = f"Data from database equal to: {exc.body}"

    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"error": message}),
    )