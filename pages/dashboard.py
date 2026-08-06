import altair as alt
import streamlit as st

from frontend.components.activity_card import render_activity_card
from frontend.components.chart_card import render_chart_card
from frontend.components.coaching_card import render_coaching_card
from frontend.components.kpi_card import render_kpi_card
from frontend.components.meeting_table import render_meeting_table
from frontend.components.navbar import render_top_navbar
from frontend.components.quick_action_card import render_quick_action_card
from frontend.components.rep_card import render_rep_card
from frontend.components.risk_card import render_risk_card
from frontend.components.section_header import render_section_header
from frontend.components.sidebar import render_sidebar
from frontend.dashboard_data import (
    BREADCRUMB,
    COACHING_SUGGESTIONS,
    CURRENT_DATE,
    CURRENT_USER,
    DASHBOARD_NAV_ITEMS,
    HIGH_RISK_DEALS,
    KPI_METRICS,
    MONTHLY_PERFORMANCE,
    PIPELINE_BY_STAGE,
    QUICK_ACTIONS,
    RECENT_ACTIVITIES,
    REVENUE_TREND,
    RISK_DISTRIBUTION,
    TOP_REPS,
    UPCOMING_MEETINGS,
    WIN_LOSS_RATIO,
)


st.set_page_config(
    page_title="Manager Dashboard | Sales Behavior Intelligence",
    page_icon="◼",
    layout="wide",
    initial_sidebar_state="expanded",
)

if not st.session_state.get("authenticated"):
    st.switch_page("pages/1_Authentication.py")

st.session_state.setdefault("dashboard_sidebar_collapsed", False)
st.session_state.setdefault("dashboard_active_item", "Dashboard")

