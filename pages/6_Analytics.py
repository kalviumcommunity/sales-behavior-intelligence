import altair as alt
import streamlit as st

from frontend.design_system import inject_design_system
from frontend.components.app_shell import render_sidebar, render_topbar, render_page_header
from frontend.components.ui_components import section_header
from frontend.dashboard_data import (
    REVENUE_TREND,
    PIPELINE_BY_STAGE,
    MONTHLY_PERFORMANCE,
    RISK_DISTRIBUTION,
    WIN_LOSS_RATIO,
    TOP_REPS,
)

st.set_page_config(
    page_title="Analytics | Sales Behavior Intelligence",
    page_icon="◆",
    layout="wide",
    initial_sidebar_state="expanded",
)

if not st.session_state.get("authenticated"):
    st.switch_page("pages/1_Authentication.py")

inject_design_system()
render_sidebar(active_item="Analytics")
render_topbar(breadcrumb="Analytics")

render_page_header(
    "Analytics",
    "Understand the patterns shaping revenue performance.",
)

# ── Altair SBI theme ─────────────────────────────────────────
def apply_sbi_theme():
    return {
        "config": {
            "background": "transparent",
            "view": {"stroke": "transparent", "fill": "transparent"},
            "axis": {
                "domainColor": "#1A2233",
                "gridColor": "#1A2233",
                "tickColor": "transparent",
                "labelColor": "#697386",
                "titleColor": "#A7B0C0",
                "titleFont": "Inter",
                "labelFont": "Inter",
                "labelFontSize": 11,
            },
            "legend": {
                "labelColor": "#A7B0C0",
                "titleColor": "#A7B0C0",
                "titleFont": "Inter",
                "labelFont": "Inter",
                "labelFontSize": 11,
            },
            "title": {
                "color": "#F5F7FB",
                "subtitleColor": "#A7B0C0",
                "font": "Inter",
                "subtitleFont": "Inter",
                "fontSize": 14,
                "fontWeight": 600,
                "anchor": "start",
                "offset": 12,
            },
        }
    }

alt.themes.register("sbi_theme", apply_sbi_theme)
alt.themes.enable("sbi_theme")

# ── Revenue Trend & Pipeline by Stage ────────────────────────
section_header("Revenue & Pipeline", "Monthly revenue trend and current pipeline distribution by stage.")

col_r1, col_r2 = st.columns(2)

with col_r1:
    st.html("<div class='sbi-card'>")
    st.html(
        "<div style='font-size: 13px; font-weight: 600; color: var(--sbi-text-secondary); margin-bottom: 16px; text-transform: uppercase; letter-spacing: 0.05em;'>Revenue Trend</div>"
    )
    revenue_chart = (
        alt.Chart(alt.Data(values=REVENUE_TREND))
        .mark_area(
            line={"color": "#5EE7FF", "strokeWidth": 2},
            color=alt.Gradient(
                gradient="linear",
                stops=[
                    alt.GradientStop(color="rgba(94,231,255,0.18)", offset=0),
                    alt.GradientStop(color="rgba(94,231,255,0)", offset=1),
                ],
                x1=1, x2=1, y1=1, y2=0,
            ),
        )
        .encode(
            x=alt.X("month:N", title=None, axis=alt.Axis(labelAngle=0)),
            y=alt.Y("revenue:Q", title=None, axis=alt.Axis(format="~s")),
            tooltip=[
                alt.Tooltip("month:N", title="Month"),
                alt.Tooltip("revenue:Q", title="Revenue", format="$,.0f"),
            ],
        )
        .properties(height=220, width="container")
    )
    st.altair_chart(revenue_chart, use_container_width=True)
    st.markdown("</div>")

