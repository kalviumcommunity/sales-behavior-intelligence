import altair as alt
import streamlit as st

from frontend.design_system import inject_design_system
from frontend.components.app_shell import render_sidebar, render_topbar, render_page_header
from frontend.components.ui_components import render_kpi_strip, badge_html, section_header, render_ai_panel
from frontend.dashboard_data import (
    CURRENT_USER,
    HIGH_RISK_DEALS,
    KPI_METRICS,
    MONTHLY_PERFORMANCE,
    PIPELINE_BY_STAGE,
    RECENT_ACTIVITIES,
    REVENUE_TREND,
    RISK_DISTRIBUTION,
    TOP_REPS,
    COACHING_SUGGESTIONS,
    UPCOMING_MEETINGS
)

st.set_page_config(
    page_title="Manager Dashboard | Sales Behavior Intelligence",
    page_icon="◆",
    layout="wide",
    initial_sidebar_state="expanded",
)

if not st.session_state.get("authenticated"):
    st.switch_page("pages/1_Authentication.py")

inject_design_system()
render_sidebar(active_item="Dashboard")
render_topbar(breadcrumb="Dashboard")

# --- Header ---
render_page_header("Manager Command Center", f"Welcome back, {CURRENT_USER['name']} — here's your pipeline health and team performance.")

# ── KPI Strip ────────────────────────────────────────────────
render_kpi_strip(KPI_METRICS[:4])
render_kpi_strip(KPI_METRICS[4:])

# --- Performance Charts ---
section_header("Performance & Pipeline", "Revenue trend and current pipeline distribution by stage.")

# Theme for Altair
def apply_sbi_theme():
    return {
        "config": {
            "background": "transparent",
            "view": {"stroke": "transparent"},
            "axis": {
                "domainColor": "#1A2233",
                "gridColor": "#1A2233",
                "tickColor": "#1A2233",
                "labelColor": "#A7B0C0",
                "titleColor": "#A7B0C0",
                "titleFont": "Inter",
                "labelFont": "Inter",
            },
            "legend": {
                "labelColor": "#A7B0C0",
                "titleColor": "#A7B0C0",
                "titleFont": "Inter",
                "labelFont": "Inter",
            },
            "title": {
                "color": "#F5F7FB",
                "subtitleColor": "#A7B0C0",
                "font": "Inter",
                "subtitleFont": "Inter",
            }
        }
    }
alt.themes.register("sbi_theme", apply_sbi_theme)
alt.themes.enable("sbi_theme")

