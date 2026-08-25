"""
Activity routes.
"""
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from backend.auth.dependencies import get_current_user
from backend.database import get_db
from backend.schemas.activity import (ActivityCreate, ActivityResponse,
                                      ActivityUpdate)
from backend.services.activity import ActivityService

router = APIRouter()


@router.post("/", response_model=ActivityResponse, status_code=status.HTTP_201_CREATED)
def create_activity(activity_in: ActivityCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    """Create an activity."""
    try:
        return ActivityResponse.model_validate(ActivityService(db).create_activity(activity_in))
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc


@router.get("/", response_model=list[ActivityResponse])
def list_activities(skip: int = Query(0, ge=0), limit: int = Query(100, ge=1, le=100), db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    """List activities."""
    return [ActivityResponse.model_validate(activity) for activity in ActivityService(db).list_activities(skip, limit)]


@router.get("/deal/{deal_id}", response_model=list[ActivityResponse])
def get_activities_by_deal(deal_id: str, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    """Get activities for a deal."""
    return [ActivityResponse.model_validate(activity) for activity in ActivityService(db).get_activities_by_deal(deal_id)]


@router.get("/{activity_id}", response_model=ActivityResponse)
def get_activity(activity_id: str, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    """Get an activity."""
    activity = ActivityService(db).get_activity(activity_id)
    if not activity:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Activity not found")
    return ActivityResponse.model_validate(activity)


@router.put("/{activity_id}", response_model=ActivityResponse)
def update_activity(activity_id: str, activity_in: ActivityUpdate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    """Update an activity."""
    activity = ActivityService(db).update_activity(activity_id, activity_in)
    if not activity:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Activity not found")
    return ActivityResponse.model_validate(activity)


@router.delete("/{activity_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_activity(activity_id: str, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    """Delete an activity."""
    if not ActivityService(db).delete_activity(activity_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Activity not found")
