"""Coaching Recommendation Component"""

import streamlit as st


def render_coaching_recommendation(coaching_data):
    """Render coaching recommendation section."""

    st.html(f"""
        <div class='coaching-card'>
            <div class='coaching-card__header'>
                <div class='coaching-card__icon'>🎯</div>
                <div>
                    <div class='coaching-card__title'>Recommended Coaching</div>
                    <div class='coaching-card__confidence'>Confidence: {coaching_data["confidence"]}%</div>
                </div>
            </div>
            <div class='coaching-card__main-title'>{coaching_data["title"]}</div>
            
            <div class='coaching-card__section'>
                <div class='coaching-card__section-label'>Why</div>
                <div class='coaching-card__section-value'>{coaching_data["why"]}</div>
            </div>
            
            <div class='coaching-card__section'>
                <div class='coaching-card__section-label'>Recommended Action</div>
                <div class='coaching-card__section-value'>{coaching_data["recommended_action"]}</div>
            </div>
            
            <div class='coaching-card__section'>
                <div class='coaching-card__section-label'>Expected Impact</div>
                <div class='coaching-card__section-value'>{coaching_data["expected_impact"]}</div>
            </div>
        </div>
        """)

    st.markdown("<div style='height: 1rem;'></div>")

    col1, col2, col3 = st.columns([2, 1, 1])
    with col3:
        if st.button(
            "✓ Mark as Reviewed", use_container_width=True, key="coaching_reviewed"
        ):
            st.toast("Coaching marked as reviewed!", icon="✓")
