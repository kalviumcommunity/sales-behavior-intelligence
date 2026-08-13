"""Badge Components - Status, risk level, and other indicators."""

import streamlit as st


def render_status_badge(status, text=""):
    """Render a status badge.
    
    Args:
        status: "low", "medium", "high", "info", or "success"
        text: Badge text
    """
    colors = {
        "low": {"bg": "rgba(74, 222, 128, 0.1)", "text": "#4ADE80", "icon": "●"},
        "medium": {"bg": "rgba(251, 191, 36, 0.1)", "text": "#FBBF24", "icon": "●"},
        "high": {"bg": "rgba(251, 113, 133, 0.1)", "text": "#FB7185", "icon": "●"},
        "info": {"bg": "rgba(96, 165, 250, 0.1)", "text": "#60A5FA", "icon": "●"},
        "success": {"bg": "rgba(74, 222, 128, 0.1)", "text": "#4ADE80", "icon": "✓"},
    }

    color = colors.get(status, colors["info"])
    badge_text = text or status.capitalize()

    st.markdown(
        f"""
        <div style='
            display: inline-block;
            background: {color["bg"]};
            color: {color["text"]};
            padding: 6px 10px;
            border-radius: 6px;
            font-size: 12px;
            font-weight: 600;
            letter-spacing: 0.05em;
        '>
            {color["icon"]} {badge_text}
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_stage_badge(stage):
    """Render a deal stage badge."""
    st.markdown(
        f"""
        <div style='
            display: inline-block;
            background: rgba(94, 231, 255, 0.1);
            color: #5EE7FF;
            padding: 6px 12px;
            border-radius: 6px;
            font-size: 12px;
            font-weight: 600;
            border: 1px solid rgba(94, 231, 255, 0.2);
        '>
            {stage}
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_health_score(score, max_score=100):
    """Render a health score with progress bar.
    
    Args:
        score: Current score
        max_score: Maximum score (default 100)
    """
    percentage = (score / max_score) * 100
    color = "#4ADE80" if percentage >= 70 else "#FBBF24" if percentage >= 50 else "#FB7185"

    st.markdown(
        f"""
        <div style='display: flex; align-items: center; gap: 12px;'>
            <div style='flex: 1;'>
                <div style='
                    width: 100%;
                    height: 6px;
                    background: rgba(255, 255, 255, 0.08);
                    border-radius: 999px;
                    overflow: hidden;
                '>
                    <div style='
                        width: {percentage}%;
                        height: 100%;
                        background: {color};
                        border-radius: 999px;
                        transition: width 300ms ease;
                    '></div>
                </div>
            </div>
            <div style='font-size: 12px; font-weight: 700; color: {color}; white-space: nowrap;'>{score}/{max_score}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
