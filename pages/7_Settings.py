import streamlit as st

from frontend.design_system import inject_design_system
from frontend.components.app_shell import render_sidebar, render_topbar, render_page_header
from frontend.components.ui_components import section_header, badge_html

st.set_page_config(
    page_title="Settings | Sales Behavior Intelligence",
    page_icon="◆",
    layout="wide",
    initial_sidebar_state="expanded",
)

if not st.session_state.get("authenticated"):
    st.switch_page("pages/1_Authentication.py")

inject_design_system()
render_sidebar(active_item="Settings")
render_topbar(breadcrumb="Settings")

render_page_header("Settings", "Manage your account, workspace, and integrations.")

# ── Settings layout: nav + content ────────────────────────────
SETTINGS_SECTIONS = [
    {"id": "profile", "label": "Profile", "icon": "◉"},
    {"id": "workspace", "label": "Workspace", "icon": "◼"},
    {"id": "notifications", "label": "Notifications", "icon": "◌"},
    {"id": "ai_prefs", "label": "AI Preferences", "icon": "✦"},
    {"id": "integrations", "label": "CRM Integrations", "icon": "◆"},
    {"id": "security", "label": "Security", "icon": "⚿"},
]

if "settings_section" not in st.session_state:
    st.session_state.settings_section = "profile"

# ── Settings nav sidebar + content ────────────────────────────
nav_col, content_col = st.columns([1, 3])

with nav_col:
    nav_html = "<div style='background: var(--sbi-bg-surface); border: 1px solid var(--sbi-border-subtle); border-radius: 12px; overflow: hidden;'>"
    for s in SETTINGS_SECTIONS:
        is_active = st.session_state.settings_section == s["id"]
        active_style = "background: var(--sbi-cyan-dim); color: var(--sbi-cyan); font-weight: 600;" if is_active else "color: var(--sbi-text-secondary);"
        nav_html += f"""
        <div style="padding: 12px 16px; font-size: 13px; border-bottom: 1px solid var(--sbi-border-subtle); {active_style} cursor: pointer; display: flex; align-items: center; gap: 10px;">
            <span style="font-size: 14px;">{s['icon']}</span>
            {s['label']}
        </div>
        """
    nav_html += "</div>"
    st.html(nav_html)

    st.html("<div style='height: 12px;'></div>")
    for s in SETTINGS_SECTIONS:
        if st.button(s["label"], key=f"nav_{s['id']}", use_container_width=True, type="primary" if st.session_state.settings_section == s["id"] else "secondary"):
            st.session_state.settings_section = s["id"]
            st.rerun()

