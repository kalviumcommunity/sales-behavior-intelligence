import streamlit as st
import altair as alt

from frontend.design_system import inject_design_system
from frontend.components.app_shell import render_sidebar, render_topbar, render_page_header
from frontend.components.ui_components import render_kpi_strip, badge_html, section_header, render_ai_panel

st.set_page_config(
    page_title="Leaderboard | Sales Behavior Intelligence",
    page_icon="🏆",
    layout="wide",
    initial_sidebar_state="expanded",
)

if not st.session_state.get("authenticated"):
    st.switch_page("pages/1_Authentication.py")

inject_design_system()
render_sidebar(active_item="Leaderboard")
render_topbar(breadcrumb="Leaderboard")

# ── Custom Leaderboard CSS ────────────────────────────────────
st.html("""
<style>
.lb-podium {
    display: flex;
    align-items: flex-end;
    justify-content: center;
    gap: 20px;
    padding: 40px 24px 0;
}
.lb-podium-card {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 12px;
    flex: 1;
    max-width: 200px;
}
.lb-podium-avatar {
    width: 64px;
    height: 64px;
    border-radius: 16px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 20px;
    font-weight: 800;
    color: #0D1120;
    position: relative;
}
.lb-podium-avatar.rank-1 {
    width: 80px;
    height: 80px;
    font-size: 24px;
    background: linear-gradient(135deg, #FFD700, #FFA500);
    box-shadow: 0 0 24px rgba(255,215,0,0.45);
    border-radius: 20px;
}
.lb-podium-avatar.rank-2 {
    background: linear-gradient(135deg, #C0C0C0, #A8A8A8);
    box-shadow: 0 0 16px rgba(192,192,192,0.3);
}
.lb-podium-avatar.rank-3 {
    background: linear-gradient(135deg, #CD7F32, #A0522D);
    box-shadow: 0 0 16px rgba(205,127,50,0.3);
}
.lb-crown {
    position: absolute;
    top: -18px;
    font-size: 20px;
}
.lb-podium-name {
    font-size: 14px;
    font-weight: 700;
    color: var(--sbi-text-primary);
    text-align: center;
}
.lb-podium-role {
    font-size: 11px;
    color: var(--sbi-text-muted);
    text-align: center;
    margin-top: -8px;
}
.lb-podium-score { font-size: 28px; font-weight: 900; letter-spacing: -0.03em; }
.lb-podium-score.rank-1 { color: #FFD700; }
.lb-podium-score.rank-2 { color: #C0C0C0; }
.lb-podium-score.rank-3 { color: #CD7F32; }
.lb-podium-base {
    width: 100%;
    border-radius: 16px 16px 0 0;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 10px 0;
    font-size: 28px;
    font-weight: 900;
    color: rgba(255,255,255,0.25);
}
.lb-podium-base.rank-1 {
    background: linear-gradient(180deg, rgba(255,215,0,0.18) 0%, rgba(255,215,0,0.06) 100%);
    border: 1px solid rgba(255,215,0,0.25);
    border-bottom: none;
    height: 120px;
}
.lb-podium-base.rank-2 {
    background: linear-gradient(180deg, rgba(192,192,192,0.12) 0%, rgba(192,192,192,0.04) 100%);
    border: 1px solid rgba(192,192,192,0.18);
    border-bottom: none;
    height: 90px;
}
.lb-podium-base.rank-3 {
    background: linear-gradient(180deg, rgba(205,127,50,0.12) 0%, rgba(205,127,50,0.04) 100%);
    border: 1px solid rgba(205,127,50,0.18);
    border-bottom: none;
    height: 70px;
}
.lb-rank-row {
    display: flex;
    align-items: center;
    gap: 16px;
    padding: 14px 20px;
    border-bottom: 1px solid var(--sbi-border-subtle);
    transition: background 0.15s ease;
}
.lb-rank-row:last-child { border-bottom: none; }
.lb-rank-row:hover { background: rgba(255,255,255,0.02); }
.lb-rank-num {
    width: 32px;
    text-align: center;
    font-size: 13px;
    font-weight: 700;
    color: var(--sbi-text-muted);
    flex-shrink: 0;
}
.lb-rank-num.top3 { color: var(--sbi-cyan); }
.lb-row-avatar {
    width: 40px;
    height: 40px;
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 13px;
    font-weight: 700;
    color: var(--sbi-text-secondary);
    background: linear-gradient(135deg, var(--sbi-violet-dim), var(--sbi-cyan-dim));
    border: 1px solid var(--sbi-border-subtle);
    flex-shrink: 0;
}
.lb-row-info { flex: 1; min-width: 0; }
.lb-row-name { font-size: 14px; font-weight: 600; color: var(--sbi-text-primary); }
.lb-row-meta { font-size: 11px; color: var(--sbi-text-muted); margin-top: 2px; }
.lb-row-stat { text-align: right; flex-shrink: 0; min-width: 70px; }
.lb-row-stat-value { font-size: 16px; font-weight: 800; }
.lb-row-stat-label { font-size: 10px; color: var(--sbi-text-muted); text-transform: uppercase; letter-spacing: 0.06em; margin-top: 1px; }
.lb-progress-wrap { flex-shrink: 0; width: 100px; }
.lb-progress-bg { height: 4px; background: var(--sbi-border-subtle); border-radius: 4px; overflow: hidden; }
.lb-progress-fill { height: 100%; border-radius: 4px; }
.lb-tier {
    display: inline-flex;
    align-items: center;
    gap: 5px;
    padding: 3px 10px;
    border-radius: 100px;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.04em;
}
.lb-tier.elite       { background: rgba(255,215,0,0.12);   color: #FFD700;              border: 1px solid rgba(255,215,0,0.25); }
.lb-tier.high        { background: rgba(94,231,255,0.1);    color: var(--sbi-cyan);      border: 1px solid rgba(94,231,255,0.2); }
.lb-tier.growing     { background: rgba(139,124,255,0.1);   color: var(--sbi-violet);    border: 1px solid rgba(139,124,255,0.2); }
.lb-tier.needs-coaching { background: rgba(255,90,90,0.1); color: var(--sbi-danger);    border: 1px solid rgba(255,90,90,0.2); }
.lb-chip-row { display: flex; gap: 8px; flex-wrap: wrap; margin-top: 6px; }
.lb-chip {
    font-size: 11px;
    padding: 3px 9px;
    background: var(--sbi-bg-elevated);
    border: 1px solid var(--sbi-border-subtle);
    border-radius: 6px;
    color: var(--sbi-text-secondary);
}
.lb-trend-up   { color: var(--sbi-success); font-size: 12px; font-weight: 700; }
.lb-trend-down { color: var(--sbi-danger);  font-size: 12px; font-weight: 700; }
.lb-trend-flat { color: var(--sbi-text-muted); font-size: 12px; }
</style>
""")

