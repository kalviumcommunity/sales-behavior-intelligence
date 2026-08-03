"""
KPI Metrics Cards Component for Sales Behavior Intelligence Dashboard.
"""
import streamlit as st

def render_kpi_metrics(deals):
    """Calculates and displays top-level pipeline KPIs."""
    total_pipeline = sum(d["amount"] for d in deals)
    high_risk_deals = [d for d in deals if d["risk_level"] == "High"]
    at_risk_amount = sum(d["amount"] for d in high_risk_deals)
    avg_risk_score = round(sum(d["risk_score"] for d in deals) / len(deals)) if deals else 0

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            label="Total Active Pipeline",
            value=f"${total_pipeline:,.0f}",
            delta=f"{len(deals)} Active Deals",
        )

    with col2:
        st.metric(
            label="Pipeline at High Risk ⚠️",
            value=f"${at_risk_amount:,.0f}",
            delta=f"{len(high_risk_deals)} Deals Flagged",
            delta_color="inverse",
        )

    with col3:
        st.metric(
            label="Average Deal Risk Score",
            value=f"{avg_risk_score} / 100",
            delta="-12 vs last month" if avg_risk_score < 60 else "+8 vs last month",
            delta_color="inverse" if avg_risk_score > 50 else "normal",
        )

    with col4:
        st.metric(
            label="Coaching Action Rate",
            value="68%",
            delta="+14% adoption",
        )
