"""Premium Application Shell Component

Unified shell for all authenticated pages including:
- Left sidebar navigation (~240px)
- Top navigation bar with breadcrumb
- Main content area with consistent padding
- Responsive mobile drawer
"""

import streamlit as st


def render_app_shell():
    """Render the complete application shell."""
    st.markdown(get_shell_css(), unsafe_allow_html=True)
    
    # Initialize session state for sidebar
    if "sidebar_collapsed" not in st.session_state:
        st.session_state.sidebar_collapsed = False


def get_shell_css():
    """Get the application shell CSS."""
    return """
    <style>
    /* SIDEBAR STYLES */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, rgba(7, 10, 18, 0.98) 0%, rgba(11, 16, 26, 0.96) 100%) !important;
        border-right: 1px solid rgba(255, 255, 255, 0.08) !important;
        width: 240px !important;
        padding: 24px 16px !important;
    }

    .sidebar-brand {
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 32px;
        padding: 12px;
        border-radius: 10px;
        background: rgba(255, 255, 255, 0.02);
    }

    .sidebar-brand-icon {
        width: 40px;
        height: 40px;
        border-radius: 8px;
        background: linear-gradient(135deg, #5EE7FF 0%, #8B7CFF 100%);
        display: flex;
        align-items: center;
        justify-content: center;
        color: #070A12;
        font-weight: 800;
        font-size: 18px;
        flex-shrink: 0;
    }

    .sidebar-brand-text {
        flex: 1;
        min-width: 0;
    }

    .sidebar-brand-title {
        font-size: 13px;
        font-weight: 700;
        color: #F5F7FB;
        margin: 0;
        line-height: 1.2;
        letter-spacing: -0.01em;
    }

    .sidebar-brand-subtitle {
        font-size: 11px;
        color: #697386;
        margin: 2px 0 0 0;
        text-transform: uppercase;
        letter-spacing: 0.08em;
    }

    /* NAVIGATION SECTION */
    .nav-section {
        margin-bottom: 28px;
    }

    .nav-section-label {
        font-size: 10px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.12em;
        color: #697386;
        margin-bottom: 8px;
        padding: 0 4px;
        display: block;
    }

    .nav-items {
        display: flex;
        flex-direction: column;
        gap: 4px;
    }

    .nav-item {
        display: flex;
        align-items: center;
        gap: 10px;
        padding: 10px 12px;
        border-radius: 10px;
        background: transparent;
        border: 1px solid transparent;
        color: #A7B0C0;
        font-size: 14px;
        font-weight: 500;
        cursor: pointer;
        transition: all 200ms cubic-bezier(0.4, 0, 0.2, 1);
        text-decoration: none;
    }

    .nav-item:hover {
        background: rgba(255, 255, 255, 0.04);
        color: #F5F7FB;
    }

    .nav-item.active {
        background: rgba(94, 231, 255, 0.08);
        border-color: rgba(94, 231, 255, 0.2);
        color: #5EE7FF;
        font-weight: 600;
        position: relative;
    }

    .nav-item.active::before {
        content: '';
        position: absolute;
        left: 0;
        top: 0;
        bottom: 0;
        width: 3px;
        background: #5EE7FF;
        border-radius: 0 3px 3px 0;
    }

    .nav-icon {
        width: 20px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 16px;
        flex-shrink: 0;
    }

    .nav-label {
        flex: 1;
    }

    /* USER PROFILE SECTION */
    .sidebar-user {
        position: absolute;
        bottom: 16px;
        left: 16px;
        right: 16px;
        display: flex;
        align-items: center;
        gap: 12px;
        padding: 12px;
        background: rgba(255, 255, 255, 0.02);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 10px;
    }

    .user-avatar {
        width: 40px;
        height: 40px;
        border-radius: 8px;
        background: linear-gradient(135deg, #8B7CFF 0%, #5EE7FF 100%);
        display: flex;
        align-items: center;
        justify-content: center;
        color: #070A12;
        font-weight: 700;
        font-size: 14px;
        flex-shrink: 0;
    }

    .user-info {
        flex: 1;
        min-width: 0;
    }

    .user-name {
        font-size: 13px;
        font-weight: 600;
        color: #F5F7FB;
        margin: 0;
    }

    .user-role {
        font-size: 11px;
        color: #697386;
        margin: 2px 0 0 0;
    }

    .user-status {
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background: #4ADE80;
        flex-shrink: 0;
    }

    /* TOP BAR STYLES */
    .topbar {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 16px 32px;
        background: rgba(16, 23, 34, 0.4);
        border-bottom: 1px solid rgba(255, 255, 255, 0.08);
        margin-bottom: 32px;
    }

    .topbar-breadcrumb {
        display: flex;
        align-items: center;
        gap: 8px;
        font-size: 13px;
        color: #697386;
    }

    .topbar-breadcrumb a {
        color: #5EE7FF;
        text-decoration: none;
        transition: color 200ms;
    }

    .topbar-breadcrumb a:hover {
        color: #F5F7FB;
    }

    .topbar-breadcrumb .separator {
        color: #697386;
    }

    .topbar-actions {
        display: flex;
        align-items: center;
        gap: 16px;
    }

    .topbar-icon-button {
        width: 40px;
        height: 40px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 8px;
        background: rgba(255, 255, 255, 0.04);
        border: 1px solid rgba(255, 255, 255, 0.08);
        color: #A7B0C0;
        cursor: pointer;
        transition: all 200ms;
        font-size: 18px;
    }

    .topbar-icon-button:hover {
        background: rgba(255, 255, 255, 0.08);
        color: #F5F7FB;
    }

    /* PAGE HEADER */
    .page-header {
        margin-bottom: 32px;
    }

    .page-title {
        font-size: 32px;
        font-weight: 800;
        color: #F5F7FB;
        margin: 0 0 8px 0;
        letter-spacing: -0.03em;
        line-height: 1.2;
    }

    .page-subtitle {
        font-size: 15px;
        color: #A7B0C0;
        margin: 0;
        line-height: 1.5;
    }

    /* RESPONSIVE */
    @media (max-width: 1024px) {
        section[data-testid="stSidebar"] {
            width: 200px !important;
            padding: 20px 12px !important;
        }

        .topbar {
            padding: 12px 20px;
            margin-bottom: 20px;
        }

        .page-title {
            font-size: 28px;
        }
    }

    @media (max-width: 768px) {
        section[data-testid="stSidebar"] {
            width: 100% !important;
            padding: 16px !important;
            position: fixed;
            top: 0;
            left: 0;
            z-index: 1000;
            height: 100vh;
            overflow-y: auto;
            transform: translateX(-100%);
            transition: transform 300ms cubic-bezier(0.4, 0, 0.2, 1);
        }

        section[data-testid="stSidebar"].open {
            transform: translateX(0);
        }

        .main .block-container {
            margin-left: 0 !important;
        }

        .topbar {
            padding: 12px 16px;
            margin-bottom: 16px;
        }

        .page-title {
            font-size: 24px;
        }

        .page-subtitle {
            font-size: 13px;
        }
    }

    @media (max-width: 480px) {
        .topbar-actions {
            gap: 8px;
        }

        .topbar-icon-button {
            width: 36px;
            height: 36px;
            font-size: 16px;
        }

        .page-title {
            font-size: 20px;
        }
    }
    </style>
    """


