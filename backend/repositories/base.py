"""
Base repository with common CRUD operations.
"""
from typing import Generic, List, Optional, Type, TypeVar
from uuid import uuid4

from sqlalchemy.orm import Session

from backend.database import Base

ModelType = TypeVar("ModelType", bound=Base)


class BaseRepository(Generic[ModelType]):
    """Base repository with generic CRUD operations."""

    def __init__(self, model: Type[ModelType], db: Session):
        self.model = model
        self.db = db

    def get(self, id: str) -> Optional[ModelType]:
        """Get a single record by ID."""
        return self.db.query(self.model).filter(self.model.id == id).first()

    def get_multi(
        self,
        skip: int = 0,
        limit: int = 100,
        filters: Optional[dict] = None,
    ) -> List[ModelType]:
        """Get multiple records with pagination and optional filters."""
        query = self.db.query(self.model)
        if filters:
            for key, value in filters.items():
                if hasattr(self.model, key):
                    query = query.filter(getattr(self.model, key) == value)
        return query.offset(skip).limit(limit).all()

    def create(self, obj_in: dict) -> ModelType:
        """Create a new record."""
        if hasattr(self.model, "id") and not obj_in.get("id"):
            obj_in["id"] = uuid4().hex
        db_obj = self.model(**obj_in)
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update(self, db_obj_or_id, obj_in: dict) -> Optional[ModelType]:
        """Update an existing record by object or ID."""
        db_obj = self.get(db_obj_or_id) if isinstance(db_obj_or_id, str) else db_obj_or_id
        if not db_obj:
            return None
        for field, value in obj_in.items():
            if hasattr(db_obj, field):
                setattr(db_obj, field, value)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete(self, id: str) -> Optional[ModelType]:
        """Delete a record by ID."""
        obj = self.get(id)
        if obj:
            self.db.delete(obj)
            self.db.commit()
        return obj

    def count(self, filters: Optional[dict] = None) -> int:
        """Count records with optional filters."""
        query = self.db.query(self.model)
        if filters:
            for key, value in filters.items():
                if hasattr(self.model, key):
                    query = query.filter(getattr(self.model, key) == value)
        return query.count()
