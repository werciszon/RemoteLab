from typing import Any

from fastapi import APIRouter
from pydantic import BaseModel, ConfigDict, Field
from app.database import save_experiment, get_experiment
from fastapi import HTTPException

router = APIRouter(tags=["experiments"])


class ExperimentSubmission(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str = Field(min_length=1)
    config: dict[str, Any]


@router.post("/experiments")
def submit_experiment(experiment: ExperimentSubmission) -> dict[str, Any]:
    try:
        experiment_id = save_experiment(experiment.name, experiment.config)
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Failed to save experiment",
        )

    return {
        "status": "saved",
        "id": experiment_id,
    }

@router.get("/experiments")
def read_experiment() -> list[dict[str, Any]]:
    try:
        return get_experiment()
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Failed to read experiment",
        )