with col_r2:
    st.html("<div class='sbi-card'>")
    st.html(
        "<div style='font-size: 13px; font-weight: 600; color: var(--sbi-text-secondary); margin-bottom: 16px; text-transform: uppercase; letter-spacing: 0.05em;'>Pipeline by Stage</div>"
    )
    pipeline_chart = (
        alt.Chart(alt.Data(values=PIPELINE_BY_STAGE))
        .mark_bar(color="#8B7CFF", cornerRadiusTopLeft=4, cornerRadiusTopRight=4)
        .encode(
            x=alt.X("stage:N", title=None, axis=alt.Axis(labelAngle=-30)),
            y=alt.Y("count:Q", title=None),
            tooltip=[
                alt.Tooltip("stage:N", title="Stage"),
                alt.Tooltip("count:Q", title="Deals"),
            ],
        )
        .properties(height=220, width="container")
    )
    st.altair_chart(pipeline_chart, use_container_width=True)
    st.markdown("</div>")

# ── Win Rate & Behavior Trend ─────────────────────────────────
st.html("<div style='height: 32px;'></div>")
section_header("Performance Over Time", "Win rate, pipeline health, and coaching completion trends by month.")

col_p1, col_p2 = st.columns(2)

with col_p1:
    st.html("<div class='sbi-card'>")
    st.html(
        "<div style='font-size: 13px; font-weight: 600; color: var(--sbi-text-secondary); margin-bottom: 16px; text-transform: uppercase; letter-spacing: 0.05em;'>Win Rate Trend (%)</div>"
    )
    win_rate_chart = (
        alt.Chart(alt.Data(values=MONTHLY_PERFORMANCE))
        .mark_line(color="#4ADE80", strokeWidth=2, point=alt.OverlayMarkDef(color="#4ADE80", size=40))
        .encode(
            x=alt.X("month:N", title=None, axis=alt.Axis(labelAngle=0)),
            y=alt.Y("win_rate:Q", title=None, scale=alt.Scale(domain=[55, 75])),
            tooltip=[
                alt.Tooltip("month:N", title="Month"),
                alt.Tooltip("win_rate:Q", title="Win Rate", format=".0f"),
            ],
        )
        .properties(height=200, width="container")
    )
    st.altair_chart(win_rate_chart, use_container_width=True)
    st.markdown("</div>")

with col_p2:
    st.html("<div class='sbi-card'>")
    st.html(
        "<div style='font-size: 13px; font-weight: 600; color: var(--sbi-text-secondary); margin-bottom: 16px; text-transform: uppercase; letter-spacing: 0.05em;'>Coaching Completion (%)</div>"
    )
    coaching_chart = (
        alt.Chart(alt.Data(values=MONTHLY_PERFORMANCE))
        .mark_bar(color="#5EE7FF", cornerRadiusTopLeft=4, cornerRadiusTopRight=4, opacity=0.8)
        .encode(
            x=alt.X("month:N", title=None, axis=alt.Axis(labelAngle=0)),
            y=alt.Y("coaching_completion:Q", title=None, scale=alt.Scale(domain=[0, 100])),
            tooltip=[
                alt.Tooltip("month:N", title="Month"),
                alt.Tooltip("coaching_completion:Q", title="Coaching %", format=".0f"),
            ],
        )
        .properties(height=200, width="container")
    )
    st.altair_chart(coaching_chart, use_container_width=True)
    st.markdown("</div>")

# ── Rep Comparison & Risk Distribution ───────────────────────
st.html("<div style='height: 32px;'></div>")
section_header("Team Breakdown", "Rep performance comparison and portfolio risk distribution.")

col_t1, col_t2 = st.columns([1.4, 1])

