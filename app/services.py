from fastapi import HTTPException, status
from httpx import AsyncClient

EXTERNAL_API_URL = 'https://jservice.io/api/random?count={count}'


async def get_questions(count):
    url = EXTERNAL_API_URL.format(count=count)
    async with AsyncClient() as client:
        response = await client.get(url)

        if response.status_code == status.HTTP_200_OK:
            return response.json()

        raise HTTPException(
            status_code=response.status_code,
            detail="Failed to fetch data, check request",
        )
