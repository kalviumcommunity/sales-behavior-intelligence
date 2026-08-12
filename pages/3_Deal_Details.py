"""Deal Details Page - Shows everything a sales manager needs to understand one deal."""
import streamlit as st

from frontend.components.sidebar import render_sidebar
from frontend.components.deal_header import render_deal_header
from frontend.components.deal_health import render_deal_health
from frontend.components.ai_summary import render_ai_summary
from frontend.components.deal_metrics import render_deal_metrics
from frontend.components.deal_timeline_visual import render_deal_timeline
from frontend.components.behavioral_signals import render_behavioral_signals
from frontend.components.stakeholders_view import render_stakeholders
from frontend.components.activity_tabs import render_activity_tabs
from frontend.components.risk_analysis import render_risk_analysis
from frontend.components.coaching_recommendation import render_coaching_recommendation
from frontend.components.next_best_action import render_next_best_action
from frontend.components.deal_stage_progress import render_deal_stage_progress

from frontend.deal_details_data import (
    get_deal_details,
    get_deal_health_metrics,
    get_ai_summary,
    get_behavioral_signals,
    get_stakeholders,
    get_deal_timeline,
    get_activity_sections,
    get_risk_factors,
    get_coaching_recommendation,
    get_next_best_action,
    get_deal_stages,
)


st.set_page_config(
    page_title="Deal Details | Sales Behavior Intelligence",
    page_icon="◪",
    layout="wide",
    initial_sidebar_state="expanded",
)

if not st.session_state.get("authenticated"):
    st.switch_page("pages/1_Authentication.py")

# Get deal ID from session state or default
deal_id = st.session_state.get("deals_selected_deal", {}).get("id", "deal_201")

# Load all data
deal = get_deal_details(deal_id)
health_metrics = get_deal_health_metrics(deal_id)
ai_data = get_ai_summary(deal_id)
signals = get_behavioral_signals(deal_id)
stakeholders = get_stakeholders(deal_id)
timeline_events = get_deal_timeline(deal_id)
activity_data = get_activity_sections(deal_id)
risk_factors = get_risk_factors(deal_id)
coaching_data = get_coaching_recommendation(deal_id)
nba_data = get_next_best_action(deal_id)
stages = get_deal_stages()