render_page_header(
    "🏆 Leaderboard",
    "Real-time team ranking by behavior score, win rate, and pipeline momentum.",
)

# ── Rep data ──────────────────────────────────────────────────
ALL_REPS = [
    {
        "rank": 1, "avatar": "AR", "name": "Alex Rivera", "role": "Senior AE", "region": "West",
        "behavior_score": 96, "win_rate": 94, "pipeline": 595000, "deals": 8,
        "trend": "up", "trend_label": "↑ +8pts",
        "tier": "elite", "tier_label": "Elite",
        "quota_attainment": 118,
        "strengths": ["Multi-threaded engagement", "Fast follow-up"],
        "momentum": "↑ Strong",
    },
    {
        "rank": 2, "avatar": "ML", "name": "Maya Lin", "role": "Enterprise AE", "region": "East",
        "behavior_score": 77, "win_rate": 82, "pipeline": 410000, "deals": 6,
        "trend": "flat", "trend_label": "→ Stable",
        "tier": "high", "tier_label": "High Performer",
        "quota_attainment": 95,
        "strengths": ["Strong discovery", "Product expertise"],
        "momentum": "→ Stable",
    },
    {
        "rank": 3, "avatar": "JS", "name": "Jordan Smith", "role": "Mid-Market AE", "region": "Central",
        "behavior_score": 71, "win_rate": 68, "pipeline": 285000, "deals": 5,
        "trend": "down", "trend_label": "↓ -5pts",
        "tier": "growing", "tier_label": "Growing",
        "quota_attainment": 72,
        "strengths": ["Relationship building"],
        "momentum": "↓ Declining",
    },
    {
        "rank": 4, "avatar": "KP", "name": "Kevin Park", "role": "SMB AE", "region": "West",
        "behavior_score": 65, "win_rate": 61, "pipeline": 198000, "deals": 9,
        "trend": "up", "trend_label": "↑ +3pts",
        "tier": "growing", "tier_label": "Growing",
        "quota_attainment": 68,
        "strengths": ["High activity volume"],
        "momentum": "↑ Improving",
    },
    {
        "rank": 5, "avatar": "RC", "name": "Rachel Chen", "role": "Enterprise AE", "region": "East",
        "behavior_score": 58, "win_rate": 55, "pipeline": 320000, "deals": 4,
        "trend": "down", "trend_label": "↓ -9pts",
        "tier": "needs-coaching", "tier_label": "Needs Coaching",
        "quota_attainment": 52,
        "strengths": ["Large deal size"],
        "momentum": "↓ Declining",
    },
]