st.markdown(
    """
    <style>
    :root {
        --bg: #07111f;
        --bg-soft: #0b1628;
        --panel: rgba(10, 18, 32, 0.76);
        --panel-strong: rgba(13, 22, 38, 0.9);
        --panel-border: rgba(148, 163, 184, 0.16);
        --text: #edf4ff;
        --muted: #95a3bd;
        --cyan: #4fd7ff;
        --blue: #7ab8ff;
        --green: #53d09a;
        --violet: #9f86ff;
        --orange: #ffb76a;
        --rose: #ff7ea8;
        --gold: #f2cd6d;
    }

    .stApp {
        background:
            radial-gradient(circle at 0% 0%, rgba(79, 215, 255, 0.18), transparent 28%),
            radial-gradient(circle at 100% 0%, rgba(159, 134, 255, 0.16), transparent 24%),
            linear-gradient(180deg, #050913 0%, #0b1322 45%, #05070d 100%);
        color: var(--text);
    }

    .main .block-container {
        padding-top: 1rem;
        padding-bottom: 2.25rem;
        max-width: 1480px;
    }

    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, rgba(6, 11, 20, 0.98), rgba(9, 15, 26, 0.96));
        border-right: 1px solid rgba(148, 163, 184, 0.1);
    }

    h1, h2, h3, h4, p, span, div, li, label {
        color: var(--text);
    }

    .sidebar-shell,
    .sidebar-user-card,
    .sidebar-collapsed-card,
    .profile-chip,
    .kpi-card,
    .chart-card,
    .activity-card,
    .coaching-card,
    .risk-card,
    .rep-card,
    .meeting-table-wrap,
    .quick-action-card,
    .section-header {
        border: 1px solid var(--panel-border);
        background: var(--panel);
        border-radius: 22px;
        box-shadow: 0 20px 52px rgba(0, 0, 0, 0.26);
    }

    .sidebar-brand {
        display: flex;
        gap: 14px;
        align-items: center;
    }

    .sidebar-avatar,
    .profile-chip__avatar,
    .rep-card__avatar,
    .sidebar-collapsed-card {
        display: grid;
        place-items: center;
        border-radius: 18px;
        background: linear-gradient(135deg, rgba(79, 215, 255, 0.18), rgba(159, 134, 255, 0.18));
        border: 1px solid rgba(79, 215, 255, 0.18);
        color: var(--text);
        font-weight: 800;
    }

    .sidebar-avatar {
        width: 48px;
        height: 48px;
    }

    .sidebar-brand__eyebrow,
    .section-header__eyebrow,
    .kpi-label,
    .activity-card__time,
    .coaching-card__eyebrow,
    .risk-card__score,
    .rep-card__rank {
        color: var(--muted);
        text-transform: uppercase;
        letter-spacing: 0.14em;
        font-size: 0.72rem;
    }

    .sidebar-brand__title {
        font-size: 1rem;
        font-weight: 800;
    }

    .sidebar-user-card {
        display: flex;
        gap: 12px;
        align-items: center;
        padding: 14px;
    }

    .sidebar-user-card__avatar {
        width: 44px;
        height: 44px;
        border-radius: 16px;
        display: grid;
        place-items: center;
        background: linear-gradient(135deg, rgba(79, 215, 255, 0.22), rgba(159, 134, 255, 0.22));
        font-weight: 800;
    }

    .sidebar-user-card__name,
    .profile-chip__name,
    .rep-card__name,
    .coaching-card__rep,
    .risk-card__company {
        font-weight: 800;
    }

    .sidebar-user-card__role,
    .sidebar-user-card__meta,
    .profile-chip__meta,
    .profile-chip__theme,
    .kpi-detail,
    .activity-card__detail,
    .coaching-card__field span,
    .coaching-card__footer span,
    .risk-card__grid span,
    .risk-card__action span,
    .rep-card__grid span,
    .meeting-table th,
    .meeting-table td,
    .section-header p {
        color: var(--muted);
    }

    .profile-chip {
        display: flex;
        gap: 12px;
        align-items: center;
        padding: 14px 16px;
    }

    .profile-chip__avatar {
        width: 52px;
        height: 52px;
    }

    .profile-chip__theme {
        margin-top: 2px;
        font-size: 0.8rem;
    }

    .topnav-spacer {
        height: 1.7rem;
    }

    .breadcrumb {
        color: var(--muted);
        font-size: 0.86rem;
        margin-bottom: 0.4rem;
    }

    .stTextInput input,
    .stSelectbox div[data-baseweb="select"] > div,
    .stDateInput input,
    .stNumberInput input {
        background: rgba(255, 255, 255, 0.04) !important;
        color: var(--text) !important;
        border-color: rgba(148, 163, 184, 0.2) !important;
        border-radius: 16px !important;
    }

    .stButton button {
        border-radius: 16px;
        border: 1px solid rgba(148, 163, 184, 0.16);
        background: rgba(255, 255, 255, 0.04);
        color: var(--text);
        font-weight: 700;
        transition: transform 0.2s ease, border-color 0.2s ease;
    }

    .stButton button:hover {
        transform: translateY(-1px);
        border-color: rgba(79, 215, 255, 0.45);
    }

    .kpi-card,
    .chart-card,
    .activity-card,
    .coaching-card,
    .risk-card,
    .rep-card,
    .meeting-table-wrap,
    .quick-action-card,
    .section-header {
        padding: 18px;
    }

    .kpi-card {
        min-height: 132px;
        display: grid;
        gap: 8px;
        position: relative;
        overflow: hidden;
    }

    .kpi-card:before {
        content: "";
        position: absolute;
        inset: 0;
        background: linear-gradient(135deg, rgba(79, 215, 255, 0.08), transparent 45%, rgba(159, 134, 255, 0.08));
        pointer-events: none;
    }

    .kpi-value {
        font-size: 1.95rem;
        font-weight: 800;
        letter-spacing: -0.04em;
        line-height: 1.05;
    }

    .kpi-cyan { box-shadow: 0 0 0 1px rgba(79, 215, 255, 0.08) inset; }
    .kpi-blue { box-shadow: 0 0 0 1px rgba(122, 184, 255, 0.08) inset; }
    .kpi-green { box-shadow: 0 0 0 1px rgba(83, 208, 154, 0.08) inset; }
    .kpi-violet { box-shadow: 0 0 0 1px rgba(159, 134, 255, 0.08) inset; }
    .kpi-orange { box-shadow: 0 0 0 1px rgba(255, 183, 106, 0.08) inset; }
    .kpi-teal { box-shadow: 0 0 0 1px rgba(79, 215, 255, 0.08) inset; }
    .kpi-rose { box-shadow: 0 0 0 1px rgba(255, 126, 168, 0.08) inset; }
    .kpi-gold { box-shadow: 0 0 0 1px rgba(242, 205, 109, 0.08) inset; }

    .chart-card {
        min-height: 340px;
    }

    .activity-card,
    .coaching-card,
    .risk-card,
    .rep-card {
        display: grid;
        gap: 12px;
    }

    .activity-card__title {
        font-size: 1rem;
        font-weight: 800;
    }

    .coaching-card__field,
    .coaching-card__footer,
    .risk-card__header,
    .risk-card__grid,
    .rep-card__grid {
        display: grid;
        gap: 8px;
    }

    .coaching-card__field strong,
    .coaching-card__footer strong,
    .risk-card__action strong,
    .risk-card__grid strong,
    .rep-card__grid strong {
        color: var(--text);
        display: block;
    }

    .coaching-card__rep {
        font-size: 1.05rem;
    }

    .risk-card__header,
    .rep-card__header {
        display: flex;
        justify-content: space-between;
        gap: 12px;
        align-items: flex-start;
    }

    .risk-card__value {
        font-size: 1.25rem;
        font-weight: 800;
        margin-top: 4px;
    }

    .meeting-table {
        width: 100%;
        border-collapse: collapse;
    }

    .meeting-table th,
    .meeting-table td {
        text-align: left;
        padding: 12px 8px;
        border-bottom: 1px solid rgba(148, 163, 184, 0.12);
        font-size: 0.94rem;
    }

    .meeting-table th {
        font-size: 0.72rem;
        text-transform: uppercase;
        letter-spacing: 0.12em;
    }

    .quick-action-card {
        min-height: 136px;
    }

    .section-header h3 {
        margin: 0;
        font-size: 1.2rem;
        letter-spacing: -0.02em;
    }

    @media (max-width: 1100px) {
        .main .block-container {
            max-width: 100%;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

render_sidebar(collapsed=st.session_state.dashboard_sidebar_collapsed, active_item=st.session_state.dashboard_active_item)

search_query = render_top_navbar(
    search_value=st.session_state.get("dashboard_search", ""),
    breadcrumb=BREADCRUMB,
    current_date=CURRENT_DATE,
    notifications=3,
)

st.markdown(
    f"""
    <div class="section-header" style="margin-top: 0.75rem;">
        <div>
            <div class="section-header__eyebrow">Welcome back</div>
            <h3>{CURRENT_USER['name']} · {CURRENT_USER['role']}</h3>
            <p>Manager view for pipeline health, coaching signals, and rep performance.</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("<div style='height: 0.5rem;'></div>", unsafe_allow_html=True)

for row in [KPI_METRICS[:4], KPI_METRICS[4:]]:
    columns = st.columns(4)
    for column, metric in zip(columns, row):
        with column:
            render_kpi_card(metric["label"], metric["value"], metric["detail"], metric["accent"])
    st.markdown("<div style='height: 0.35rem;'></div>", unsafe_allow_html=True)

st.markdown("<div style='height: 0.6rem;'></div>", unsafe_allow_html=True)
render_section_header(
    "Performance Charts",
    "Mocked operational trends that summarize pipeline movement, risk, and execution quality.",
)

revenue_source = alt.Data(values=REVENUE_TREND)
pipeline_source = alt.Data(values=PIPELINE_BY_STAGE)
win_loss_source = alt.Data(values=WIN_LOSS_RATIO)
risk_source = alt.Data(values=RISK_DISTRIBUTION)
monthly_source = alt.Data(values=MONTHLY_PERFORMANCE)

revenue_trend_chart = (
    alt.Chart(revenue_source)
    .mark_line(point=True, strokeWidth=3)
    .encode(x=alt.X("month:N", title="Month"), y=alt.Y("revenue:Q", title="Revenue", axis=alt.Axis(format="$,.0f")), tooltip=["month:N", alt.Tooltip("revenue:Q", format="$,.0f")])
    .properties(height=240)
)

pipeline_chart = (
    alt.Chart(pipeline_source)
    .mark_bar(cornerRadiusTopLeft=10, cornerRadiusTopRight=10)
    .encode(x=alt.X("stage:N", title=None), y=alt.Y("count:Q", title="Deals"), color=alt.value("#7ab8ff"), tooltip=["stage:N", "count:Q"])
    .properties(height=240)
)

win_loss_chart = (
    alt.Chart(win_loss_source)
    .mark_arc(innerRadius=55)
    .encode(theta=alt.Theta("value:Q"), color=alt.Color("outcome:N", legend=alt.Legend(title=None)), tooltip=["outcome:N", "value:Q"])
    .properties(height=240)
)

risk_chart = (
    alt.Chart(risk_source)
    .mark_bar(cornerRadius=8)
    .encode(x=alt.X("bucket:N", title=None), y=alt.Y("value:Q", title="Deals"), color=alt.Color("bucket:N", legend=None), tooltip=["bucket:N", "value:Q"])
    .properties(height=240)
)

monthly_chart = (
    alt.Chart(monthly_source)
    .transform_fold(["pipeline", "win_rate", "coaching_completion"], as_=["metric", "value"])
    .mark_line(point=True)
    .encode(
        x=alt.X("month:N", title="Month"),
        y=alt.Y("value:Q", title="Score / Index"),
        color=alt.Color("metric:N", title=None),
        tooltip=["month:N", "metric:N", "value:Q"],
    )
    .properties(height=240)
)

chart_col1, chart_col2, chart_col3 = st.columns(3)
with chart_col1:
    render_chart_card("Revenue Trend", "Monthly revenue growth across the current selling motion.", revenue_trend_chart)
with chart_col2:
    render_chart_card("Pipeline by Stage", "Open opportunities distributed by their current funnel stage.", pipeline_chart)
with chart_col3:
    render_chart_card("Win/Loss Ratio", "High-level outcome split from the mock revenue book.", win_loss_chart)

chart_col4, chart_col5 = st.columns(2)
with chart_col4:
    render_chart_card("Risk Distribution", "Concentration of healthy, moderate, and high-risk opportunities.", risk_chart)
with chart_col5:
    render_chart_card("Monthly Performance", "Pipeline, win rate, and coaching completion moving together.", monthly_chart)

st.markdown("<div style='height: 0.55rem;'></div>", unsafe_allow_html=True)
left_col, right_col = st.columns([1.15, 0.95])
with left_col:
    render_section_header("Recent Activities", "A compact timeline of the most recent sales motions.")
    for activity in RECENT_ACTIVITIES:
        render_activity_card(activity["time"], activity["title"], activity["detail"], activity["icon"])
        st.markdown("<div style='height: 0.4rem;'></div>", unsafe_allow_html=True)

with right_col:
    render_section_header("High Risk Deals", "The opportunities that need direct manager intervention first.")
    for deal in HIGH_RISK_DEALS:
        if not search_query or search_query.lower() in deal["company"].lower() or search_query.lower() in deal["assigned_rep"].lower() or search_query.lower() in deal["stage"].lower():
            render_risk_card(
                deal["company"],
                deal["deal_value"],
                deal["risk_score"],
                deal["stage"],
                deal["assigned_rep"],
                deal["recommended_action"],
            )
            st.markdown("<div style='height: 0.35rem;'></div>", unsafe_allow_html=True)

st.markdown("<div style='height: 0.55rem;'></div>", unsafe_allow_html=True)
coaching_col, leaderboard_col = st.columns([1.05, 0.95])
with coaching_col:
    render_section_header("AI Coaching Suggestions", "Behavioral recommendations generated from the latest opportunity signals.")
    for suggestion in COACHING_SUGGESTIONS:
        if not search_query or search_query.lower() in suggestion["rep"].lower() or search_query.lower() in suggestion["problem"].lower():
            render_coaching_card(
                suggestion["rep"],
                suggestion["problem"],
                suggestion["suggestion"],
                suggestion["confidence"],
            )
            st.markdown("<div style='height: 0.35rem;'></div>", unsafe_allow_html=True)

with leaderboard_col:
    render_section_header("Top Performing Reps", "Small leaderboard for pipeline, win rate, and behavior score.")
    for rep in TOP_REPS:
        render_rep_card(rep["rank"], rep["avatar"], rep["name"], rep["pipeline"], rep["win_rate"], rep["behavior_score"])
        st.markdown("<div style='height: 0.35rem;'></div>", unsafe_allow_html=True)

st.markdown("<div style='height: 0.55rem;'></div>", unsafe_allow_html=True)
meeting_col, actions_col = st.columns([1.1, 0.9])
with meeting_col:
    render_section_header("Upcoming Meetings", "The next calendar checkpoints tied to active revenue work.")
    filtered_meetings = [
        meeting
        for meeting in UPCOMING_MEETINGS
        if not search_query or search_query.lower() in meeting["company"].lower() or search_query.lower() in meeting["rep"].lower() or search_query.lower() in meeting["stage"].lower()
    ]
    render_meeting_table(filtered_meetings)

with actions_col:
    render_section_header("Quick Actions", "Fast entry points for common manager workflows.")
    action_grid = st.columns(2)
    for index, action in enumerate(QUICK_ACTIONS):
        with action_grid[index % 2]:
            render_quick_action_card(action["label"], action["description"], action["icon"])

st.markdown(
    """
    <div class="section-header" style="margin-top: 0.8rem;">
        <div>
            <div class="section-header__eyebrow">Ready for the team</div>
            <h3>Dashboard scaffolding is in place.</h3>
            <p>Sidebar navigation, top navigation, KPI cards, charts, deal risk, coaching, reps, meetings, and quick actions are now wired into reusable components.</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)
