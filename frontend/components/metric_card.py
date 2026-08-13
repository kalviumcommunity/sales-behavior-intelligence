"""Metric Card Component - For displaying KPIs and data points."""

import streamlit as st


def render_metric(label, value, trend=None, trend_value=None, trend_direction="up"):
    """Render a single metric.
    
    Args:
        label: Metric label (e.g., "Pipeline")
        value: Main metric value (e.g., "$4.82M")
        trend: Optional trend label (e.g., "+12.4%")
        trend_value: Optional numeric trend value
        trend_direction: "up", "down", or "flat"
    """
    trend_color = "#4ADE80" if trend_direction == "up" else "#FB7185" if trend_direction == "down" else "#60A5FA"
    trend_icon = "↑" if trend_direction == "up" else "↓" if trend_direction == "down" else "→"

    st.markdown(
        f"""
        <div style='
            display: flex;
            flex-direction: column;
            gap: 8px;
            padding: 16px;
            background: rgba(16, 23, 34, 0.6);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 12px;
            transition: all 200ms cubic-bezier(0.4, 0, 0.2, 1);
        '>
            <div style='font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #697386;'>{label}</div>
            <div style='font-size: 28px; font-weight: 800; color: #F5F7FB; letter-spacing: -0.02em;'>{value}</div>
            {'<div style="font-size: 13px; color: ' + trend_color + '; font-weight: 600;">' + trend_icon + ' ' + (trend or '') + '</div>' if trend else ''}
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_metric_grid(metrics):
    """Render a grid of metrics.
    
    Args:
        metrics: List of metric dicts with keys: label, value, trend, trend_direction
    """
    cols = st.columns(len(metrics))
    for col, metric in zip(cols, metrics):
        with col:
            render_metric(
                label=metric.get("label"),
                value=metric.get("value"),
                trend=metric.get("trend"),
                trend_direction=metric.get("trend_direction", "up"),
            )


def render_metric_card(title, value, subtitle="", icon="", accent="cyan"):
    """Render a premium metric card.
    
    Args:
        title: Card title
        value: Main value to display
        subtitle: Optional subtitle
        icon: Optional emoji/icon
        accent: Color accent ("cyan", "violet", "green", "orange", "red")
    """
    accent_color = {
        "cyan": "#5EE7FF",
        "violet": "#8B7CFF",
        "green": "#4ADE80",
        "orange": "#FBBF24",
        "red": "#FB7185",
    }.get(accent, "#5EE7FF")

    st.markdown(
        f"""
        <div style='
            padding: 20px;
            background: rgba(16, 23, 34, 0.4);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 12px;
            border-left: 3px solid {accent_color};
        '>
            <div style='display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 12px;'>
                <div style='font-size: 13px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #697386;'>{title}</div>
                {'<div style="font-size: 20px;">' + icon + '</div>' if icon else ''}
            </div>
            <div style='font-size: 32px; font-weight: 800; color: #F5F7FB; letter-spacing: -0.02em; margin-bottom: 4px;'>{value}</div>
            {'<div style="font-size: 13px; color: #A7B0C0;">' + subtitle + '</div>' if subtitle else ''}
        </div>
        """,
        unsafe_allow_html=True,
    )