# ── Sort / filter controls ─────────────────────────────────────
sort_col, filter_col, period_col = st.columns([2, 2, 2])
with sort_col:
    sort_by = st.selectbox("Sort by", ["Behavior Score", "Win Rate", "Pipeline Value", "Quota Attainment"], index=0)
with filter_col:
    region_filter = st.selectbox("Region", ["All Regions", "West", "East", "Central"], index=0)
with period_col:
    period = st.selectbox("Period", ["This Month", "Last Quarter", "YTD"], index=0)

filtered_reps = ALL_REPS if region_filter == "All Regions" else [r for r in ALL_REPS if r["region"] == region_filter]
sort_key_map = {"Behavior Score": "behavior_score", "Win Rate": "win_rate", "Pipeline Value": "pipeline", "Quota Attainment": "quota_attainment"}
filtered_reps = sorted(filtered_reps, key=lambda x: x[sort_key_map[sort_by]], reverse=True)
for i, rep in enumerate(filtered_reps):
    rep["display_rank"] = i + 1

# ── KPI Strip ─────────────────────────────────────────────────
avg_score = round(sum(r["behavior_score"] for r in filtered_reps) / len(filtered_reps)) if filtered_reps else 0
avg_win   = round(sum(r["win_rate"] for r in filtered_reps) / len(filtered_reps)) if filtered_reps else 0
total_pipeline = sum(r["pipeline"] for r in filtered_reps)
top_quota = max((r["quota_attainment"] for r in filtered_reps), default=0)

render_kpi_strip([
    {"label": "Avg Behavior Score",   "value": str(avg_score),                      "detail": "↑ 6pts vs last month", "trend": "up"},
    {"label": "Avg Win Rate",         "value": f"{avg_win}%",                        "detail": "Across ranked reps"},
    {"label": "Total Pipeline",       "value": f"${total_pipeline/1_000_000:.2f}M",  "detail": "Active opportunity value"},
    {"label": "Top Quota Attainment", "value": f"{top_quota}%",                      "detail": "Best performer this period", "trend": "up"},
])

st.html("<div style='height: 32px;'></div>")

# ── Podium ─────────────────────────────────────────────────────
section_header("Top 3 Performers", "Podium ranking based on selected metric.")

top3 = filtered_reps[:3] if len(filtered_reps) >= 3 else filtered_reps

def format_score(rep):
    sk = sort_key_map[sort_by]
    v = rep[sk]
    if sk == "pipeline": return f"${v/1000:.0f}K"
    if sk in ("win_rate", "quota_attainment"): return f"{v}%"
    return str(v)

if len(top3) == 3:
    podium_order = [top3[1], top3[0], top3[2]]
    rank_labels  = [2, 1, 3]
elif len(top3) == 2:
    podium_order = [top3[1], top3[0]]
    rank_labels  = [2, 1]
else:
    podium_order = top3
    rank_labels  = list(range(1, len(top3)+1))

