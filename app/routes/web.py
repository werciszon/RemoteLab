from pathlib import Path

from fastapi import APIRouter
from fastapi.responses import FileResponse




router = APIRouter(include_in_schema=False)
WEB_DIR = Path(__file__).resolve().parents[1] / "web"


@router.get("/")
def home() -> FileResponse:
    return FileResponse(WEB_DIR / "index.html")

@router.get("/calibration")
def calibration() -> FileResponse:
    return FileResponse(WEB_DIR / "calibration.html")

@router.get("/experiment")
def experiment() -> FileResponse:
    return FileResponse(WEB_DIR / "experiment.html")
