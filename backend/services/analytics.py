"""
Analytics service for manager dashboard metrics.
"""
from sqlalchemy import func
from sqlalchemy.orm import Session

from backend.models.coaching import CoachingCard
from backend.models.deal import Deal
from backend.models.rep import Rep
from backend.schemas.analytics import (ManagerSummaryResponse,
                                       RepPerformanceItem, RiskBreakdown,
                                       StageBreakdownItem)


class AnalyticsService:
    """Service for cross-entity analytics."""

    def __init__(self, db: Session):
        self.db = db

    def get_manager_summary(self) -> ManagerSummaryResponse:
        """Build top-level manager dashboard metrics."""
        total_deals = self.db.query(func.count(Deal.id)).scalar() or 0
        pipeline_value = self.db.query(func.coalesce(func.sum(Deal.amount), 0)).scalar() or 0
        high_risk_deals = self.db.query(func.count(Deal.id)).filter(Deal.risk_level == "High").scalar() or 0
        open_coaching_cards = (
            self.db.query(func.count(CoachingCard.id))
            .filter(CoachingCard.status != "Coached")
            .scalar()
            or 0
        )

        risk_counts = {
            risk_level.lower(): count
            for risk_level, count in self.db.query(Deal.risk_level, func.count(Deal.id)).group_by(Deal.risk_level).all()
        }

        stage_breakdown = [
            StageBreakdownItem(stage=stage, count=count, value=float(value or 0))
            for stage, count, value in (
                self.db.query(Deal.stage, func.count(Deal.id), func.coalesce(func.sum(Deal.amount), 0))
                .group_by(Deal.stage)
                .order_by(Deal.stage)
                .all()
            )
        ]

        rep_performance = [
            RepPerformanceItem(
                id=rep_id,
                name=name,
                role=role,
                deals_count=deals_count,
                quota_attainment=quota_attainment,
                pipeline_value=float(pipeline_value or 0),
            )
            for rep_id, name, role, deals_count, quota_attainment, pipeline_value in (
                self.db.query(
                    Rep.id,
                    Rep.name,
                    Rep.role,
                    Rep.deals_count,
                    Rep.quota_attainment,
                    func.coalesce(func.sum(Deal.amount), 0),
                )
                .outerjoin(Deal, Deal.rep_id == Rep.id)
                .group_by(Rep.id, Rep.name, Rep.role, Rep.deals_count, Rep.quota_attainment)
                .order_by(Rep.quota_attainment.desc())
                .all()
            )
        ]

        return ManagerSummaryResponse(
            total_deals=total_deals,
            pipeline_value=float(pipeline_value),
            high_risk_deals=high_risk_deals,
            open_coaching_cards=open_coaching_cards,
            risk_breakdown=RiskBreakdown(
                low=risk_counts.get("low", 0),
                medium=risk_counts.get("medium", 0),
                high=risk_counts.get("high", 0),
            ),
            stage_breakdown=stage_breakdown,
            rep_performance=rep_performance,
        )