col_c1, col_c2 = st.columns(2)
with col_c1:
    st.markdown("<div class='sbi-card'>", unsafe_allow_html=True)
    st.markdown("<div style='font-size: 14px; font-weight: 600; margin-bottom: 16px;'>Revenue Trend</div>", unsafe_allow_html=True)
    revenue_chart = (
        alt.Chart(alt.Data(values=REVENUE_TREND))
        .mark_area(
            line={'color': '#5EE7FF'},
            color=alt.Gradient(
                gradient='linear',
                stops=[alt.GradientStop(color='#5EE7FF', offset=0),
                       alt.GradientStop(color='rgba(94, 231, 255, 0)', offset=1)],
                x1=1, x2=1, y1=1, y2=0
            )
        )
        .encode(
            x=alt.X("month:N", title=None, axis=alt.Axis(labelAngle=0)),
            y=alt.Y("revenue:Q", title=None, axis=alt.Axis(format="~s")),
            tooltip=["month:N", "revenue:Q"]
        ).properties(height=240, width='container')
    )
    st.altair_chart(revenue_chart, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col_c2:
    st.markdown("<div class='sbi-card'>", unsafe_allow_html=True)
    st.markdown("<div style='font-size: 14px; font-weight: 600; margin-bottom: 16px;'>Pipeline by Stage</div>", unsafe_allow_html=True)
    pipeline_chart = (
        alt.Chart(alt.Data(values=PIPELINE_BY_STAGE))
        .mark_bar(color="#8B7CFF", cornerRadiusTopLeft=4, cornerRadiusTopRight=4)
        .encode(
            x=alt.X("stage:N", title=None, axis=alt.Axis(labelAngle=-45)),
            y=alt.Y("count:Q", title=None),
            tooltip=["stage:N", "count:Q"]
        ).properties(height=240, width='container')
    )
    st.altair_chart(pipeline_chart, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div style='height: 32px;'></div>", unsafe_allow_html=True)

# --- Needs Attention & Activity ---
section_header("Needs Attention", "Priority items requiring manager action today.")

col_n1, col_n2 = st.columns([1.5, 1])

with col_n1:
    st.markdown("<div class='sbi-card' style='height: 100%;'>", unsafe_allow_html=True)
    st.markdown("<div style='font-size: 14px; font-weight: 600; margin-bottom: 16px;'>High Risk Deals</div>", unsafe_allow_html=True)
    
    table_html = """
    <div class='sbi-table-wrapper'>
        <table class='sbi-table'>
            <thead>
                <tr>
                    <th>Company</th>
                    <th>Value</th>
                    <th>Rep</th>
                    <th>Risk Score</th>
                </tr>
            </thead>
            <tbody>
    """
    for deal in HIGH_RISK_DEALS[:5]:
        table_html += f"""
                <tr>
                    <td style='font-weight: 600;'>{deal['company']}</td>
                    <td>{deal['deal_value']}</td>
                    <td>{deal['assigned_rep']}</td>
                    <td>{badge_html(f"{deal['risk_score']} - High Risk", "danger")}</td>
                </tr>
        """
    table_html += "</tbody></table></div>"
    st.markdown(table_html, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col_n2:
    ai_content = ""
    for idx, coach in enumerate(COACHING_SUGGESTIONS[:3]):
        border_style = '' if idx == 2 else '1px solid rgba(139,124,255,0.1)'
        ai_content += f"""
        <div style="margin-top: 16px; padding-bottom: 16px; border-bottom: {border_style};">
            <div style="font-weight: 600; font-size: 14px; margin-bottom: 4px;">{coach['rep']}</div>
            <div class="sbi-text-xs sbi-text-secondary" style="margin-bottom: 8px;">{coach['problem']}</div>
            <div class="sbi-text-xs" style="color: var(--sbi-text-primary); border-left: 2px solid var(--sbi-violet); padding-left: 8px;">{coach['suggestion']}</div>
        </div>
        """
    render_ai_panel("AI Coaching Priority", ai_content, style="height: 100%;")

st.markdown("<div style='height: 32px;'></div>", unsafe_allow_html=True)

# --- Bottom Section: Reps & Activity ---
col_b1, col_b2 = st.columns([1, 1.5])

with col_b1:
    section_header("Top Performers", "Ranked by behavior score.")
    st.markdown("<div class='sbi-card'>", unsafe_allow_html=True)
    
    for idx, rep in enumerate(TOP_REPS[:4]):
        st.markdown(
            f"""
            <div style="display: flex; align-items: center; justify-content: space-between; padding: 12px 0; border-bottom: {'' if idx==3 else '1px solid var(--sbi-border-subtle)'};">
                <div style="display: flex; align-items: center; gap: 12px;">
                    <div style="width: 32px; height: 32px; border-radius: 6px; background: rgba(94,231,255,0.1); color: var(--sbi-cyan); display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 12px;">#{rep['rank']}</div>
                    <div>
                        <div style="font-size: 14px; font-weight: 600;">{rep['name']}</div>
                        <div class="sbi-text-xs sbi-text-muted">Score: {rep['behavior_score']}</div>
                    </div>
                </div>
                <div style="text-align: right;">
                    <div style="font-size: 13px; font-weight: 600;">{rep['win_rate']}</div>
                    <div class="sbi-text-xs sbi-text-muted">Win Rate</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    st.markdown("</div>", unsafe_allow_html=True)

with col_b2:
    section_header("Recent Activity", "Latest pipeline updates from your team.")
    st.markdown("<div class='sbi-card'>", unsafe_allow_html=True)
    
    for idx, act in enumerate(RECENT_ACTIVITIES[:4]):
        st.markdown(
            f"""
            <div style="display: flex; gap: 16px; padding: 12px 0; border-bottom: {'' if idx==3 else '1px solid var(--sbi-border-subtle)'};">
                <div style="color: var(--sbi-text-muted); font-size: 12px; width: 60px; flex-shrink: 0; padding-top: 2px;">{act['time']}</div>
                <div>
                    <div style="font-size: 13px; font-weight: 600; margin-bottom: 2px;">{act['title']}</div>
                    <div class="sbi-text-xs sbi-text-secondary">{act['detail']}</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    st.markdown("</div>", unsafe_allow_html=True)
