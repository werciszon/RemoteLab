from fastapi import APIRouter

from fastapi import HTTPException
from app.database import check_database_connection


router = APIRouter()


@router.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}

@router.get("/db-check")
def db_check():
    try:
        result = check_database_connection()
        return {
            "database": "connected",
            "test_result": result[0],
        }
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Database connection failed",
        )