from fastapi import APIRouter
import httpx

router = APIRouter()

API_KEY = 'c8325111828b92605bd8c918d0d09525'
BASE_URL = 'https://api.openweathermap.org/data/2.5'


async def fetch_data(url: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.status_code, response.json()


@router.get("/all_statuses")
async def get_all_statuses(city: str = 'London', lat: float = 51.5074, lon: float = -0.1278):
    results = {}
    endpoints = {
        "weather": f"{BASE_URL}/weather?q={city}&appid={API_KEY}",
        "forecast": f"{BASE_URL}/forecast?q={city}&appid={API_KEY}",
        "onecall": f"{BASE_URL}/onecall?lat={lat}&lon={lon}&appid={API_KEY}"
    }
    async with httpx.AsyncClient() as client:
        for name, url in endpoints.items():
            status_code, data = await fetch_data(url)
            results[name] = {"status_code": status_code, "data": data}
    return results
