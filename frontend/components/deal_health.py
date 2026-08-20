"""Deal Health Overview Component"""
import streamlit as st


def render_deal_health(health_metrics):
    """Render the deal health overview section."""
    
    cols = st.columns(4)
    
    # Health Score
    with cols[0]:
        score_pct = (health_metrics["health_score"] / health_metrics["health_max"]) * 100
        color = "#5fd6a0" if score_pct >= 70 else "#ffb76a" if score_pct >= 50 else "#ff8ea7"
        
        st.markdown(
            f"""
            <div class='deal-health-card'>
                <div class='deal-health__label'>Deal Health Score</div>
                <div class='deal-health__score' style='color: {color};'>
                    {health_metrics["health_score"]} / {health_metrics["health_max"]}
                </div>
                <div class='deal-health__bar'>
                    <div class='deal-health__progress' style='width: {score_pct}%; background-color: {color};'></div>
                </div>
            </div>
            """
        )
    
    # Risk Level
    with cols[1]:
        risk_color = "#ff8ea7" if health_metrics["risk_level"] == "High" else "#ffb76a" if health_metrics["risk_level"] == "Medium" else "#5fd6a0"
        
        st.markdown(
            f"""
            <div class='deal-health-card'>
                <div class='deal-health__label'>Risk Level</div>
                <div class='deal-health__value' style='color: {risk_color};'>{health_metrics["risk_level"]}</div>
                <div class='deal-health__meta'>Needs attention</div>
            </div>
            """
        )
    
    # Deal Velocity
    with cols[2]:
        velocity_color = "#ff8ea7" if "Below" in health_metrics["deal_velocity"] else "#ffb76a"
        
        st.markdown(
            f"""
            <div class='deal-health-card'>
                <div class='deal-health__label'>Deal Velocity</div>
                <div class='deal-health__value'>{health_metrics["deal_velocity"]}</div>
                <div class='deal-health__trend' style='color: {velocity_color};'>{health_metrics["velocity_trend"]}</div>
            </div>
            """
        )
    
    # Engagement
    with cols[3]:
        next_step_status = "✓ Confirmed" if health_metrics["next_step_confirmed"] else "✗ Not Confirmed"
        next_step_color = "#5fd6a0" if health_metrics["next_step_confirmed"] else "#ffb76a"
        
        st.markdown(
            f"""
            <div class='deal-health-card'>
                <div class='deal-health__label'>Next Step</div>
                <div class='deal-health__value' style='color: {next_step_color};'>{next_step_status}</div>
                <div class='deal-health__meta'>Action needed</div>
            </div>
            """
        )
