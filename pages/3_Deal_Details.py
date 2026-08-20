import streamlit as st
from datetime import datetime

from frontend.design_system import inject_design_system
from frontend.components.app_shell import render_sidebar, render_topbar, render_page_header
from frontend.components.ui_components import render_kpi_strip, badge_html, section_header, render_ai_panel
from frontend.deal_details_data import (
    get_activity_sections,
    get_ai_summary,
    get_behavioral_signals,
    get_coaching_recommendation,
    get_deal_details,
    get_deal_health_metrics,
    get_deal_stages,
    get_deal_timeline,
    get_next_best_action,
    get_risk_factors,
    get_stakeholders,
)

st.set_page_config(
    page_title="Deal Details | Sales Behavior Intelligence",
    page_icon="◆",
    layout="wide",
    initial_sidebar_state="expanded",
)

if not st.session_state.get("authenticated"):
    st.switch_page("pages/1_Authentication.py")

inject_design_system()
render_sidebar(active_item="Deals")

# Get deal context
deal_id = st.session_state.get("deals_selected_deal", {}).get("id", "deal_201")
deal = get_deal_details(deal_id)
health = get_deal_health_metrics(deal_id)
ai_summary = get_ai_summary(deal_id)
signals = get_behavioral_signals(deal_id)
stakeholders = get_stakeholders(deal_id)
timeline = get_deal_timeline(deal_id)
activities = get_activity_sections(deal_id)
risks = get_risk_factors(deal_id)
next_action = get_next_best_action(deal_id)
stages = get_deal_stages()

render_topbar(breadcrumb=f"Deals / {deal['company']}")

# --- Header ---
header_actions = """
<button class='sbi-btn-secondary' style='height: 36px; padding: 0 16px; font-size: 13px;'>Share</button>
<button class='sbi-btn-primary' style='height: 36px; padding: 0 16px; font-size: 13px;'>Coach Rep</button>
"""
render_page_header(
    f"← Back to Deals", 
    "", 
    header_actions=""
)
# We recreate the header layout per prompt instructions
st.html(
    f"""
    <div style="margin-top: -24px; margin-bottom: 32px; display: flex; justify-content: space-between; align-items: flex-end;">
        <div>
            <div class="sbi-text-sm sbi-text-muted" style="margin-bottom: 4px;">Enterprise Platform Expansion</div>
            <div class="sbi-page-title" style="margin: 0;">{deal['company']}</div>
            <div class="sbi-text-secondary" style="margin-top: 4px;">Managed by <span class="sbi-text-primary sbi-font-semibold">{deal['assigned_rep']}</span></div>
        </div>
        <div style="display: flex; gap: 8px;">{header_actions}</div>
    </div>
    """)


# --- Stage Tracker ---
stage_html = "<div style='display: flex; gap: 8px; margin-bottom: 32px;'>"
for s in stages:
    color = "var(--sbi-cyan)" if s.get('completed') or s.get('current') else "var(--sbi-border-subtle)"
    bg = "var(--sbi-cyan-dim)" if s.get('completed') or s.get('current') else "var(--sbi-bg-hover)"
    weight = "700" if s.get('current') else "500"
    text_color = "var(--sbi-cyan)" if s.get('current') else ("var(--sbi-text-primary)" if s.get('completed') else "var(--sbi-text-muted)")
    
    stage_html += f"""
    <div style='flex: 1; padding: 12px; background: {bg}; border-left: 3px solid {color}; border-radius: 0 6px 6px 0; font-size: 13px; font-weight: {weight}; color: {text_color};'>
        {s['name']}
    </div>
    """
stage_html += "</div>"
st.html(stage_html)

# --- Top Row: AI Summary & Health ---
c_summary, c_health = st.columns([1.5, 1])

with c_summary:
    key_sigs = ''.join([badge_html(s, "neutral") for s in ai_summary['key_signals']])
    ai_html = f"""
        <div style="display: flex; justify-content: flex-end; align-items: flex-start; margin-bottom: 16px;">
            {badge_html(f"Confidence: {ai_summary['confidence']}%", "violet")}
        </div>
        <div style="font-size: 15px; line-height: 1.6; margin-bottom: 24px; color: var(--sbi-text-primary);">
            {ai_summary['summary']}
        </div>
        <div style="display: flex; flex-wrap: wrap; gap: 8px;">
            {key_sigs}
        </div>
        <div style="margin-top: 16px;">
            <button class="sbi-btn-secondary">View Evidence</button>
        </div>
    """
    render_ai_panel("AI Deal Summary", ai_html, style="height: 100%;")

