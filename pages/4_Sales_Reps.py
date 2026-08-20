import streamlit as st

from frontend.design_system import inject_design_system
from frontend.components.app_shell import render_sidebar, render_topbar, render_page_header
from frontend.components.ui_components import render_kpi_strip, badge_html, section_header, render_ai_panel
from frontend.dashboard_data import TOP_REPS, COACHING_SUGGESTIONS

st.set_page_config(
    page_title="Sales Reps | Sales Behavior Intelligence",
    page_icon="◆",
    layout="wide",
    initial_sidebar_state="expanded",
)

if not st.session_state.get("authenticated"):
    st.switch_page("pages/1_Authentication.py")

inject_design_system()
render_sidebar(active_item="Sales Reps")
render_topbar(breadcrumb="Sales Reps")

render_page_header(
    "Sales Reps",
    "Understand team performance through behavior, not just outcomes.",
)

# ── Team metrics ────────────────────────────────────────────
avg_score = round(sum(r["behavior_score"] for r in TOP_REPS) / len(TOP_REPS)) if TOP_REPS else 0
team_pipeline = sum(int(r["pipeline"].replace("$", "").replace(",", "")) for r in TOP_REPS if r.get("pipeline"))
coaching_count = len(COACHING_SUGGESTIONS)

kpi_metrics = [
    {"label": "Team Win Rate", "value": "68%", "detail": "↑ 4% vs last quarter", "trend": "up"},
    {"label": "Team Pipeline", "value": f"${team_pipeline/1000000:.2f}M", "detail": "Across active reps"},
    {"label": "Avg Behavior Score", "value": f"{avg_score}", "detail": "↑ 6pts this month", "trend": "up"},
    {"label": "Coaching Opportunities", "value": f"{coaching_count}", "detail": "Requiring manager review", "trend": "down"},
]
render_kpi_strip(kpi_metrics)


# ── Rep Table ───────────────────────────────────────────────
section_header("Active Representatives", "Ranked by behavior score.")

# Build extended rep data
REPS_DATA = [
    {
        "rank": 1, "avatar": "AR", "name": "Alex Rivera", "role": "Senior AE",
        "behavior_score": 96, "win_rate": "94%", "pipeline": "$595,000",
        "deals": 8, "momentum": "↑ Strong", "momentum_dir": "up",
        "coaching_need": "Low", "coaching_cls": "success",
        "status": "On Track", "status_cls": "success",
        "strengths": ["Multi-threaded engagement", "Fast follow-up", "Executive alignment"],
        "coaching_note": "Leading performer — consider peer mentoring.",
    },
    {
        "rank": 2, "avatar": "ML", "name": "Maya Lin", "role": "Enterprise AE",
        "behavior_score": 77, "win_rate": "82%", "pipeline": "$410,000",
        "deals": 6, "momentum": "→ Stable", "momentum_dir": "flat",
        "coaching_need": "Medium", "coaching_cls": "warning",
        "status": "Watch", "status_cls": "warning",
        "strengths": ["Strong discovery", "Product expertise"],
        "coaching_note": "Post-demo follow-up cadence needs improvement.",
    },
    {
        "rank": 3, "avatar": "JS", "name": "Jordan Smith", "role": "Mid-Market AE",
        "behavior_score": 71, "win_rate": "68%", "pipeline": "$285,000",
        "deals": 5, "momentum": "↓ Declining", "momentum_dir": "down",
        "coaching_need": "High", "coaching_cls": "danger",
        "status": "At Risk", "status_cls": "danger",
        "strengths": ["Relationship building"],
        "coaching_note": "Discovery depth and stakeholder mapping need focus.",
    },
]

table_html = """
<div class="sbi-card sbi-table-wrapper" style="padding: 0; overflow: hidden;">
    <table class="sbi-table">
        <thead>
            <tr>
                <th style="padding-left: 20px;">Rep</th>
                <th>Behavior Score</th>
                <th>Win Rate</th>
                <th>Pipeline</th>
                <th>Deals</th>
                <th>Momentum</th>
                <th>Coaching Need</th>
                <th>Status</th>
            </tr>
        </thead>
        <tbody>
"""

for rep in REPS_DATA:
    score_pct = rep["behavior_score"]
    score_color = "var(--sbi-success)" if score_pct >= 85 else ("var(--sbi-warning)" if score_pct >= 70 else "var(--sbi-danger)")
    momentum_color = "var(--sbi-success)" if rep["momentum_dir"] == "up" else ("var(--sbi-text-muted)" if rep["momentum_dir"] == "flat" else "var(--sbi-danger)")

    table_html += f"""
            <tr>
                <td style="padding-left: 20px;">
                    <div style="display: flex; align-items: center; gap: 12px;">
                        <div style="width: 36px; height: 36px; border-radius: 8px; background: linear-gradient(135deg, var(--sbi-violet-dim), var(--sbi-cyan-dim)); border: 1px solid var(--sbi-border-subtle); display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: 700; color: var(--sbi-text-secondary);">{rep['avatar']}</div>
                        <div>
                            <div style="font-weight: 600; font-size: 14px;">{rep['name']}</div>
                            <div style="font-size: 11px; color: var(--sbi-text-muted);">{rep['role']}</div>
                        </div>
                    </div>
                </td>
                <td>
                    <div style="display: flex; align-items: center; gap: 10px;">
                        <span style="font-weight: 700; color: {score_color}; font-size: 15px;">{rep['behavior_score']}</span>
                        <div style="flex: 1; height: 3px; background: var(--sbi-border-subtle); border-radius: 2px; min-width: 60px;">
                            <div style="height: 100%; width: {score_pct}%; background: {score_color}; border-radius: 2px;"></div>
                        </div>
                    </div>
                </td>
                <td style="font-weight: 600;">{rep['win_rate']}</td>
                <td style="font-weight: 600;">{rep['pipeline']}</td>
                <td style="color: var(--sbi-text-secondary);">{rep['deals']} active</td>
                <td><span style="color: {momentum_color}; font-size: 12px; font-weight: 600;">{rep['momentum']}</span></td>
                <td>{badge_html(rep['coaching_need'], rep['coaching_cls'])}</td>
                <td style="padding-right: 20px;">{badge_html(rep['status'], rep['status_cls'])}</td>
            </tr>
    """