with content_col:
    section = st.session_state.settings_section

    # ── Profile ─────────────────────────────────────────────
    if section == "profile":
        section_header("Profile", "Your personal information and account details.")

        st.html(
            """
            <div style="display: flex; align-items: center; gap: 20px; padding: 20px 0; border-bottom: 1px solid var(--sbi-border-subtle); margin-bottom: 24px;">
                <div style="width: 56px; height: 56px; border-radius: 12px; background: linear-gradient(135deg, rgba(139,124,255,0.3), rgba(94,231,255,0.3)); border: 1px solid rgba(94,231,255,0.2); display: flex; align-items: center; justify-content: center; font-size: 18px; font-weight: 700;">SJ</div>
                <div>
                    <div style="font-weight: 700; font-size: 16px;">Sarah Johnson</div>
                    <div style="font-size: 12px; color: var(--sbi-text-muted); margin-top: 2px;">Sales Manager · Enterprise Growth</div>
                </div>
            </div>
            """
        )

        col1, col2 = st.columns(2)
        with col1:
            st.text_input("Full Name", value="Sarah Johnson")
            st.text_input("Job Title", value="Sales Manager")
        with col2:
            st.text_input("Email", value="sarah.johnson@salesbehaviour.ai")
            st.text_input("Team", value="Enterprise Growth")

        st.markdown("<div style='height: 16px;'></div>")
        col_btn, _ = st.columns([1, 3])
        with col_btn:
            if st.button("Save Changes", key="save_profile", use_container_width=True, type="primary"):
                st.success("Profile saved.", icon="✓")

    # ── Workspace ────────────────────────────────────────────
    elif section == "workspace":
        section_header("Workspace", "Configure your Sales Behavior Intelligence workspace settings.")

        st.text_input("Workspace Name", value="Enterprise Growth Team")
        st.text_input("Organization", value="Sales Behavior Intelligence Corp.")

        st.html("<div style='height: 16px;'></div>")
        st.html(
            """
            <div style="font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.07em; color: var(--sbi-text-muted); margin-bottom: 12px;">Fiscal Year</div>
            """
        )
        fy_col1, fy_col2 = st.columns(2)
        with fy_col1:
            st.selectbox("Fiscal Year Start", ["January", "April", "July", "October"], label_visibility="collapsed")
        with fy_col2:
            st.selectbox("Quarter Model", ["Standard (Q1–Q4)", "Custom"], label_visibility="collapsed")

        st.markdown("<div style='height: 16px;'></div>")
        col_btn, _ = st.columns([1, 3])
        with col_btn:
            if st.button("Save Workspace", key="save_workspace", use_container_width=True, type="primary"):
                st.success("Workspace settings saved.", icon="✓")

    # ── Notifications ─────────────────────────────────────────
    elif section == "notifications":
        section_header("Notifications", "Control which signals and events trigger notifications.")

        notification_settings = [
            ("Risk Alerts", "Get notified when a deal enters high-risk status.", True),
            ("Coaching Recommendations", "Receive AI-generated coaching suggestions.", True),
            ("Deal Stage Changes", "Notify when a deal advances or regresses.", True),
            ("Meeting Reminders", "15-minute pre-meeting reminders.", True),
            ("Weekly Pipeline Summary", "Email digest every Monday morning.", False),
            ("Rep Inactivity Alerts", "Alert when a rep hasn't updated a deal in 5+ days.", True),
        ]

        for name, desc, default in notification_settings:
            row_col1, row_col2 = st.columns([4, 1])
            with row_col1:
                st.html(
                    f"""
                    <div style="padding: 12px 0; border-bottom: 1px solid var(--sbi-border-subtle);">
                        <div style="font-size: 14px; font-weight: 600;">{name}</div>
                        <div style="font-size: 12px; color: var(--sbi-text-muted); margin-top: 2px;">{desc}</div>
                    </div>
                    """
                )
            with row_col2:
                st.markdown("<div style='height: 8px;'></div>")
                st.toggle("", value=default, key=f"notif_{name.replace(' ', '_').lower()}")

    # ── AI Preferences ────────────────────────────────────────
    elif section == "ai_prefs":
        section_header("AI Preferences", "Tune the AI coaching engine to match your team's needs.")

        st.html(
            """<div style="font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.07em; color: var(--sbi-text-muted); margin-bottom: 16px;">Risk Detection Sensitivity</div>"""
        )
        risk_level = st.select_slider(
            "Risk sensitivity",
            options=["Low", "Moderate", "High", "Very High"],
            value="High",
            label_visibility="collapsed",
        )
        st.caption(f"Current: **{risk_level}** — AI will flag more deals as at-risk with higher sensitivity.")

        st.markdown("<div style='height: 20px;'></div>")
        st.html(
            """<div style="font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.07em; color: var(--sbi-text-muted); margin-bottom: 16px;">Minimum Confidence Threshold</div>"""
        )
        threshold = st.slider("Confidence threshold", min_value=60, max_value=99, value=88, label_visibility="collapsed")
        st.caption(f"Only show coaching recommendations with ≥{threshold}% AI confidence.")

        st.markdown("<div style='height: 20px;'></div>")
        st.html(
            """<div style="font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.07em; color: var(--sbi-text-muted); margin-bottom: 16px;">Coaching Frequency</div>"""
        )
        coaching_freq = st.radio(
            "Coaching frequency",
            options=["Real-time", "Daily digest", "Weekly summary"],
            index=0,
            label_visibility="collapsed",
            horizontal=True,
        )

        st.markdown("<div style='height: 16px;'></div>")
        col_btn, _ = st.columns([1, 3])
        with col_btn:
            if st.button("Save AI Preferences", key="save_ai", use_container_width=True, type="primary"):
                st.success("AI preferences saved.", icon="✓")

    # ── CRM Integrations ──────────────────────────────────────
    elif section == "integrations":
        section_header("CRM Integrations", "Connect your CRM to enable automatic activity sync.")

        integrations = [
            {"name": "Salesforce", "status": "Demo Mode", "status_cls": "neutral", "icon": "☁", "desc": "Connect to sync deals, activities, and contacts."},
            {"name": "HubSpot", "status": "Not Connected", "status_cls": "neutral", "icon": "⬡", "desc": "Bi-directional sync with HubSpot CRM."},
            {"name": "Outreach.io", "status": "Demo Mode", "status_cls": "neutral", "icon": "✉", "desc": "Analyze outreach sequences and email cadence data."},
            {"name": "Gong", "status": "Not Connected", "status_cls": "neutral", "icon": "◎", "desc": "Import call transcripts for behavioral analysis."},
        ]

        for crm in integrations:
            st.html(
                f"""
                <div style="display: flex; align-items: center; gap: 16px; padding: 16px 0; border-bottom: 1px solid var(--sbi-border-subtle);">
                    <div style="width: 40px; height: 40px; border-radius: 8px; background: var(--sbi-bg-elevated); border: 1px solid var(--sbi-border-subtle); display: flex; align-items: center; justify-content: center; font-size: 16px; color: var(--sbi-text-secondary);">{crm['icon']}</div>
                    <div style="flex: 1;">
                        <div style="font-weight: 600; font-size: 14px; margin-bottom: 2px;">{crm['name']}</div>
                        <div style="font-size: 12px; color: var(--sbi-text-muted);">{crm['desc']}</div>
                    </div>
                    {badge_html(crm['status'], crm['status_cls'])}
                </div>
                """
            )

        st.markdown(
            """
            <div style="margin-top: 20px; padding: 16px; background: var(--sbi-bg-elevated); border-radius: 10px; border: 1px solid var(--sbi-border-subtle);">
                <div style="font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.07em; color: var(--sbi-text-muted); margin-bottom: 6px;">Demo Environment</div>
                <div style="font-size: 12px; color: var(--sbi-text-secondary);">This is a demonstration environment. CRM integrations use simulated data. In production, real sync would be configured here.</div>
            </div>
            """
        )

    # ── Security ──────────────────────────────────────────────
    elif section == "security":
        section_header("Security", "Manage your password, sessions, and access controls.")

        st.markdown(
            """
            <div style="font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.07em; color: var(--sbi-text-muted); margin-bottom: 16px;">Change Password</div>
            """
        )
        st.text_input("Current Password", type="password")
        col1, col2 = st.columns(2)
        with col1:
            st.text_input("New Password", type="password")
        with col2:
            st.text_input("Confirm Password", type="password")

        st.markdown("<div style='height: 16px;'></div>")
        col_btn, _ = st.columns([1, 3])
        with col_btn:
            if st.button("Update Password", key="update_pwd", use_container_width=True, type="primary"):
                st.success("Password updated.", icon="✓")

        st.html("<div style='height: 24px;'></div>")
        st.markdown(
            f"""
            <div style="font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.07em; color: var(--sbi-text-muted); margin-bottom: 12px;">Active Sessions</div>
            <div style="display: flex; justify-content: space-between; align-items: center; padding: 12px 0; border-bottom: 1px solid var(--sbi-border-subtle);">
                <div>
                    <div style="font-size: 13px; font-weight: 600;">Current Session — Chrome on Windows</div>
                    <div style="font-size: 11px; color: var(--sbi-text-muted); margin-top: 2px;">Delhi, India · Active now</div>
                </div>
                {badge_html('Active', 'success')}
            </div>
            """
        )
