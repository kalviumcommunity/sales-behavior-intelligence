"""
Deal routes for opportunity management.
"""

from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from backend.auth.dependencies import get_current_user
from backend.database import get_db
from backend.schemas.deal import DealCreate, DealListResponse, DealResponse, DealUpdate
from backend.services.deal import DealService

router = APIRouter()


@router.post("/", response_model=DealResponse, status_code=status.HTTP_201_CREATED)
def create_deal(
    deal_in: DealCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    """Create a deal."""
    try:
        return DealResponse.model_validate(DealService(db).create_deal(deal_in))
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)
        ) from exc


@router.get("/", response_model=DealListResponse)
def list_deals(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=100),
    rep_id: Optional[str] = Query(None),
    risk_level: Optional[str] = Query(None),
    stage: Optional[str] = Query(None),
    search: Optional[str] = Query(None),
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    """List deals."""
    return DealService(db).list_deals(skip, limit, rep_id, risk_level, stage, search)


@router.get("/{deal_id}", response_model=DealResponse)
def get_deal(
    deal_id: str, db: Session = Depends(get_db), current_user=Depends(get_current_user)
):
    """Get a deal."""
    deal = DealService(db).get_deal(deal_id)
    if not deal:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Deal not found"
        )
    return DealResponse.model_validate(deal)


@router.put("/{deal_id}", response_model=DealResponse)
def update_deal(
    deal_id: str,
    deal_in: DealUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    """Update a deal."""
    try:
        deal = DealService(db).update_deal(deal_id, deal_in)
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)
        ) from exc
    if not deal:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Deal not found"
        )
    return DealResponse.model_validate(deal)


@router.delete("/{deal_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_deal(
    deal_id: str, db: Session = Depends(get_db), current_user=Depends(get_current_user)
):
    """Delete a deal."""
    if not DealService(db).delete_deal(deal_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Deal not found"
        )
