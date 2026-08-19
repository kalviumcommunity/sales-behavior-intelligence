"""
Sales representative routes.
"""
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from backend.auth.dependencies import get_current_manager
from backend.database import get_db
from backend.schemas.rep import RepCreate, RepResponse, RepUpdate
from backend.services.rep import RepService

router = APIRouter()


@router.post("/", response_model=RepResponse, status_code=status.HTTP_201_CREATED)
def create_rep(rep_in: RepCreate, db: Session = Depends(get_db), current_user=Depends(get_current_manager)):
    """Create a sales representative."""
    return RepResponse.model_validate(RepService(db).create_rep(rep_in))


@router.get("/", response_model=list[RepResponse])
def list_reps(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=100),
    db: Session = Depends(get_db),
    current_user=Depends(get_current_manager),
):
    """List sales representatives."""
    return [RepResponse.model_validate(rep) for rep in RepService(db).list_reps(skip=skip, limit=limit)]


@router.get("/{rep_id}", response_model=RepResponse)
def get_rep(rep_id: str, db: Session = Depends(get_db), current_user=Depends(get_current_manager)):
    """Get a sales representative."""
    rep = RepService(db).get_rep(rep_id)
    if not rep:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sales representative not found")
    return RepResponse.model_validate(rep)


@router.put("/{rep_id}", response_model=RepResponse)
def update_rep(rep_id: str, rep_in: RepUpdate, db: Session = Depends(get_db), current_user=Depends(get_current_manager)):
    """Update a sales representative."""
    rep = RepService(db).update_rep(rep_id, rep_in)
    if not rep:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sales representative not found")
    return RepResponse.model_validate(rep)


@router.delete("/{rep_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_rep(rep_id: str, db: Session = Depends(get_db), current_user=Depends(get_current_manager)):
    """Delete a sales representative."""
    if not RepService(db).delete_rep(rep_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sales representative not found")