# Apply global styles
st.markdown(
    """
    <style>
    :root {
        --bg: #06101d;
        --panel: rgba(11, 18, 32, 0.82);
        --panel-strong: rgba(13, 21, 37, 0.92);
        --panel-border: rgba(148, 163, 184, 0.15);
        --text: #edf4ff;
        --muted: #93a4bd;
        --cyan: #57d8ff;
        --violet: #9a86ff;
        --blue: #7ab8ff;
        --green: #59d19b;
        --orange: #ffb76a;
        --rose: #ff8ea7;
    }

    .stApp {
        background:
            radial-gradient(circle at 0% 0%, rgba(87, 216, 255, 0.14), transparent 28%),
            radial-gradient(circle at 100% 0%, rgba(154, 134, 255, 0.16), transparent 24%),
            linear-gradient(180deg, #040812 0%, #0a1220 48%, #05070d 100%);
        color: var(--text);
    }

    .main .block-container {
        padding-top: 1rem;
        padding-bottom: 2.2rem;
        max-width: 1520px;
    }

    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, rgba(7, 11, 20, 0.98), rgba(11, 16, 30, 0.96));
        border-right: 1px solid rgba(148, 163, 184, 0.1);
    }

    h1, h2, h3, h4, p, span, div, li, label {
        color: var(--text);
    }

    /* Deal Header Styles */
    .deal-header-info {
        padding: 8px 0;
    }

    .deal-header__company {
        font-size: 0.88rem;
        color: var(--muted);
        text-transform: uppercase;
        letter-spacing: 0.12em;
        margin-bottom: 6px;
    }

    .deal-header__name {
        font-size: 1.85rem;
        font-weight: 800;
        letter-spacing: -0.03em;
        line-height: 1.1;
    }

    .deal-key-info {
        padding: 12px;
        background: rgba(255, 255, 255, 0.04);
        border: 1px solid rgba(148, 163, 184, 0.12);
        border-radius: 12px;
        text-align: center;
    }

    .deal-key-info__label {
        font-size: 0.72rem;
        color: var(--muted);
        text-transform: uppercase;
        letter-spacing: 0.14em;
        margin-bottom: 4px;
        display: block;
    }

    .deal-key-info__value {
        font-size: 1rem;
        font-weight: 700;
        color: var(--text);
    }

    /* Deal Health Styles */
    .deal-health-card {
        padding: 16px;
        background: rgba(255, 255, 255, 0.02);
        border: 1px solid rgba(148, 163, 184, 0.12);
        border-radius: 14px;
        display: flex;
        flex-direction: column;
        gap: 10px;
    }

    .deal-health__label {
        font-size: 0.72rem;
        color: var(--muted);
        text-transform: uppercase;
        letter-spacing: 0.14em;
    }

    .deal-health__score,
    .deal-health__value {
        font-size: 1.35rem;
        font-weight: 800;
        letter-spacing: -0.02em;
    }

    .deal-health__bar {
        height: 8px;
        background: rgba(255, 255, 255, 0.05);
        border-radius: 999px;
        overflow: hidden;
    }

    .deal-health__progress {
        height: 100%;
        border-radius: inherit;
        transition: width 0.3s ease;
    }

    .deal-health__meta,
    .deal-health__trend {
        font-size: 0.85rem;
        line-height: 1.4;
    }

    /* AI Summary Styles */
    .ai-summary-card {
        padding: 20px;
        background: linear-gradient(135deg, rgba(87, 216, 255, 0.08), rgba(154, 134, 255, 0.08));
        border: 1px solid rgba(87, 216, 255, 0.18);
        border-radius: 16px;
        margin-bottom: 20px;
    }

    .ai-summary__header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 12px;
    }

    .ai-summary__title {
        font-size: 1.05rem;
        font-weight: 700;
    }

    .ai-summary__confidence {
        font-size: 0.85rem;
        color: var(--muted);
    }

    .ai-summary__content {
        margin-bottom: 14px;
    }

    .ai-summary__content p {
        margin: 0;
        line-height: 1.6;
        color: var(--text);
    }

    .ai-summary__signals-label {
        font-size: 0.75rem;
        color: var(--muted);
        text-transform: uppercase;
        letter-spacing: 0.14em;
        margin-bottom: 8px;
        display: block;
    }

    .ai-summary__signals-list {
        list-style: none;
        margin: 0;
        padding: 0;
        display: grid;
        gap: 8px;
    }

    .ai-summary__signals-list li {
        padding: 8px 12px;
        background: rgba(255, 255, 255, 0.04);
        border-left: 3px solid var(--cyan);
        border-radius: 6px;
        font-size: 0.92rem;
    }

    /* Section Heading */
    .section-heading {
        font-size: 1.15rem;
        font-weight: 700;
        margin: 28px 0 16px 0;
        letter-spacing: -0.01em;
    }

    /* Deal Metrics */
    .deal-metric-card {
        padding: 14px;
        background: rgba(255, 255, 255, 0.02);
        border: 1px solid rgba(148, 163, 184, 0.12);
        border-radius: 12px;
        text-align: center;
    }

    .deal-metric__label {
        display: block;
        font-size: 0.72rem;
        color: var(--muted);
        text-transform: uppercase;
        letter-spacing: 0.14em;
        margin-bottom: 6px;
    }

    .deal-metric__value {
        display: block;
        font-size: 1.1rem;
        font-weight: 700;
        color: var(--text);
    }

    /* Behavioral Signal Styles */
    .behavioral-signal-card {
        padding: 16px;
        background: rgba(255, 255, 255, 0.02);
        border: 1px solid rgba(148, 163, 184, 0.12);
        border-radius: 14px;
        margin-bottom: 12px;
    }

    .behavioral-signal__header {
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        margin-bottom: 12px;
    }

    .behavioral-signal__name {
        font-size: 1rem;
        font-weight: 700;
    }

    .behavioral-signal__score {
        font-size: 1rem;
        font-weight: 700;
    }

    .behavioral-signal__number {
        font-weight: 800;
    }

    .behavioral-signal__bar {
        height: 8px;
        background: rgba(255, 255, 255, 0.05);
        border-radius: 999px;
        overflow: hidden;
        margin-bottom: 10px;
    }

    .behavioral-signal__progress {
        height: 100%;
        border-radius: inherit;
        transition: width 0.3s ease;
    }

    .behavioral-signal__insight {
        font-size: 0.92rem;
        line-height: 1.6;
        color: var(--text);
    }

    /* Stakeholder Styles */
    .warning-banner {
        padding: 12px 14px;
        background: rgba(255, 142, 167, 0.12);
        border: 1px solid rgba(255, 142, 167, 0.24);
        border-radius: 12px;
        color: #ffadb9;
        font-size: 0.92rem;
        line-height: 1.5;
        margin-bottom: 14px;
    }

    .stakeholder-card {
        padding: 16px;
        background: rgba(255, 255, 255, 0.02);
        border: 1px solid rgba(148, 163, 184, 0.12);
        border-radius: 14px;
        margin-bottom: 12px;
    }

    .stakeholder__header {
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        margin-bottom: 12px;
    }

    .stakeholder__info {
        flex: 1;
    }

    .stakeholder__name {
        font-size: 1rem;
        font-weight: 700;
        margin-bottom: 4px;
    }

    .stakeholder__title {
        font-size: 0.88rem;
        color: var(--muted);
    }

    .thread-badge {
        display: inline-block;
        padding: 6px 10px;
        border-radius: 6px;
        font-size: 0.75rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.08em;
    }

    .thread-badge--primary {
        background: rgba(87, 216, 255, 0.18);
        color: #57d8ff;
    }

    .thread-badge--secondary {
        background: rgba(154, 134, 255, 0.18);
        color: #9a86ff;
    }

    .thread-badge--not-engaged {
        background: rgba(255, 142, 167, 0.18);
        color: #ffadb9;
    }

    .stakeholder__grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 12px;
    }

    .stakeholder__field {
        padding: 10px 12px;
        background: rgba(255, 255, 255, 0.02);
        border-radius: 10px;
    }

    .stakeholder__label {
        display: block;
        font-size: 0.72rem;
        color: var(--muted);
        text-transform: uppercase;
        letter-spacing: 0.12em;
        margin-bottom: 4px;
    }

    .stakeholder__value {
        display: block;
        font-size: 0.92rem;
        font-weight: 600;
    }

    /* Timeline Styles */
    .timeline-event {
        display: flex;
        gap: 14px;
        padding: 14px 0;
        border-bottom: 1px solid rgba(148, 163, 184, 0.1);
    }

    .timeline-event:last-child {
        border-bottom: none;
    }

    .timeline-event__icon {
        width: 40px;
        height: 40px;
        min-width: 40px;
        display: flex;
        align-items: center;
        justify-content: center;
        border: 2px solid;
        border-radius: 12px;
        font-size: 1.1rem;
    }

    .timeline-event__content {
        flex: 1;
        padding-top: 2px;
    }

    .timeline-event__date-type {
        display: flex;
        gap: 12px;
        margin-bottom: 4px;
    }

    .timeline-event__date {
        font-size: 0.85rem;
        font-weight: 700;
        color: var(--text);
    }

    .timeline-event__type {
        font-size: 0.75rem;
        color: var(--muted);
        text-transform: uppercase;
        letter-spacing: 0.08em;
    }

    .timeline-event__title {
        font-size: 1rem;
        font-weight: 700;
        margin-bottom: 4px;
    }

    .timeline-event__description {
        font-size: 0.92rem;
        color: var(--text);
        line-height: 1.5;
    }

    .timeline-event__person {
        font-size: 0.85rem;
        color: var(--muted);
        margin-top: 6px;
    }

    /* Activity Styles */
    .activity-count {
        font-size: 0.85rem;
        color: var(--muted);
        margin-bottom: 12px;
    }

    .activity-card {
        padding: 14px;
        background: rgba(255, 255, 255, 0.02);
        border: 1px solid rgba(148, 163, 184, 0.12);
        border-radius: 12px;
        margin-bottom: 10px;
    }

    .activity-card__header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 8px;
    }

    .activity-card__sender,
    .activity-card__title,
    .activity-card__author {
        font-size: 0.95rem;
        font-weight: 700;
    }

    .activity-card__status {
        font-size: 0.78rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.08em;
    }

    .activity-card__subject,
    .activity-card__content {
        font-size: 0.92rem;
        color: var(--text);
        margin-bottom: 8px;
        line-height: 1.5;
    }

    .activity-card__participants,
    .activity-card__summary,
    .activity-card__outcome {
        font-size: 0.88rem;
        color: var(--text);
        margin-bottom: 4px;
        line-height: 1.5;
    }

    .activity-card__time,
    .activity-card__date,
    .activity-card__meta {
        font-size: 0.78rem;
        color: var(--muted);
    }

    /* Risk Analysis Styles */
    .risk-card {
        padding: 16px;
        background: rgba(255, 255, 255, 0.02);
        border: 1px solid rgba(148, 163, 184, 0.12);
        border-radius: 14px;
        margin-bottom: 12px;
    }

    .risk-card__header {
        display: flex;
        gap: 12px;
        margin-bottom: 10px;
    }

    .risk-card__severity {
        font-size: 0.75rem;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 0.12em;
        white-space: nowrap;
    }

    .risk-card__title {
        font-size: 1rem;
        font-weight: 700;
        flex: 1;
    }

    .risk-card__content {
        margin-bottom: 10px;
    }

    .risk-card__description {
        font-size: 0.92rem;
        line-height: 1.6;
        color: var(--text);
    }

    .risk-card__footer {
        display: grid;
        gap: 10px;
    }

    .risk-card__section {
        padding: 10px 12px;
        background: rgba(255, 255, 255, 0.02);
        border-radius: 10px;
    }

    .risk-card__section-label {
        font-size: 0.75rem;
        color: var(--muted);
        text-transform: uppercase;
        letter-spacing: 0.12em;
        margin-bottom: 4px;
        display: block;
    }

    .risk-card__section-value {
        font-size: 0.92rem;
        line-height: 1.5;
    }

    /* Coaching Recommendation Styles */
    .coaching-card {
        padding: 20px;
        background: linear-gradient(135deg, rgba(154, 134, 255, 0.08), rgba(87, 216, 255, 0.08));
        border: 1px solid rgba(154, 134, 255, 0.18);
        border-radius: 16px;
        margin-bottom: 20px;
    }

    .coaching-card__header {
        display: flex;
        gap: 12px;
        align-items: flex-start;
        margin-bottom: 14px;
    }

    .coaching-card__icon {
        font-size: 1.5rem;
    }

    .coaching-card__title {
        font-size: 0.88rem;
        font-weight: 700;
        color: var(--muted);
        text-transform: uppercase;
        letter-spacing: 0.12em;
    }

    .coaching-card__confidence {
        font-size: 0.78rem;
        color: var(--cyan);
        font-weight: 700;
    }

    .coaching-card__main-title {
        font-size: 1.2rem;
        font-weight: 800;
        margin-bottom: 16px;
        letter-spacing: -0.01em;
    }

    .coaching-card__section {
        margin-bottom: 14px;
    }

    .coaching-card__section-label {
        display: block;
        font-size: 0.75rem;
        color: var(--muted);
        text-transform: uppercase;
        letter-spacing: 0.12em;
        margin-bottom: 6px;
        font-weight: 700;
    }

    .coaching-card__section-value {
        font-size: 0.92rem;
        line-height: 1.6;
    }

    /* Next Best Action Styles */
    .nba-card {
        padding: 20px;
        background: linear-gradient(135deg, rgba(87, 216, 255, 0.12), rgba(89, 209, 155, 0.08));
        border: 1px solid rgba(87, 216, 255, 0.24);
        border-radius: 16px;
        margin-bottom: 20px;
    }

    .nba-card__label {
        font-size: 0.7rem;
        color: var(--cyan);
        text-transform: uppercase;
        letter-spacing: 0.16em;
        font-weight: 800;
        margin-bottom: 6px;
        display: block;
    }

    .nba-card__title {
        font-size: 1.35rem;
        font-weight: 800;
        margin-bottom: 16px;
        letter-spacing: -0.02em;
    }

    .nba-card__grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 12px;
        margin-bottom: 16px;
    }

    .nba-card__field {
        display: flex;
        flex-direction: column;
        gap: 6px;
    }

    .nba-card__field-label {
        font-size: 0.72rem;
        color: var(--muted);
        text-transform: uppercase;
        letter-spacing: 0.12em;
        display: block;
    }

    .nba-card__field-value {
        font-size: 1rem;
        font-weight: 700;
    }

    .nba-card__details {
        padding: 12px;
        background: rgba(255, 255, 255, 0.04);
        border-radius: 10px;
        font-size: 0.92rem;
        line-height: 1.6;
    }

    /* Stage Progression Styles */
    .stage-progression {
        display: flex;
        flex-direction: column;
        gap: 0;
        align-items: center;
    }

    .stage-item {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 6px;
        padding: 12px 20px;
        min-width: 120px;
        position: relative;
    }

    .stage-item__icon {
        width: 36px;
        height: 36px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 50%;
        font-size: 1rem;
        font-weight: 800;
        border: 2px solid rgba(148, 163, 184, 0.2);
        background: rgba(255, 255, 255, 0.02);
    }

    .stage-item--completed .stage-item__icon {
        background: rgba(89, 209, 155, 0.12);
        border-color: rgba(89, 209, 155, 0.3);
        color: #59d19b;
    }

    .stage-item--current .stage-item__icon {
        background: rgba(87, 216, 255, 0.12);
        border-color: rgba(87, 216, 255, 0.3);
        color: #57d8ff;
    }

    .stage-item__name {
        font-size: 0.92rem;
        font-weight: 700;
        text-align: center;
    }

    .stage-item--completed .stage-item__name {
        color: #59d19b;
    }

    .stage-item--current .stage-item__name {
        color: #57d8ff;
    }

    .stage-item__arrow {
        font-size: 1.2rem;
        color: rgba(148, 163, 184, 0.3);
        margin: 4px 0;
    }

    /* Responsive */
    @media (max-width: 1200px) {
        .stakeholder__grid,
        .nba-card__grid {
            grid-template-columns: repeat(2, 1fr);
        }
    }

    @media (max-width: 768px) {
        .main .block-container {
            padding-left: 16px;
            padding-right: 16px;
        }

        .deal-header__name {
            font-size: 1.45rem;
        }

        .stakeholder__grid {
            grid-template-columns: 1fr;
        }

        .nba-card__grid {
            grid-template-columns: repeat(2, 1fr);
        }
    }

    .stTabs [data-baseweb="tab-list"] {
        background: none;
        border-bottom: 1px solid rgba(148, 163, 184, 0.1);
    }

    .stTabs [data-baseweb="tab"] {
        background: none;
        border: none;
        color: var(--muted);
    }

    .stTabs [aria-selected="true"] {
        color: var(--cyan) !important;
        border-bottom: 2px solid var(--cyan) !important;
    }

    .stButton button {
        background: transparent !important;
        border: 1px solid rgba(148, 163, 184, 0.2) !important;
        color: var(--text) !important;
        border-radius: 10px !important;
        font-weight: 700;
        padding: 0.6rem 1rem !important;
        transition: all 0.2s ease !important;
    }

    .stButton button:hover {
        border-color: rgba(87, 216, 255, 0.4) !important;
        background: rgba(87, 216, 255, 0.08) !important;
    }

    div[data-testid="stVerticalBlockBorderWrapper"] {
        border: none !important;
        background: none !important;
        box-shadow: none !important;
        padding: 0 !important;
        margin: 0 !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Initialize session state
st.session_state.setdefault("dashboard_sidebar_collapsed", False)
st.session_state.setdefault("dashboard_active_item", "Deal Details")

# Sidebar
render_sidebar(collapsed=st.session_state.dashboard_sidebar_collapsed, active_item="Deals")

# Render page
render_deal_header(deal)

st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)

# Deal Health Section
render_deal_health(health_metrics)

st.markdown("<div style='height: 1.5rem;'></div>", unsafe_allow_html=True)

# AI Summary
render_ai_summary(ai_data)

# Deal Metrics
render_deal_metrics(deal)

st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)

# Two column layout for timeline and behavioral signals
col_left, col_right = st.columns([1.2, 1], gap="medium")

with col_left:
    render_deal_timeline(timeline_events)

with col_right:
    render_behavioral_signals(signals)

st.markdown("<div style='height: 1.5rem;'></div>", unsafe_allow_html=True)

# Stakeholders
render_stakeholders(stakeholders)

st.markdown("<div style='height: 1.5rem;'></div>", unsafe_allow_html=True)

# Activity Tabs
render_activity_tabs(activity_data)

st.markdown("<div style='height: 1.5rem;'></div>", unsafe_allow_html=True)

# Risk Analysis
render_risk_analysis(risk_factors)

st.markdown("<div style='height: 1.5rem;'></div>", unsafe_allow_html=True)

# Coaching Recommendation
render_coaching_recommendation(coaching_data)

# Next Best Action (prominent positioning)
render_next_best_action(nba_data)

st.markdown("<div style='height: 1.5rem;'></div>", unsafe_allow_html=True)

# Deal Stage Progression
render_deal_stage_progress(stages)

st.markdown("<div style='height: 2rem;'></div>", unsafe_allow_html=True)
