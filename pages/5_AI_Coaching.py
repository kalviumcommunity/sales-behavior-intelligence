import streamlit as st

from frontend.design_system import inject_design_system
from frontend.components.app_shell import render_sidebar, render_topbar, render_page_header
from frontend.components.ui_components import render_kpi_strip, badge_html, section_header, render_ai_panel
from frontend.dashboard_data import COACHING_SUGGESTIONS
from frontend.mock_data import MOCK_COACHING_CARDS

st.set_page_config(
    page_title="AI Coaching | Sales Behavior Intelligence",
    page_icon="◆",
    layout="wide",
    initial_sidebar_state="expanded",
)

if not st.session_state.get("authenticated"):
    st.switch_page("pages/1_Authentication.py")

inject_design_system()
render_sidebar(active_item="AI Coaching")
render_topbar(breadcrumb="AI Coaching")

render_page_header(
    "AI Coaching",
    "Turn behavioral signals into better coaching conversations.",
)

# ── Summary KPIs ─────────────────────────────────────────────
total_cards = sum(len(v) for v in MOCK_COACHING_CARDS.values())
high_priority = sum(1 for v in MOCK_COACHING_CARDS.values() for c in v if c["severity"] == "High Risk")
medium_priority = sum(1 for v in MOCK_COACHING_CARDS.values() for c in v if c["severity"] == "Medium Risk")

kpi_metrics = [
    {"label": "Coaching Opportunities", "value": f"{total_cards}", "detail": "Across all active deals"},
    {"label": "High Priority", "value": f"{high_priority}", "detail": "Require immediate action"},
    {"label": "Medium Priority", "value": f"{medium_priority}", "detail": "Monitor and address soon"},
    {"label": "Avg AI Confidence", "value": "92%", "detail": "Signal detection accuracy"},
]
render_kpi_strip(kpi_metrics)


# ── Intro section ────────────────────────────────────────────
section_header("Who Needs Coaching Today?", "Behavioral signals detected across your pipeline, ranked by impact on deal outcomes.")

# ── High Priority coaching cards ─────────────────────────────
st.html(
    """
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 16px;">
        <span class="sbi-badge sbi-badge--danger">● HIGH PRIORITY</span>
        <span style="font-size: 12px; color: var(--sbi-text-muted);">These behaviors are directly correlated with deal slippage. Act within 24–48 hours.</span>
    </div>
    """
)

# deal_101 coaching cards are High Risk
high_cards = [c for v in MOCK_COACHING_CARDS.values() for c in v if c["severity"] == "High Risk"]

