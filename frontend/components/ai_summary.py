"""AI Deal Summary Component"""

import streamlit as st


def render_ai_summary(ai_data):
    """Render AI-generated deal summary."""

    st.html(f"""
        <div class='ai-summary-card'>
            <div class='ai-summary__header'>
                <div class='ai-summary__title'>🤖 AI Deal Summary</div>
                <div class='ai-summary__confidence'>Confidence: {ai_data["confidence"]}%</div>
            </div>
            <div class='ai-summary__content'>
                <p>{ai_data["summary"]}</p>
            </div>
        </div>
        """)

    # Key Signals
    st.markdown("<div style='height: 0.5rem;'></div>")

    col1, col2 = st.columns([1, 4])
    with col1:
        st.html("<div class='ai-summary__signals-label'>Key Signals</div>")

    # Render signals as list
    signals_html = "".join(f"<li>{signal}</li>" for signal in ai_data["key_signals"])

    st.markdown(f"""
        <ul class='ai-summary__signals-list'>
            {signals_html}
        </ul>
        """)
