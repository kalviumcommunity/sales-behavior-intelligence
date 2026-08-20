"""Deal Metrics Component"""
import streamlit as st


def render_deal_metrics(deal):
    """Render key deal metrics in compact form."""
    
    def format_currency(value):
        if value >= 1_000_000:
            return f"${value / 1_000_000:.2f}M"
        if value >= 1_000:
            return f"${value / 1_000:.0f}K"
        return f"${value:,.0f}"
    
    st.html("<div class='section-heading'>📊 Deal Metrics</div>")
    
    metric_cols = st.columns(6)
    
    metrics = [
        ("Deal Value", format_currency(deal["deal_value"])),
        ("Days Open", str(deal["days_open"])),
        ("Days in Stage", str(deal["days_in_stage"])),
        ("Stakeholders", str(deal["stakeholders_count"])),
        ("Interactions", str(deal["interactions_count"])),
        ("Last Activity", deal["last_activity_label"]),
    ]
    
    for col, (label, value) in zip(metric_cols, metrics):
        with col:
            st.markdown(
                f"""
                <div class='deal-metric-card'>
                    <div class='deal-metric__label'>{label}</div>
                    <div class='deal-metric__value'>{value}</div>
                </div>
                """
            )
