from fastapi import FastAPI
from api import weather, forecast, onecall
from error import router as error_router
from all_statuses import router as all_statuses

app = FastAPI()

app.include_router(
    weather.router,
    prefix="/weather",
    tags=["Weather"]
)
app.include_router(
    forecast.router,
    prefix="/forecast",
    tags=["Forecast"]
)
app.include_router(
    onecall.router,
    prefix="/onecall",
    tags=["OneCall"]
)
app.include_router(
    error_router,
    prefix="/error",
    tags=["Error"]
)
app.include_router(
    all_statuses,
    prefix="/test_status",
    tags=["All statuses"]
)
