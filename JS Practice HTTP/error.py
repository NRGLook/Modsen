from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.get("/{code}")
async def get_error(code: int):
    raise HTTPException(
        status_code=code,
        detail=f"This is a test error with code {code}"
    )
