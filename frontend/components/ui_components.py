"""Canonical UI Components for SBI v2.

This module provides reusable UI components that ensure visual consistency
and eliminate 'card soup' and repeated HTML strings across pages.
"""

import streamlit as st

def render_kpi_strip(metrics_list):
    """
    Renders a compact strip of KPI metrics.
    
    Args:
        metrics_list: List of dicts with 'label', 'value', 'detail', 'trend' keys.
    """
    if not metrics_list:
        return
        
    num_metrics = len(metrics_list)
    
    html = f"<div class='sbi-kpi-grid' style='grid-template-columns: repeat({num_metrics}, 1fr);'>"
    
    for m in metrics_list:
        trend_class = ""
        if m.get("trend") == "up":
            trend_class = "sbi-kpi-trend-up"
        elif m.get("trend") == "down":
            trend_class = "sbi-kpi-trend-down"
            
        html += f"""
        <div class="sbi-kpi-cell">
            <div class="sbi-kpi-label">{m.get('label', '')}</div>
            <div class="sbi-kpi-value">{m.get('value', '')}</div>
            <div class="sbi-kpi-detail {trend_class}">{m.get('detail', '')}</div>
        </div>
        """
        
    html += "</div>"
    st.html(html)


def badge_html(text, variant="neutral"):
    """
    Returns the HTML string for a badge.
    
    Variants: success, warning, danger, info, cyan, violet, neutral
    """
    return f"<span class='sbi-badge sbi-badge--{variant}'>{text}</span>"


def render_empty_state(title, desc, icon="🔍"):
    """
    Renders a consistent empty state.
    """
    st.html(
        f"""
        <div class="sbi-empty">
            <div class="sbi-empty-icon">{icon}</div>
            <div class="sbi-empty-title">{title}</div>
            <div class="sbi-empty-desc">{desc}</div>
        </div>
        """
    )


def render_ai_panel(label, content_html, style=""):
    """
    Renders a consistent AI coaching/insight panel.
    """
    st.html(
        f"""
        <div class='sbi-ai-panel' style='{style}'>
            <div class='sbi-ai-label'>{label}</div>
            {content_html}
        </div>
        """
    )


def section_header(title, subtitle=None):
    """
    Renders a consistent section title and subtitle.
    """
    html = f"<div class='sbi-section-title'>{title}</div>"
    if subtitle:
        html += f"<div class='sbi-section-subtitle'>{subtitle}</div>"
    st.html(html)
