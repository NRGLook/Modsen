from fastapi import FastAPI
from app.api import router

app = FastAPI(
    title="Weather API",
    description="API для получения HTTP статусов "
                "с использованием OpenWeatherMap API",
    version="0.0.1",
)

app.include_router(router)