podium_cards = ""
for rep, rl in zip(podium_order, rank_labels):
    crown = '<span class="lb-crown">&#128081;</span>' if rl == 1 else ""
    podium_cards += f"""
    <div class="lb-podium-card">
        <div class="lb-podium-avatar rank-{rl}">{crown}{rep['avatar']}</div>
        <div class="lb-podium-name">{rep['name']}</div>
        <div class="lb-podium-role">{rep['role']}</div>
        <div class="lb-podium-score rank-{rl}">{format_score(rep)}</div>
        <div class="lb-podium-base rank-{rl}">#{rl}</div>
    </div>"""

st.html(f"""
<div class="sbi-card" style="padding: 0; overflow: hidden;">
    <div class="lb-podium">{podium_cards}</div>
    <div style="height: 1px; background: var(--sbi-border-subtle);"></div>
</div>
""")

st.html("<div style='height: 32px;'></div>")

# ── Full Rankings Table ────────────────────────────────────────
section_header("Full Rankings", f"Sorted by {sort_by} · {period}")

rows_html = ""
for rep in filtered_reps:
    dr = rep["display_rank"]
    score_val = format_score(rep)
    score_raw = rep[sort_key_map[sort_by]]
    sk = sort_key_map[sort_by]
    if sk == "pipeline":
        score_pct = min((score_raw / 600000) * 100, 100)
        color_val = score_raw / 600000 * 100
    elif sk in ("win_rate", "quota_attainment"):
        score_pct = min(score_raw, 100)
        color_val = score_raw
    else:
        score_pct = score_raw
        color_val = score_raw
    score_color = "var(--sbi-success)" if color_val >= 85 else ("var(--sbi-warning)" if color_val >= 65 else "var(--sbi-danger)")
    trend_cls   = "lb-trend-up" if rep["trend"] == "up" else ("lb-trend-down" if rep["trend"] == "down" else "lb-trend-flat")
    top3_cls    = "top3" if dr <= 3 else ""
    chips = "".join(f'<span class="lb-chip">{s}</span>' for s in rep["strengths"]) + f'<span class="lb-chip">📍 {rep["region"]}</span>'

    rows_html += f"""
    <div class="lb-rank-row">
        <div class="lb-rank-num {top3_cls}">#{dr}</div>
        <div class="lb-row-avatar">{rep['avatar']}</div>
        <div class="lb-row-info">
            <div class="lb-row-name">{rep['name']} &nbsp;<span class="lb-tier {rep['tier']}">{rep['tier_label']}</span></div>
            <div class="lb-row-meta">{rep['role']}</div>
            <div class="lb-chip-row">{chips}</div>
        </div>
        <div class="lb-progress-wrap">
            <div style="font-size:10px; color:var(--sbi-text-muted); margin-bottom:4px; text-align:right;">{sort_by}</div>
            <div class="lb-progress-bg">
                <div class="lb-progress-fill" style="width:{score_pct:.0f}%; background:{score_color};"></div>
            </div>
        </div>
        <div class="lb-row-stat" style="min-width:80px;">
            <div class="lb-row-stat-value" style="color:{score_color};">{score_val}</div>
            <div class="lb-row-stat-label">{sort_by}</div>
        </div>
        <div class="lb-row-stat" style="min-width:60px;">
            <div class="lb-row-stat-value">{rep['win_rate']}%</div>
            <div class="lb-row-stat-label">Win Rate</div>
        </div>
        <div class="lb-row-stat" style="min-width:55px;">
            <span class="{trend_cls}">{rep['trend_label']}</span>
        </div>
    </div>"""

st.html(f'<div class="sbi-card" style="padding: 0; overflow: hidden;">{rows_html}</div>')

st.html("<div style='height: 32px;'></div>")

# ── Charts ─────────────────────────────────────────────────────
section_header("Performance Breakdown", "Behavior score and quota attainment across all reps.")

def apply_sbi_theme():
    return {"config": {"background": "transparent", "view": {"stroke": "transparent"},
        "axis": {"domainColor": "#1A2233", "gridColor": "#1A2233", "tickColor": "#1A2233",
                 "labelColor": "#A7B0C0", "titleColor": "#A7B0C0", "titleFont": "Inter", "labelFont": "Inter"},
        "legend": {"labelColor": "#A7B0C0", "titleColor": "#A7B0C0", "titleFont": "Inter", "labelFont": "Inter"},
        "title": {"color": "#F5F7FB", "subtitleColor": "#A7B0C0", "font": "Inter", "subtitleFont": "Inter"}}}

