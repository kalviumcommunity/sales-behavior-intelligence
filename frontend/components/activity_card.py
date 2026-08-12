import streamlit as st


def render_activity_card(time, title, detail, icon="◌"):
    st.markdown(
        f"""
        <div class="activity-card">
            <div class="activity-card__time">{time}</div>
            <div class="activity-card__title">{icon} {title}</div>
            <div class="activity-card__detail">{detail}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
