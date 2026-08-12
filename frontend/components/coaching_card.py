import streamlit as st


def render_coaching_card(rep, problem, suggestion, confidence):
    st.markdown(
        f"""
        <div class="coaching-card">
            <div class="coaching-card__header">
                <div class="coaching-card__eyebrow">Rep</div>
                <div class="coaching-card__rep">{rep}</div>
            </div>
            <div class="coaching-card__field">
                <span>Problem</span>
                <strong>{problem}</strong>
            </div>
            <div class="coaching-card__field">
                <span>Suggestion</span>
                <strong>{suggestion}</strong>
            </div>
            <div class="coaching-card__footer">
                <span>Confidence</span>
                <strong>{confidence}%</strong>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