with col_t1:
    rep_data = [
        {"name": r["name"], "metric": "Win Rate", "value": int(r["win_rate"].replace("%", ""))}
        for r in TOP_REPS
    ] + [
        {"name": r["name"], "metric": "Behavior Score", "value": r["behavior_score"]}
        for r in TOP_REPS
    ]

    st.html("<div class='sbi-card'>")
    st.html(
        "<div style='font-size: 13px; font-weight: 600; color: var(--sbi-text-secondary); margin-bottom: 16px; text-transform: uppercase; letter-spacing: 0.05em;'>Rep Comparison</div>"
    )
    rep_chart = (
        alt.Chart(alt.Data(values=rep_data))
        .mark_bar(cornerRadiusTopLeft=3, cornerRadiusTopRight=3)
        .encode(
            x=alt.X("value:Q", title=None),
            y=alt.Y("name:N", title=None, sort="-x"),
            color=alt.Color(
                "metric:N",
                scale=alt.Scale(domain=["Win Rate", "Behavior Score"], range=["#5EE7FF", "#8B7CFF"]),
                legend=alt.Legend(title=None, orient="top", labelFontSize=11),
            ),
            xOffset="metric:N",
            tooltip=[
                alt.Tooltip("name:N", title="Rep"),
                alt.Tooltip("metric:N", title="Metric"),
                alt.Tooltip("value:Q", title="Score"),
            ],
        )
        .properties(height=200, width="container")
    )
    st.altair_chart(rep_chart, use_container_width=True)
    st.markdown("</div>")

with col_t2:
    st.html("<div class='sbi-card'>")
    st.html(
        "<div style='font-size: 13px; font-weight: 600; color: var(--sbi-text-secondary); margin-bottom: 16px; text-transform: uppercase; letter-spacing: 0.05em;'>Risk Distribution</div>"
    )
    risk_chart = (
        alt.Chart(alt.Data(values=RISK_DISTRIBUTION))
        .mark_arc(innerRadius=55, padAngle=0.03, cornerRadius=4)
        .encode(
            theta=alt.Theta("value:Q"),
            color=alt.Color(
                "bucket:N",
                scale=alt.Scale(
                    domain=["Low", "Medium", "High"],
                    range=["#4ADE80", "#FBBF24", "#FB7185"],
                ),
                legend=alt.Legend(title=None, orient="bottom"),
            ),
            tooltip=[
                alt.Tooltip("bucket:N", title="Risk"),
                alt.Tooltip("value:Q", title="Deals"),
            ],
        )
        .properties(height=200, width="container")
    )
    st.altair_chart(risk_chart, use_container_width=True)
    st.markdown("</div>")

# ── Key Insights ─────────────────────────────────────────────
st.html("<div style='height: 32px;'></div>")
section_header("Key Insights", "Patterns the AI has detected in your pipeline data this period.")

insights = [
    {
        "icon": "↑",
        "color": "var(--sbi-success)",
        "title": "Win rate is up 7pts over 6 months",
        "desc": "Consistent improvement correlates with increased coaching completion and multi-threaded deal execution.",
    },
    {
        "icon": "⚠",
        "color": "var(--sbi-warning)",
        "title": "40% of pipeline is at Medium or High risk",
        "desc": "3 of 5 active high-value deals show single-threaded stakeholder engagement patterns.",
    },
    {
        "icon": "✦",
        "color": "var(--sbi-violet)",
        "title": "Coaching drives 1.4× higher velocity",
        "desc": "Deals where coaching was completed within 48 hours of a risk signal are progressing 40% faster.",
    },
    {
        "icon": "◆",
        "color": "var(--sbi-cyan)",
        "title": "Revenue run rate: $375K/month",
        "desc": "Up from $240K in January. Projected Q3 close: $1.1M if current pipeline converts at 68%.",
    },
]

insight_cols = st.columns(2)
for i, insight in enumerate(insights):
    with insight_cols[i % 2]:
        st.markdown(
            f"""
            <div style="display: flex; gap: 16px; padding: 16px 0; border-bottom: 1px solid var(--sbi-border-subtle);">
                <div style="width: 36px; height: 36px; border-radius: 8px; background: var(--sbi-bg-elevated); display: flex; align-items: center; justify-content: center; font-size: 16px; color: {insight['color']}; flex-shrink: 0;">{insight['icon']}</div>
                <div>
                    <div style="font-weight: 600; font-size: 14px; margin-bottom: 4px;">{insight['title']}</div>
                    <div style="font-size: 12px; color: var(--sbi-text-secondary); line-height: 1.5;">{insight['desc']}</div>
                </div>
            </div>
            """
        )
