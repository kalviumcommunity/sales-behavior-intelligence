"""
Admin Dashboard View
Contains the comprehensive pipeline, deal deep dive, and coaching features.
"""
import streamlit as st
from frontend.components.metrics import render_kpi_metrics
from frontend.views.pipeline_overview import render_pipeline_overview
from frontend.views.deal_deep_dive import render_deal_deep_dive
from frontend.views.rep_coaching import render_rep_coaching

def render_admin_dashboard(mock_reps, mock_deals, mock_timelines, mock_coaching_cards):
    # Global Top KPI Bar
    render_kpi_metrics(mock_deals)

    st.markdown("<br>", unsafe_allow_html=True)

    # Main Dashboard Navigation Tabs
    tab1, tab2, tab3 = st.tabs([
        "📊 Pipeline Risk Matrix",
        "🔍 Deal Deep Dive & Timeline",
        "👤 Rep Coaching & Analytics",
    ])

    with tab1:
        render_pipeline_overview(mock_deals)

    with tab2:
        render_deal_deep_dive(mock_deals, mock_timelines, mock_coaching_cards)

    with tab3:
        render_rep_coaching(mock_reps, mock_deals)
