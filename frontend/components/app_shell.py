"""Premium Application Shell Component

Unified shell for all authenticated pages including:
- Left sidebar navigation (~240px)
- Top navigation bar with breadcrumb
- Main content area with consistent padding
"""

import streamlit as st

def get_sidebar_css():
    """CSS specifically for the sidebar and topbar layout in authenticated pages."""
    return """
    <style>
    /* HIDE NATIVE STREAMLIT MULTIPAGE NAV */
    [data-testid="stSidebarNav"],
    [data-testid="stSidebarNavSeparator"],
    [data-testid="stSidebarNavItems"],
    section[data-testid="stSidebar"] > div:first-child > div:first-child > div:first-child > nav,
    section[data-testid="stSidebar"] ul.streamlit-menu { display: none !important; }

    /* SIDEBAR STYLES */
    section[data-testid="stSidebar"] {
        background: var(--sbi-bg-secondary) !important;
        border-right: 1px solid var(--sbi-border-subtle) !important;
        width: 240px !important;
        min-width: 240px !important;
    }
    section[data-testid="stSidebar"] > div:first-child {
        padding: var(--sbi-sp-4) !important;
        display: flex;
        flex-direction: column;
        height: 100vh;
    }

    .sbi-sidebar-brand {
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: var(--sbi-sp-8);
        padding: 4px;
    }

    .sbi-sidebar-brand-icon {
        width: 32px;
        height: 32px;
        border-radius: var(--sbi-r-md);
        background: linear-gradient(135deg, var(--sbi-cyan), var(--sbi-violet));
        display: flex;
        align-items: center;
        justify-content: center;
        color: var(--sbi-text-inverse);
        font-weight: 800;
        font-size: 16px;
        flex-shrink: 0;
    }

    .sbi-sidebar-brand-text {
        flex: 1;
        min-width: 0;
    }
    .sbi-sidebar-brand-title {
        font-size: 13px;
        font-weight: 700;
        color: var(--sbi-text-primary);
        margin: 0;
        line-height: 1.2;
        letter-spacing: -0.01em;
    }

    .sbi-nav-section-label {
        font-size: 10px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.12em;
        color: var(--sbi-text-muted);
        margin: var(--sbi-sp-4) 0 var(--sbi-sp-2) 4px;
        display: block;
    }

    .stButton > button.sbi-nav-item {
        background: transparent !important;
        border: 1px solid transparent !important;
        color: var(--sbi-text-secondary) !important;
        justify-content: flex-start !important;
        padding: 8px 12px !important;
        font-weight: 500 !important;
        font-size: 14px !important;
        width: 100% !important;
    }
    
    .stButton > button.sbi-nav-item:hover {
        background: rgba(255,255,255,0.03) !important;
        color: var(--sbi-text-primary) !important;
    }
    
    .stButton > button.sbi-nav-item-active {
        background: var(--sbi-cyan-dim) !important;
        border: 1px solid rgba(94,231,255,0.2) !important;
        color: var(--sbi-cyan) !important;
        justify-content: flex-start !important;
        padding: 8px 12px !important;
        font-weight: 600 !important;
        font-size: 14px !important;
        width: 100% !important;
    }

    /* USER PROFILE SECTION */
    .sbi-sidebar-user {
        margin-top: auto;
        display: flex;
        align-items: center;
        gap: 12px;
        padding: 12px;
        background: rgba(255, 255, 255, 0.02);
        border: 1px solid var(--sbi-border-subtle);
        border-radius: var(--sbi-r-md);
    }
    .sbi-user-avatar {
        width: 36px;
        height: 36px;
        border-radius: var(--sbi-r-sm);
        background: linear-gradient(135deg, var(--sbi-violet), var(--sbi-cyan));
        display: flex;
        align-items: center;
        justify-content: center;
        color: var(--sbi-text-inverse);
        font-weight: 700;
        font-size: 13px;
        flex-shrink: 0;
    }
    .sbi-user-info { flex: 1; min-width: 0; }
    .sbi-user-name { font-size: 13px; font-weight: 600; color: var(--sbi-text-primary); margin: 0; }
    .sbi-user-role { font-size: 11px; color: var(--sbi-text-muted); margin: 2px 0 0 0; }

    /* TOP BAR STYLES */
    .sbi-topbar {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: var(--sbi-sp-4) var(--sbi-sp-6);
        background: var(--sbi-bg-secondary);
        border-bottom: 1px solid var(--sbi-border-subtle);
        margin: -var(--sbi-sp-6) -var(--sbi-sp-8) var(--sbi-sp-6) -var(--sbi-sp-8); /* Negative margin to hit edges */
    }

    .sbi-topbar-breadcrumb {
        display: flex;
        align-items: center;
        gap: 8px;
        font-size: 13px;
        color: var(--sbi-text-muted);
    }
    .sbi-topbar-breadcrumb a { color: var(--sbi-text-primary); text-decoration: none; font-weight: 500; }
    .sbi-topbar-breadcrumb .separator { color: var(--sbi-text-muted); }

    .sbi-topbar-actions {
        display: flex;
        align-items: center;
        gap: 12px;
    }
    
    .sbi-topbar-icon {
        width: 36px;
        height: 36px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: var(--sbi-r-sm);
        background: var(--sbi-bg-surface);
        border: 1px solid var(--sbi-border-subtle);
        color: var(--sbi-text-secondary);
        cursor: pointer;
        transition: all var(--sbi-t-fast);
        font-size: 16px;
    }
    .sbi-topbar-icon:hover {
        background: var(--sbi-bg-hover);
        color: var(--sbi-text-primary);
    }
    
    /* PAGE HEADER */
    .sbi-page-header {
        margin-bottom: var(--sbi-sp-8);
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
    }
    .sbi-page-title {
        font-size: 32px;
        font-weight: 700;
        color: var(--sbi-text-primary);
        margin: 0 0 var(--sbi-sp-1) 0;
        letter-spacing: -0.02em;
    }
    .sbi-page-subtitle {
        font-size: 15px;
        color: var(--sbi-text-secondary);
        margin: 0;
    }
    
    @media (max-width: 1024px) {
        .sbi-topbar { margin: -var(--sbi-sp-4) -var(--sbi-sp-5) var(--sbi-sp-5) -var(--sbi-sp-5); }
    }
    @media (max-width: 768px) {
        .sbi-topbar { margin: -var(--sbi-sp-3) -var(--sbi-sp-4) var(--sbi-sp-4) -var(--sbi-sp-4); }
        .sbi-page-title { font-size: 24px; }
    }
    </style>
    """