for idx, card in enumerate(high_cards):
    col_main, col_action = st.columns([6, 1])

    rep_lookup = {"card_1": "Maya Lin", "card_2": "Maya Lin", "card_3": "Maya Lin"}
    rep_name = rep_lookup.get(card["id"], "Maya Lin")

    with col_main:
        st.markdown(
            f"""
            <div class="sbi-card" style="border-left: 3px solid var(--sbi-danger); padding: 20px; margin-bottom: 12px;">
                <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 12px;">
                    <div>
                        <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 4px;">
                            <span style="font-weight: 700; font-size: 15px; color: var(--sbi-text-primary);">{card['flag_title']}</span>
                            {badge_html(card['severity'], "danger")}
                        </div>
                        <div style="font-size: 12px; color: var(--sbi-text-muted);">Rep: <span style="color: var(--sbi-text-secondary); font-weight: 500;">{rep_name}</span></div>
                    </div>
                    <div class="sbi-ai-label">AI Signal</div>
                </div>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
                    <div>
                        <div style="font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.07em; color: var(--sbi-text-muted); margin-bottom: 6px;">Evidence</div>
                        <div style="font-size: 12px; color: var(--sbi-text-secondary); line-height: 1.5;">{card['evidence']}</div>
                    </div>
                    <div>
                        <div style="font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.07em; color: var(--sbi-text-muted); margin-bottom: 6px;">Recommended Action</div>
                        <div style="font-size: 12px; color: var(--sbi-text-primary); line-height: 1.5; border-left: 2px solid var(--sbi-cyan); padding-left: 10px;">{card['action']}</div>
                    </div>
                </div>
                <div style="margin-top: 12px; padding-top: 12px; border-top: 1px solid var(--sbi-border-subtle);">
                    <div style="font-size: 11px; color: var(--sbi-text-muted);">Expected Impact: <span style="color: var(--sbi-warning); font-weight: 600;">{card['impact']}</span></div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col_action:
        st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
        if st.button("Coach Rep", key=f"high_coach_{idx}", use_container_width=True, type="primary"):
            pass
        if st.button("Mark Done", key=f"high_done_{idx}", use_container_width=True, type="secondary"):
            pass

# ── Medium Priority coaching cards ───────────────────────────
st.html("<div style='height: 20px;'></div>")
st.html(
    """
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 16px;">
        <span class="sbi-badge sbi-badge--warning">● MEDIUM PRIORITY</span>
        <span style="font-size: 12px; color: var(--sbi-text-muted);">Address within the next coaching cycle to maintain deal momentum.</span>
    </div>
    """
)

medium_cards = [c for v in MOCK_COACHING_CARDS.values() for c in v if c["severity"] == "Medium Risk"]

for idx, card in enumerate(medium_cards):
    col_main, col_action = st.columns([6, 1])

    with col_main:
        st.markdown(
            f"""
            <div class="sbi-card" style="border-left: 3px solid var(--sbi-warning); padding: 20px; margin-bottom: 12px;">
                <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 12px;">
                    <div>
                        <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 4px;">
                            <span style="font-weight: 700; font-size: 15px; color: var(--sbi-text-primary);">{card['flag_title']}</span>
                            {badge_html(card['severity'], "warning")}
                        </div>
                        <div style="font-size: 12px; color: var(--sbi-text-muted);">Status: <span style="color: var(--sbi-text-secondary); font-weight: 500;">{card['status']}</span></div>
                    </div>
                    <div class="sbi-ai-label">AI Signal</div>
                </div>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
                    <div>
                        <div style="font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.07em; color: var(--sbi-text-muted); margin-bottom: 6px;">Evidence</div>
                        <div style="font-size: 12px; color: var(--sbi-text-secondary); line-height: 1.5;">{card['evidence']}</div>
                    </div>
                    <div>
                        <div style="font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.07em; color: var(--sbi-text-muted); margin-bottom: 6px;">Recommended Action</div>
                        <div style="font-size: 12px; color: var(--sbi-text-primary); line-height: 1.5; border-left: 2px solid rgba(251,191,36,0.5); padding-left: 10px;">{card['action']}</div>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col_action:
        st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
        if st.button("Review", key=f"med_review_{idx}", use_container_width=True, type="secondary"):
            pass

# ── AI Coaching Tips ─────────────────────────────────────────
st.html("<div style='height: 32px;'></div>")
section_header("Recommended Coaching Approaches", "Evidence-based frameworks for the behaviors detected this week.")

tips = [
    {
        "title": "Post-Demo Follow-Up Framework",
        "desc": "Train reps to pre-book the proposal review meeting before ending the demo call. This one habit reduces follow-up lag by an average of 62%.",
        "tag": "Follow-up Timing",
        "icon": "⏱",
    },
    {
        "title": "Multi-Threading Conversation Guide",
        "desc": "Use the champion to facilitate introductions: 'Who else on the leadership team will evaluate the ROI before signing?' Get names before ending the call.",
        "tag": "Stakeholder Coverage",
        "icon": "🔀",
    },
    {
        "title": "Discovery Depth — SPICED Framework",
        "desc": "Ensure reps are covering Situation, Pain, Impact, Critical Event, Decision before proposing pricing. Discovery depth is the #1 predictor of win rate.",
        "tag": "Discovery Quality",
        "icon": "🔍",
    },
]

tip_cols = st.columns(3)
for i, tip in enumerate(tips):
    with tip_cols[i]:
        st.markdown(
            f"""
            <div class="sbi-card" style="height: 100%;">
                <div style="font-size: 22px; margin-bottom: 12px;">{tip['icon']}</div>
                <div style="margin-bottom: 8px;">
                    {badge_html(tip['tag'], "cyan")}
                </div>
                <div style="font-weight: 700; font-size: 14px; margin-bottom: 8px; color: var(--sbi-text-primary);">{tip['title']}</div>
                <div style="font-size: 12px; color: var(--sbi-text-secondary); line-height: 1.6;">{tip['desc']}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