with c_health:
    health_color = "var(--sbi-danger)" if health['risk_level'] == "High" else ("var(--sbi-warning)" if health['risk_level'] == "Medium" else "var(--sbi-success)")
    
    st.html(
        f"""
        <div class="sbi-card" style="height: 100%;">
            <div class="sbi-section-subtitle" style="margin-bottom: 16px; font-weight: 600;">Deal Health</div>
            <div style="display: flex; align-items: baseline; gap: 8px; margin-bottom: 4px;">
                <span style="font-size: 40px; font-weight: 800; color: {health_color}; line-height: 1;">{health['health_score']}</span>
                <span class="sbi-text-muted">/ {health['health_max']}</span>
            </div>
            <div class="sbi-text-sm sbi-font-semibold" style="margin-bottom: 24px;">{health['risk_level']} Risk</div>
            
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
                <div>
                    <div class="sbi-text-xs sbi-text-muted" style="text-transform: uppercase;">Value</div>
                    <div class="sbi-font-bold" style="font-size: 15px;">${deal['deal_value']:,.0f}</div>
                </div>
                <div>
                    <div class="sbi-text-xs sbi-text-muted" style="text-transform: uppercase;">Expected Close</div>
                    <div class="sbi-font-bold" style="font-size: 15px;">{deal['expected_close'].strftime('%b %d')}</div>
                </div>
                <div>
                    <div class="sbi-text-xs sbi-text-muted" style="text-transform: uppercase;">Velocity</div>
                    <div class="sbi-font-bold" style="font-size: 15px;">{health['deal_velocity']}</div>
                </div>
                <div>
                    <div class="sbi-text-xs sbi-text-muted" style="text-transform: uppercase;">Engagement</div>
                    <div class="sbi-font-bold" style="font-size: 15px;">{health['engagement']}</div>
                </div>
            </div>
        </div>
        """)

st.html("<div style='height: 32px;'></div>")

# --- Middle Row: Signals, Stakeholders, Next Action ---
c_signals, c_stakeholders = st.columns([1, 1.2])

with c_signals:
    section_header("Behavioral Signals")
    st.html("<div class='sbi-card'>")
    for idx, sig in enumerate(signals):
        sig_color = "var(--sbi-danger)" if sig['severity'] == "high" else ("var(--sbi-warning)" if sig['severity'] == "medium" else "var(--sbi-info)")
        st.html(
            f"""
            <div style="padding: 16px 0; border-bottom: {'' if idx==len(signals)-1 else '1px solid var(--sbi-border-subtle)'};">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <div style="font-weight: 600; font-size: 14px;">{sig['signal_name']}</div>
                    <div class="sbi-font-bold" style="color: {sig_color}; font-size: 13px;">{sig['score']}/100</div>
                </div>
                <div class="sbi-text-sm sbi-text-secondary">{sig['insight']}</div>
            </div>
            """)
    st.html("</div>")
    
    st.html("<div style='height: 24px;'></div>")
    
    section_header("Next Best Action")
    st.html(
        f"""
        <div class="sbi-card" style="border-left: 3px solid var(--sbi-cyan);">
            <div style="display: flex; justify-content: space-between; margin-bottom: 12px;">
                <div class="sbi-font-bold" style="font-size: 15px;">{next_action['action']}</div>
                {badge_html(f"Priority: {next_action['priority']}", "cyan")}
            </div>
            <div class="sbi-text-sm sbi-text-secondary" style="margin-bottom: 16px;">{next_action['details']}</div>
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div style="font-size: 12px; color: var(--sbi-text-muted);">Assignee: <span style="color: var(--sbi-text-primary); font-weight: 600;">{next_action['suggested_owner']}</span></div>
                <button class="sbi-btn-primary">Take Action</button>
            </div>
        </div>
        """)

