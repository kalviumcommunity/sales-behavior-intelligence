import streamlit as st

from frontend.dashboard_data import DASHBOARD_NAV_ITEMS, CURRENT_USER


PAGE_ROUTES = {
    "Dashboard": "pages/dashboard.py",
    "Deals": "pages/2_Deals.py",
}


def render_sidebar(collapsed=False, active_item="Dashboard"):
    if "dashboard_sidebar_collapsed" not in st.session_state:
        st.session_state.dashboard_sidebar_collapsed = collapsed

    is_collapsed = st.session_state.dashboard_sidebar_collapsed

    with st.sidebar:
        st.markdown(
            """
            <div class="sidebar-shell">
                <div class="sidebar-brand">
                    <div class="sidebar-avatar">SB</div>
                    <div>
                        <div class="sidebar-brand__eyebrow">Revenue command center</div>
                        <div class="sidebar-brand__title">Sales Behavior Intelligence</div>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        toggle_label = "Expand sidebar" if is_collapsed else "Collapse sidebar"
        if st.button(toggle_label, use_container_width=True, key="sidebar_toggle_button"):
            st.session_state.dashboard_sidebar_collapsed = not is_collapsed
            st.rerun()

        st.markdown("<div style='height: 0.4rem;'></div>", unsafe_allow_html=True)

        for item in DASHBOARD_NAV_ITEMS:
            label = item["icon"] if is_collapsed else f"{item['icon']} {item['label']}"
            if item["label"] == active_item and not is_collapsed:
                label = f"▸ {label}"
            if st.button(label, use_container_width=True, key=f"sidebar_nav_{item['label']}"):
                if item["label"] == "Logout":
                    st.session_state.pop("authenticated", None)
                    st.session_state.pop("dashboard_active_item", None)
                    st.switch_page("pages/1_Authentication.py")
                elif item["label"] in PAGE_ROUTES:
                    st.session_state.dashboard_active_item = item["label"]
                    st.switch_page(PAGE_ROUTES[item["label"]])
                else:
                    st.session_state.dashboard_active_item = item["label"]
                    st.toast(f"{item['label']} selected", icon=item["icon"])
                    st.rerun()

        st.markdown("<div style='height: 0.75rem;'></div>", unsafe_allow_html=True)
        if is_collapsed:
            st.markdown(
                f"<div class='sidebar-collapsed-card'><strong>{CURRENT_USER['avatar']}</strong></div>",
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                f"""
                <div class="sidebar-user-card">
                    <div class="sidebar-user-card__avatar">{CURRENT_USER['avatar']}</div>
                    <div>
                        <div class="sidebar-user-card__name">{CURRENT_USER['name']}</div>
                        <div class="sidebar-user-card__role">{CURRENT_USER['role']}</div>
                        <div class="sidebar-user-card__meta">{CURRENT_USER['team']}</div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
