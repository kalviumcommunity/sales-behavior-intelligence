import streamlit as st

from frontend.design_system import inject_design_system
from frontend.components.app_shell import render_sidebar, render_topbar, render_page_header
from frontend.components.ui_components import render_kpi_strip, badge_html, render_empty_state
from frontend.deals_data import DEALS

st.set_page_config(
    page_title="Deals | Sales Behavior Intelligence",
    page_icon="◆",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Authentication Check
if not st.session_state.get("authenticated"):
    st.switch_page("pages/1_Authentication.py")

inject_design_system()
render_sidebar(active_item="Deals")
render_topbar(breadcrumb="Deals", actions_html="")

# --- Data Computation ---
total_pipeline = sum(d['amount'] for d in DEALS if d['stage'] != 'Closed Lost')
open_deals = len([d for d in DEALS if d['stage'] not in ['Closed Won', 'Closed Lost']])
at_risk_deals = len([d for d in DEALS if d['risk_level'] == 'High'])
avg_deal_value = total_pipeline / max(open_deals, 1)

# --- Header & Metrics ---
actions = """
<button class='sbi-btn-secondary' style='height: 36px; padding: 0 16px; font-size: 13px;'>Export</button>
<button class='sbi-btn-primary' style='height: 36px; padding: 0 16px; font-size: 13px;'>+ Add Deal</button>
"""
render_page_header(
    "Deals", 
    "Monitor every opportunity and the behaviors influencing progression.", 
    header_actions=actions
)

kpi_metrics = [
    {"label": "Total Pipeline", "value": f"${total_pipeline:,.0f}", "detail": ""},
    {"label": "Open Deals", "value": f"{open_deals}", "detail": ""},
    {"label": "At-Risk Deals", "value": f"{at_risk_deals}", "detail": "High Priority", "trend": "down"},
    {"label": "Avg Deal Value", "value": f"${avg_deal_value:,.0f}", "detail": ""},
]
render_kpi_strip(kpi_metrics)

# --- Filter Toolbar ---
fc1, fc2, fc3, fc4, fc5, fc6 = st.columns([2, 1, 1, 1, 1, 1])
search = fc1.text_input("Search", placeholder="Search deals or companies...", label_visibility="collapsed")
stage_filter = fc2.selectbox("Stage", ["All Stages", "Discovery", "Qualification", "Proposal", "Negotiation", "Contract"], label_visibility="collapsed")
risk_filter = fc3.selectbox("Risk", ["All Risk", "Low", "Medium", "High"], label_visibility="collapsed")
rep_filter = fc4.selectbox("Rep", ["All Reps", "Maya Lin", "Alex Rivera", "Jordan Smith"], label_visibility="collapsed")

# --- Filter Application ---
filtered_deals = DEALS
if search:
    filtered_deals = [d for d in filtered_deals if search.lower() in d['company'].lower() or search.lower() in d['deal_name'].lower()]
if stage_filter != "All Stages":
    filtered_deals = [d for d in filtered_deals if d['stage'] == stage_filter]
if risk_filter != "All Risk":
    filtered_deals = [d for d in filtered_deals if d['risk_level'] == risk_filter]
if rep_filter != "All Reps":
    filtered_deals = [d for d in filtered_deals if d['rep_name'] == rep_filter]

st.html(f"<div class='sbi-text-muted sbi-text-xs sbi-font-semibold' style='margin-bottom: 12px;'>Showing {len(filtered_deals)} deals</div>")

# --- Deal Table Header ---
st.html(
    """
    <div style="display: grid; grid-template-columns: 2.5fr 1fr 1fr 1.5fr 1fr 2fr 0.8fr; gap: 12px; padding: 12px 16px; border-bottom: 1px solid var(--sbi-border-subtle); color: var(--sbi-text-muted); font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em;">
        <div>Deal</div>
        <div>Value</div>
        <div>Stage</div>
        <div>Health / Risk</div>
        <div>Rep</div>
        <div>AI Signal</div>
        <div style="text-align: right;">Action</div>
    </div>
    """)

# --- Deal Table Rows ---
for deal in filtered_deals:
    
    # Badge resolution
    stage_badge_class = "info"
    if deal['stage'] == "Closed Won": stage_badge_class = "success"
    elif deal['stage'] == "Closed Lost": stage_badge_class = "danger"
    elif deal['stage'] in ["Negotiation", "Contract"]: stage_badge_class = "warning"
    
    risk_color = "var(--sbi-success)"
    if deal['risk_level'] == "High": risk_color = "var(--sbi-danger)"
    elif deal['risk_level'] == "Medium": risk_color = "var(--sbi-warning)"

    row_html = f"""
    <div style="display: grid; grid-template-columns: 2.5fr 1fr 1fr 1.5fr 1fr 2fr; gap: 12px; padding: 16px 16px 16px 0; align-items: center;">
        <div>
            <div class="sbi-font-bold" style="font-size: 14px; margin-bottom: 2px; color: var(--sbi-text-primary);">{deal['deal_name']}</div>
            <div class="sbi-text-secondary sbi-text-xs">{deal['company']}</div>
        </div>
        <div class="sbi-font-semibold" style="font-size: 14px; color: var(--sbi-text-primary);">${deal['amount']:,.0f}</div>
        <div>{badge_html(deal['stage'], stage_badge_class)}</div>
        <div>
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 4px; font-size: 12px;">
                <span class="sbi-font-bold" style="color: {risk_color}">{deal['risk_score']}/100</span>
                <span class="sbi-text-muted sbi-text-xs">{deal['risk_level']} Risk</span>
            </div>
            <div style="height: 4px; background: var(--sbi-border-subtle); border-radius: 2px; overflow: hidden;">
                <div style="height: 100%; width: {deal['risk_score']}%; background: {risk_color}; border-radius: 2px;"></div>
            </div>
        </div>
        <div style="font-size: 13px; color: var(--sbi-text-primary);">{deal['rep_name']}</div>
        <div>
            <div class="sbi-ai-label" style="margin-bottom: 2px;">AI Signal</div>
            <div class="sbi-text-secondary" style="font-size: 12px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">{deal['ai_signal']}</div>
        </div>
    </div>
    """

    col_content, col_action = st.columns([9, 1])
    with col_content:
        st.html(row_html)
    with col_action:
        # Align button vertically
        st.html("<div style='height: 24px;'></div>")
        if st.button("Open →", key=f"open_{deal['id']}", use_container_width=True, type="secondary"):
            st.session_state["deals_selected_deal"] = {"id": deal["id"]}
            st.switch_page("pages/3_Deal_Details.py")
    
    st.html("<div style='height: 1px; background: var(--sbi-border-subtle); margin: 0;'></div>")

if not filtered_deals:
    render_empty_state("No deals found", "Try adjusting your filters to see more results.")
