import streamlit as st


def render_risk_card(company, deal_value, risk_score, stage, assigned_rep, recommended_action):
    st.markdown(
        f"""
        <div class="risk-card">
            <div class="risk-card__header">
                <div>
                    <div class="risk-card__company">{company}</div>
                    <div class="risk-card__value">{deal_value}</div>
                </div>
                <div class="risk-card__score">Risk {risk_score}</div>
            </div>
            <div class="risk-card__grid">
                <div><span>Stage</span><strong>{stage}</strong></div>
                <div><span>Assigned Rep</span><strong>{assigned_rep}</strong></div>
            </div>
            <div class="risk-card__action">
                <span>Recommended Action</span>
                <strong>{recommended_action}</strong>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
