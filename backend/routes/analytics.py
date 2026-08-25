"""
Analytics routes for manager dashboard summaries.
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.auth.dependencies import get_current_manager
from backend.database import get_db
from backend.schemas.analytics import ManagerSummaryResponse
from backend.services.analytics import AnalyticsService

router = APIRouter()


@router.get("/manager-summary", response_model=ManagerSummaryResponse)
def get_manager_summary(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_manager),
):
    """Get aggregate metrics for the manager dashboard."""
    analytics_service = AnalyticsService(db)
    return analytics_service.get_manager_summary()
