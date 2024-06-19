from fastapi import APIRouter, HTTPException
from httpx import AsyncClient
from app.config import API_KEY

router = APIRouter(
    prefix="/api",
    tags=["HTTP Code Test with Weather API"]
)


@router.get(
    "/weather/{city}",
    summary="Get weather by city",
    description="Получить информацию о погоде в указанном городе "
                "с использованием OpenWeatherMap API"
)
async def get_weather(
        city: str
):
    """
    Получить погоду для указанного города.

    :param city:
        Название города для получения информации о погоде.
    :return:
        JSON с данными о погоде или ошибка с соответствующим статусом HTTP.
    """
    url = (f"https://api.openweathermap.org/data/2.5/weather?q="
           f"{city}"
           f"&appid={API_KEY}")

    async with AsyncClient() as client:
        response = await client.get(url)

    if response.status_code == 200:
        return response.json()
    elif response.status_code == 201:
        raise HTTPException(
            status_code=201,
            detail="Created"
        )
    elif response.status_code == 202:
        raise HTTPException(
            status_code=202,
            detail="Accepted"
        )
    elif response.status_code == 204:
        raise HTTPException(
            status_code=204,
            detail="No Content"
        )
    elif response.status_code == 400:
        raise HTTPException(
            status_code=400,
            detail="Bad Request"
        )
    elif response.status_code == 401:
        raise HTTPException(
            status_code=401,
            detail="Invalid API key"
        )
    elif response.status_code == 403:
        raise HTTPException(
            status_code=403,
            detail="Forbidden"
        )
    elif response.status_code == 404:
        raise HTTPException(
            status_code=404,
            detail="City not found"
        )
    elif response.status_code == 429:
        raise HTTPException(
            status_code=429,
            detail="Too many requests"
        )
    elif response.status_code == 500:
        raise HTTPException(
            status_code=500,
            detail="Internal Server Error"
        )
    elif response.status_code == 502:
        raise HTTPException(
            status_code=502,
            detail="Bad Gateway"
        )
    elif response.status_code == 503:
        raise HTTPException(
            status_code=503,
            detail="Service Unavailable"
        )
    elif response.status_code == 504:
        raise HTTPException(
            status_code=504,
            detail="Gateway Timeout"
        )
    else:
        raise HTTPException(
            status_code=response.status_code,
            detail="An error occurred"
        )


@router.get(
    "/status/{status_code}",
    summary="Get custom status code",
    description="Получить ответ с указанным статусом HTTP"
)
async def get_status(
        status_code: int
):
    """
    Получить ответ с указанным статусом HTTP.

    :param status_code:
        Код статуса HTTP для генерации ответа.
    :return:
        Сообщение с указанным статусом HTTP или ошибка с соответствующим
        статусом HTTP.
    """
    if 100 <= status_code < 200:
        return {
            "message": f"Informational response with status code {status_code}"
        }
    elif 200 <= status_code < 300:
        return {
            "message": f"Success response with status code {status_code}"
        }
    elif 300 <= status_code < 400:
        return {
            "message": f"Redirection response with status code {status_code}"
        }
    elif 400 <= status_code < 500:
        return {
            "message": f"Client error with status code {status_code}"
        }
    elif 500 <= status_code < 600:
        return {
            "message": f"Server error with status code {status_code}"
        }
    else:
        raise HTTPException(
            status_code=400,
            detail="Invalid status code"
        )