def render_sidebar(active_item="Dashboard"):
    """Render the unified sidebar navigation."""
    st.markdown(get_sidebar_css(), unsafe_allow_html=True)
    
    with st.sidebar:
        # Brand
        st.markdown(
            """
            <div class='sbi-sidebar-brand'>
                <div class='sbi-sidebar-brand-icon'>SBI</div>
                <div class='sbi-sidebar-brand-text'>
                    <p class='sbi-sidebar-brand-title'>Sales Behavior<br>Intelligence</p>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Overview Section
        st.markdown("<div class='sbi-nav-section-label'>OVERVIEW</div>", unsafe_allow_html=True)
        if st.button("📊 Dashboard", key="nav_dashboard", use_container_width=True, type="primary" if active_item == "Dashboard" else "secondary"):
            st.switch_page("pages/dashboard.py")

        # Pipeline Section
        st.markdown("<div class='sbi-nav-section-label'>PIPELINE</div>", unsafe_allow_html=True)
        if st.button("◆ Deals", key="nav_deals", use_container_width=True, type="primary" if active_item == "Deals" else "secondary"):
            st.switch_page("pages/2_Deals.py")

        # Insights Section
        st.markdown("<div class='sbi-nav-section-label'>INSIGHTS</div>", unsafe_allow_html=True)
        if st.button("👥 Sales Reps", key="nav_reps", use_container_width=True, type="primary" if active_item == "Sales Reps" else "secondary"):
            st.switch_page("pages/4_Sales_Reps.py")
        if st.button("✦ AI Coaching", key="nav_coaching", use_container_width=True, type="primary" if active_item == "AI Coaching" else "secondary"):
            st.switch_page("pages/5_AI_Coaching.py")
        if st.button("▣ Analytics", key="nav_analytics", use_container_width=True, type="primary" if active_item == "Analytics" else "secondary"):
            st.switch_page("pages/6_Analytics.py")

        # System Section
        st.markdown("<div class='sbi-nav-section-label'>SYSTEM</div>", unsafe_allow_html=True)
        if st.button("⚙️ Settings", key="nav_settings", use_container_width=True, type="primary" if active_item == "Settings" else "secondary"):
            st.switch_page("pages/7_Settings.py")
            
        if st.button("↪️  Logout", key="nav_logout", use_container_width=True, type="secondary"):
            st.session_state.authenticated = False
            st.switch_page("pages/1_Authentication.py")

        # Basic sidebar button styling (without :contains)
        st.markdown(
            """
            <style>
            div[data-testid="stSidebar"] button[data-testid="baseButton-secondary"] {
                justify-content: flex-start !important;
                border: none !important;
                background: transparent !important;
                color: var(--sbi-text-secondary) !important;
            }
            div[data-testid="stSidebar"] button[data-testid="baseButton-secondary"]:hover {
                background: rgba(255,255,255,0.03) !important;
                color: var(--sbi-text-primary) !important;
            }
            div[data-testid="stSidebar"] button[data-testid="baseButton-primary"] {
                justify-content: flex-start !important;
                background: var(--sbi-cyan-dim) !important;
                border: 1px solid rgba(94,231,255,0.2) !important;
                color: var(--sbi-cyan) !important;
                font-weight: 600 !important;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        # User Profile at the bottom
        st.markdown(
            """
            <div class='sbi-sidebar-user'>
                <div class='sbi-user-avatar'>SJ</div>
                <div class='sbi-user-info'>
                    <p class='sbi-user-name'>Sarah Johnson</p>
                    <p class='sbi-user-role'>Sales Manager</p>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

def render_topbar(breadcrumb="Dashboard", actions_html=""):
    """Render the top navigation bar."""
    st.markdown(
        f"""
        <div class='sbi-topbar'>
            <div class='sbi-topbar-breadcrumb'>
                <span>Sales Behavior Intelligence</span>
                <span class='separator'>/</span>
                <a href="#">{breadcrumb}</a>
            </div>
            <div class='sbi-topbar-actions'>
                <div class='sbi-topbar-icon'>🔍</div>
                <div class='sbi-topbar-icon'>🔔</div>
                {actions_html}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

def render_page_header(title, subtitle="", header_actions=None):
    """Render a page header with optional subtitle and actions."""
    actions_html = ""
    if header_actions:
        actions_html = f"<div style='display: flex; gap: 8px;'>{header_actions}</div>"
        
    st.markdown(
        f"""
        <div class='sbi-page-header'>
            <div>
                <h1 class='sbi-page-title'>{title}</h1>
                {f"<p class='sbi-page-subtitle'>{subtitle}</p>" if subtitle else ""}
            </div>
            {actions_html}
        </div>
        """,
        unsafe_allow_html=True,
    )
