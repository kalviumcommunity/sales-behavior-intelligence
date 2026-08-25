"""
Pydantic schemas for manager analytics responses.
"""

from pydantic import BaseModel


class RiskBreakdown(BaseModel):
    """Deal count by risk level."""

    low: int = 0
    medium: int = 0
    high: int = 0


class StageBreakdownItem(BaseModel):
    """Deal count and value for a pipeline stage."""

    stage: str
    count: int
    value: float


class RepPerformanceItem(BaseModel):
    """Rep summary for dashboard ranking."""

    id: str
    name: str
    role: str
    deals_count: int
    quota_attainment: int
    pipeline_value: float


class ManagerSummaryResponse(BaseModel):
    """Manager dashboard summary."""

    total_deals: int
    pipeline_value: float
    high_risk_deals: int
    open_coaching_cards: int
    risk_breakdown: RiskBreakdown
    stage_breakdown: list[StageBreakdownItem]
    rep_performance: list[RepPerformanceItem]