table_html += "</tbody></table></div>"
st.html(table_html)

# ── Rep detail cards ─────────────────────────────────────────
st.html("<div style='height: 32px;'></div>")
section_header("Representative Profiles", "Behavior patterns, strengths, and recommended coaching actions.")

cols = st.columns(3)
for i, rep in enumerate(REPS_DATA):
    score_color = "var(--sbi-success)" if rep["behavior_score"] >= 85 else ("var(--sbi-warning)" if rep["behavior_score"] >= 70 else "var(--sbi-danger)")
    with cols[i]:
        strengths_html = "".join(f'<div style="display: flex; align-items: center; gap: 8px; padding: 6px 0; border-bottom: 1px solid var(--sbi-border-subtle); font-size: 12px; color: var(--sbi-text-secondary);"><span style="color: var(--sbi-success);">✓</span> {s}</div>' for s in rep["strengths"])
        ai_html = f"<div style='font-size: 12px; color: var(--sbi-text-secondary);'>{rep['coaching_note']}</div>"
        
        st.html(
            f"""
            <div class="sbi-card" style="height: 100%;">
                <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 20px;">
                    <div style="width: 44px; height: 44px; border-radius: 10px; background: linear-gradient(135deg, rgba(139,124,255,0.2), rgba(94,231,255,0.2)); border: 1px solid var(--sbi-border-medium); display: flex; align-items: center; justify-content: center; font-size: 14px; font-weight: 700; color: var(--sbi-text-primary);">{rep['avatar']}</div>
                    <div>
                        <div style="font-size: 15px; font-weight: 700;">{rep['name']}</div>
                        <div style="font-size: 11px; color: var(--sbi-text-muted);">{rep['role']} · Rank #{rep['rank']}</div>
                    </div>
                </div>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-bottom: 20px;">
                    <div style="background: var(--sbi-bg-elevated); border-radius: 8px; padding: 10px 12px;">
                        <div style="font-size: 10px; color: var(--sbi-text-muted); text-transform: uppercase; letter-spacing: 0.07em; margin-bottom: 4px;">Behavior</div>
                        <div style="font-size: 20px; font-weight: 800; color: {score_color};">{rep['behavior_score']}</div>
                    </div>
                    <div style="background: var(--sbi-bg-elevated); border-radius: 8px; padding: 10px 12px;">
                        <div style="font-size: 10px; color: var(--sbi-text-muted); text-transform: uppercase; letter-spacing: 0.07em; margin-bottom: 4px;">Win Rate</div>
                        <div style="font-size: 20px; font-weight: 800;">{rep['win_rate']}</div>
                    </div>
                </div>
                <div style="margin-bottom: 16px;">
                    <div style="font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.07em; color: var(--sbi-text-muted); margin-bottom: 8px;">Strengths</div>
                    {strengths_html}
                </div>
            </div>
            """
        )
        render_ai_panel("Coaching Note", ai_html, style="margin-top: 16px;")

# ── Coaching opportunities ─────────────────────────────────
st.markdown("<div style='height: 32px;'></div>", unsafe_allow_html=True)
section_header("Active Coaching Opportunities", "AI-detected behavioral patterns requiring manager attention.")

for idx, c in enumerate(COACHING_SUGGESTIONS):
    col_info, col_action = st.columns([5, 1])
    with col_info:
        st.html(
            f"""
            <div style="display: flex; gap: 16px; padding: 16px 0; border-bottom: 1px solid var(--sbi-border-subtle); align-items: flex-start;">
                <div style="width: 36px; height: 36px; border-radius: 8px; background: var(--sbi-violet-dim); border: 1px solid rgba(139,124,255,0.15); display: flex; align-items: center; justify-content: center; font-size: 14px; flex-shrink: 0; color: var(--sbi-violet);">✦</div>
                <div style="flex: 1;">
                    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 4px;">
                        <span style="font-weight: 600; font-size: 14px;">{c['rep']}</span>
                        {badge_html(f"Confidence: {c['confidence']}%", "violet")}
                    </div>
                    <div style="font-size: 13px; color: var(--sbi-text-secondary); margin-bottom: 4px;">{c['problem']}</div>
                    <div style="font-size: 12px; color: var(--sbi-text-muted); border-left: 2px solid rgba(94,231,255,0.25); padding-left: 10px;">{c['suggestion']}</div>
                </div>
            </div>
            """
        )
    with col_action:
        st.markdown("<div style='height: 24px;'></div>", unsafe_allow_html=True)
        if st.button("Coach Rep", key=f"coach_{idx}", use_container_width=True, type="secondary"):
            st.switch_page("pages/5_AI_Coaching.py")
