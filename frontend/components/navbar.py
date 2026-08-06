import streamlit as st

from frontend.dashboard_data import CURRENT_USER


def render_top_navbar(search_value="", breadcrumb="Home / Manager Dashboard", current_date="", notifications=3):
    col_search, col_notifications, col_profile = st.columns([4.2, 0.8, 1.8], vertical_alignment="center")

    with col_search:
        st.markdown(f"<div class='breadcrumb'>{breadcrumb}</div>", unsafe_allow_html=True)
        query = st.text_input(
            "Search dashboard",
            value=search_value,
            placeholder="Search deals, reps, stages, meetings...",
            label_visibility="collapsed",
            key="dashboard_search",
        )
        st.caption(current_date)

    with col_notifications:
        st.markdown("<div class='topnav-spacer'></div>", unsafe_allow_html=True)
        st.button(f"🔔 {notifications}", use_container_width=True, key="notifications_button")

    with col_profile:
        st.markdown(
            f"""
            <div class="profile-chip">
                <div class="profile-chip__avatar">{CURRENT_USER['avatar']}</div>
                <div>
                    <div class="profile-chip__name">{CURRENT_USER['name']}</div>
                    <div class="profile-chip__meta">{CURRENT_USER['role']} · {CURRENT_USER['team']}</div>
                    <div class="profile-chip__theme">Theme: Midnight Glass</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    return query