def render_sidebar_navigation():
    """Render the sidebar navigation."""
    with st.sidebar:
        # Brand
        st.markdown(
            """
            <div class='sidebar-brand'>
                <div class='sidebar-brand-icon'>◆</div>
                <div class='sidebar-brand-text'>
                    <p class='sidebar-brand-title'>Sales Behavior</p>
                    <p class='sidebar-brand-subtitle'>Intelligence</p>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("<div style='height: 8px;'></div>", unsafe_allow_html=True)

        # Overview Section
        st.markdown("<div class='nav-section-label'>OVERVIEW</div>", unsafe_allow_html=True)
        if st.button("📊 Dashboard", key="nav_dashboard", use_container_width=True):
            st.session_state.current_page = "dashboard"
            st.switch_page("pages/dashboard.py")

        st.markdown("<div style='height: 4px;'></div>", unsafe_allow_html=True)

        # Pipeline Section
        st.markdown("<div class='nav-section-label'>PIPELINE</div>", unsafe_allow_html=True)
        if st.button("◆ Deals", key="nav_deals", use_container_width=True):
            st.session_state.current_page = "deals"
            st.switch_page("pages/2_Deals.py")

        st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)

        # Insights Section
        st.markdown("<div class='nav-section-label'>INSIGHTS</div>", unsafe_allow_html=True)
        if st.button("👥 Sales Reps", key="nav_reps", use_container_width=True):
            st.toast("Coming soon", icon="🚀")

        st.markdown("<div style='height: 4px;'></div>", unsafe_allow_html=True)
        if st.button("✦ AI Coaching", key="nav_coaching", use_container_width=True):
            st.toast("Coming soon", icon="🚀")

        st.markdown("<div style='height: 4px;'></div>", unsafe_allow_html=True)
        if st.button("▣ Analytics", key="nav_analytics", use_container_width=True):
            st.toast("Coming soon", icon="🚀")

        st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)

        # System Section
        st.markdown("<div class='nav-section-label'>SYSTEM</div>", unsafe_allow_html=True)
        if st.button("⚙️ Settings", key="nav_settings", use_container_width=True):
            st.toast("Coming soon", icon="🚀")

        st.markdown("<div style='height: 4px;'></div>", unsafe_allow_html=True)
        if st.button("↪️  Logout", key="nav_logout", use_container_width=True):
            st.session_state.authenticated = False
            st.switch_page("pages/1_Authentication.py")

        st.markdown("<div style='height: 32px;'></div>", unsafe_allow_html=True)

        # User Profile
        st.markdown(
            """
            <div class='sidebar-user'>
                <div class='user-avatar'>SJ</div>
                <div class='user-info'>
                    <p class='user-name'>Sarah Johnson</p>
                    <p class='user-role'>Sales Manager</p>
                </div>
                <div class='user-status'></div>
            </div>
            """,
            unsafe_allow_html=True,
        )


def render_topbar(breadcrumb="Dashboard"):
    """Render the top navigation bar."""
    st.markdown(
        f"""
        <div class='topbar'>
            <div class='topbar-breadcrumb'>
                <span>Workspace</span>
                <span class='separator'>/</span>
                <span>{breadcrumb}</span>
            </div>
            <div class='topbar-actions'>
                <div class='topbar-icon-button'>🔍</div>
                <div class='topbar-icon-button'>🔔</div>
                <div class='topbar-icon-button'>?</div>
                <div class='topbar-icon-button'>👤</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_page_header(title, subtitle="", show_actions=False):
    """Render a page header."""
    actions_html = ""
    if show_actions:
        actions_html = """
        <div style='display: flex; gap: 12px;'>
            <button style='padding: 8px 16px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.08); background: rgba(255,255,255,0.04); color: #F5F7FB; cursor: pointer;'>+ Add</button>
            <button style='padding: 8px 16px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.08); background: rgba(255,255,255,0.04); color: #F5F7FB; cursor: pointer;'>Export</button>
        </div>
        """

    st.markdown(
        f"""
        <div class='page-header'>
            <div style='display: flex; justify-content: space-between; align-items: flex-start;'>
                <div>
                    <h1 class='page-title'>{title}</h1>
                    {'<p class="page-subtitle">' + subtitle + '</p>' if subtitle else ''}
                </div>
                {actions_html}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