alt.themes.register("sbi_theme", apply_sbi_theme)
alt.themes.enable("sbi_theme")

chart_data = [{"name": r["name"], "behavior_score": r["behavior_score"], "win_rate": r["win_rate"], "quota": r["quota_attainment"]} for r in filtered_reps]

c1, c2 = st.columns(2)
with c1:
    st.html("<div class='sbi-card'>")
    st.html("<div style='font-size:14px; font-weight:600; margin-bottom:16px;'>Behavior Score by Rep</div>")
    bar = (alt.Chart(alt.Data(values=chart_data))
        .mark_bar(cornerRadiusTopLeft=4, cornerRadiusTopRight=4)
        .encode(
            x=alt.X("name:N", title=None, sort=None, axis=alt.Axis(labelAngle=-30)),
            y=alt.Y("behavior_score:Q", title=None, scale=alt.Scale(domain=[0, 100])),
            color=alt.Color("behavior_score:Q", scale=alt.Scale(domain=[50, 75, 100], range=["#FF5A5A", "#F0B429", "#00E5A0"]), legend=None),
            tooltip=["name:N", "behavior_score:Q"],
        ).properties(height=220, width="container"))
    st.altair_chart(bar, use_container_width=True)
    st.html("</div>")

with c2:
    st.html("<div class='sbi-card'>")
    st.html("<div style='font-size:14px; font-weight:600; margin-bottom:16px;'>Quota Attainment vs Win Rate</div>")
    scatter = (alt.Chart(alt.Data(values=chart_data))
        .mark_circle(size=120)
        .encode(
            x=alt.X("quota:Q", title="Quota Attainment %", scale=alt.Scale(domain=[40, 130])),
            y=alt.Y("win_rate:Q", title="Win Rate %", scale=alt.Scale(domain=[40, 100])),
            color=alt.value("#8B7CFF"),
            tooltip=["name:N", "quota:Q", "win_rate:Q"],
        ).properties(height=220, width="container"))
    labels = scatter.mark_text(align="left", dx=10, dy=-5, fontSize=11, color="#A7B0C0").encode(text="name:N")
    st.altair_chart(scatter + labels, use_container_width=True)
    st.html("</div>")

st.html("<div style='height: 32px;'></div>")

# ── AI Coaching callout ────────────────────────────────────────
section_header("AI Coaching Priorities", "Reps with the highest coaching impact potential.")

coaching_reps = [r for r in filtered_reps if r["tier"] in ("growing", "needs-coaching")]
if coaching_reps:
    ai_content = ""
    for idx, rep in enumerate(coaching_reps):
        border = "" if idx == len(coaching_reps) - 1 else "1px solid rgba(139,124,255,0.1)"
        ai_content += f"""
        <div style="margin-top: 14px; padding-bottom: 14px; border-bottom: {border};">
            <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 4px;">
                <span style="font-weight: 700; font-size: 14px;">{rep['name']}</span>
                <span class="lb-tier {rep['tier']}">{rep['tier_label']}</span>
                <span style="font-size: 11px; color: var(--sbi-text-muted);">Score: {rep['behavior_score']}/100</span>
            </div>
            <div style="font-size: 12px; color: var(--sbi-text-secondary);">
                Strengths: {', '.join(rep['strengths'])} · Momentum: {rep['momentum']}
            </div>
        </div>"""
    col_ai, col_btn = st.columns([4, 1])
    with col_ai:
        render_ai_panel("AI Coaching Queue", ai_content)
    with col_btn:
        st.html("<div style='height: 48px;'></div>")
        if st.button("Open Coaching →", key="lb_coaching_btn", use_container_width=True, type="primary"):
            st.switch_page("pages/5_AI_Coaching.py")
else:
    st.html("""
    <div style="padding: 20px; text-align: center; color: var(--sbi-text-muted); font-size: 14px;">
        All filtered reps are performing at High or Elite tier!
    </div>""")
