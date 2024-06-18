from fastapi import APIRouter, HTTPException
import httpx


router = APIRouter()


API_KEY = 'c8325111828b92605bd8c918d0d09525'
BASE_URL = 'https://api.openweathermap.org/data/2.5'


async def fetch_data(url: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.status_code, response.json()


@router.get("/{city}")
async def get_forecast(city: str):
    url = f"{BASE_URL}/forecast?q={city}&appid={API_KEY}"
    status_code, data = await fetch_data(url)
    return {"status_code": status_code, "data": data}


@router.get("/status")
async def get_status():
    return {"status": "Forecast endpoint is working correctly"}