with c_stakeholders:
    section_header("Stakeholders")
    table_html = """
    <div class='sbi-card sbi-table-wrapper' style="padding: 0; overflow: hidden;">
        <table class='sbi-table'>
            <thead>
                <tr>
                    <th>Contact</th>
                    <th>Role</th>
                    <th>Engagement</th>
                    <th>Last Interaction</th>
                </tr>
            </thead>
            <tbody>
    """
    for sh in stakeholders:
        eng_badge = "success" if sh['engagement_level'] == "High" else ("warning" if sh['engagement_level'] == "Medium" else "danger")
        table_html += f"""
                <tr>
                    <td>
                        <div class="sbi-font-semibold" style="font-size: 14px;">{sh['name']}</div>
                        <div class="sbi-text-xs sbi-text-secondary">{sh['job_title']}</div>
                    </td>
                    <td>{sh['role']}</td>
                    <td>{badge_html(sh['engagement_level'], eng_badge)}</td>
                    <td class="sbi-text-sm sbi-text-secondary">{sh['last_interaction']}</td>
                </tr>
        """
    table_html += "</tbody></table></div>"
    st.html(table_html)
    
    st.html("<div style='height: 24px;'></div>")
    
    section_header("Why this deal may slip")
    st.html("<div class='sbi-card'>")
    for idx, r in enumerate(risks[:2]): # Show top 2 risks to save space
        st.html(
            f"""
            <div style="padding: 12px 0; border-bottom: {'' if idx==1 else '1px solid var(--sbi-border-subtle)'};">
                <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 4px;">
                    {badge_html(r['severity'], "danger" if r['severity'] == "HIGH" else "warning")}
                    <span class="sbi-font-semibold" style="font-size: 14px;">{r['reason']}</span>
                </div>
                <div class="sbi-text-sm sbi-text-secondary" style="margin-left: 4px;">{r['description']}</div>
            </div>
            """)
    st.html("</div>")

st.html("<div style='height: 32px;'></div>")

# --- Bottom Row: Activity Feed ---
section_header("Activity Feed")
tab1, tab2, tab3 = st.tabs(["Timeline", "Emails", "Meetings"])

with tab1:
    st.html("<div class='sbi-card'>")
    for t in timeline[::-1]: # Reverse to show newest first
        st.html(
            f"""
            <div style="display: flex; gap: 16px; margin-bottom: 24px; position: relative;">
                <div style="width: 40px; flex-shrink: 0; text-align: right; padding-top: 4px;" class="sbi-text-xs sbi-text-muted">{t['date']}</div>
                <div style="width: 32px; height: 32px; border-radius: 50%; background: var(--sbi-bg-hover); border: 1px solid var(--sbi-border-subtle); display: flex; align-items: center; justify-content: center; flex-shrink: 0; z-index: 1;">{t['icon']}</div>
                <div>
                    <div class="sbi-font-bold" style="font-size: 14px; margin-bottom: 4px;">{t['title']}</div>
                    <div class="sbi-text-sm sbi-text-secondary">{t['description']}</div>
                    {f'<div class="sbi-text-xs" style="margin-top: 6px; color: var(--sbi-cyan);">👤 {t["related_person"]}</div>' if t["related_person"] else ''}
                </div>
            </div>
            """)
    st.html("</div>")

with tab2:
    st.html("<div class='sbi-card'>")
    for e in activities['emails']:
        st.html(
            f"""
            <div style="padding: 16px 0; border-bottom: 1px solid var(--sbi-border-subtle);">
                <div style="display: flex; justify-content: space-between; margin-bottom: 4px;">
                    <div class="sbi-font-semibold" style="font-size: 14px;">{e['subject']}</div>
                    <div class="sbi-text-xs sbi-text-muted">{e['time']}</div>
                </div>
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div class="sbi-text-sm sbi-text-secondary">From/To: {e['sender']}</div>
                    {badge_html(e['response_status'], "neutral")}
                </div>
            </div>
            """)
    st.html("</div>")

with tab3:
    st.html("<div class='sbi-card'>")
    for m in activities['meetings']:
        st.html(
            f"""
            <div style="padding: 16px 0; border-bottom: 1px solid var(--sbi-border-subtle);">
                <div style="display: flex; justify-content: space-between; margin-bottom: 8px;">
                    <div class="sbi-font-semibold" style="font-size: 14px;">{m['name']}</div>
                    <div class="sbi-text-xs sbi-text-muted">{m['date']}</div>
                </div>
                <div class="sbi-text-sm" style="margin-bottom: 8px;">Outcome: <span class="sbi-text-secondary">{m['outcome']}</span></div>
                <div class="sbi-text-xs sbi-text-muted">Participants: {', '.join(m['participants'])}</div>
            </div>
            """)
    st.html("</div>")
