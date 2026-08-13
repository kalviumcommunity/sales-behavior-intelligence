"""Risk Analysis Component"""
import streamlit as st


def render_risk_analysis(risk_factors):
    """Render risk analysis section."""
    
    st.markdown("<div class='section-heading'>⚠️ Why This Deal Is At Risk</div>", unsafe_allow_html=True)
    
    for risk in risk_factors:
        severity_color = (
            "#ff8ea7" if risk["severity"] == "HIGH"
            else "#ffb76a" if risk["severity"] == "MEDIUM"
            else "#57d8ff"
        )
        
        severity_icon = (
            "🔴" if risk["severity"] == "HIGH"
            else "🟡" if risk["severity"] == "MEDIUM"
            else "🔵"
        )
        
        st.markdown(
            f"""
            <div class='risk-card'>
                <div class='risk-card__header'>
                    <div class='risk-card__severity' style='color: {severity_color};'>
                        {severity_icon} {risk["severity"]}
                    </div>
                    <div class='risk-card__title'>{risk["reason"]}</div>
                </div>
                <div class='risk-card__content'>
                    <div class='risk-card__description'>{risk["description"]}</div>
                </div>
                <div class='risk-card__footer'>
                    <div class='risk-card__section'>
                        <div class='risk-card__section-label'>Recommended Action</div>
                        <div class='risk-card__section-value'>{risk["recommended_action"]}</div>
                    </div>
                    <div class='risk-card__section'>
                        <div class='risk-card__section-label'>Impact If Not Addressed</div>
                        <div class='risk-card__section-value'>{risk["impact"]}</div>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
