"""
Deal Deep Dive View (Tab 2).
Provides deal selector, risk score header, activity timeline, and evidence-backed coaching cards.
"""
import streamlit as st

from frontend.components.coaching_cards import render_coaching_cards
from frontend.components.timeline import render_deal_timeline


def render_deal_deep_dive(deals, timelines, coaching_cards_data):
    """Renders detailed view for inspecting a specific deal."""
    st.markdown("### 🔍 Opportunity Deep Dive & Behavioral Inspection")
    st.caption("Inspect seller behaviors, interaction sequences, and evidence-based recommendations.")

    # Deal Selector Dropdown
    deal_options = {d["id"]: f"{d['name']} — ${d['amount']:,.0f} ({d['risk_level']} Risk)" for d in deals}
    selected_deal_id = st.selectbox("Select Opportunity to Inspect", options=list(deal_options.keys()), format_func=lambda x: deal_options[x])

    selected_deal = next(d for d in deals if d["id"] == selected_deal_id)

    # Deal Summary Card Header
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Deal Amount", f"${selected_deal['amount']:,.0f}")
    with col2:
        st.metric("Current Stage", selected_deal['stage'], f"{selected_deal['days_in_stage']} days")
    with col3:
        st.metric("Deal Owner", selected_deal['rep_name'])
    with col4:
        st.metric("Risk Score", f"{selected_deal['risk_score']} / 100", delta=selected_deal['risk_level'], delta_color="inverse")

    st.markdown("---")

    # Main Split View: Timeline (Left) & Coaching Cards (Right)
    left_col, right_col = st.columns([1, 1])

    with left_col:
        events = timelines.get(selected_deal_id, [])
        render_deal_timeline(events)

    with right_col:
        cards = coaching_cards_data.get(selected_deal_id, [])
        render_coaching_cards(cards)
