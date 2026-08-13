"""
Centralized Design System for Sales Behavior Intelligence v2.
All CSS variables, tokens, and shared styles in one place.
Import and inject via inject_design_system() in each page.
"""

DESIGN_SYSTEM_CSS = """
<style>
/* ============================================================
   DESIGN TOKENS — SBI v2
   ============================================================ */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

:root {
  /* Backgrounds */
  --bg-primary:    #070A12;
  --bg-secondary:  #0B101A;
  --bg-surface:    #101722;
  --bg-elevated:   #141C29;
  --bg-hover:      #1A2233;

  /* Borders */
  --border-subtle:  rgba(255,255,255,0.07);
  --border-medium:  rgba(255,255,255,0.11);
  --border-strong:  rgba(255,255,255,0.18);

  /* Text */
  --text-primary:   #F5F7FB;
  --text-secondary: #A7B0C0;
  --text-muted:     #697386;
  --text-disabled:  #3E4558;

  /* Accents */
  --accent-cyan:    #5EE7FF;
  --accent-violet:  #8B7CFF;
  --accent-cyan-dim: rgba(94,231,255,0.12);
  --accent-violet-dim: rgba(139,124,255,0.12);

  /* Status */
  --success:        #4ADE80;
  --success-dim:    rgba(74,222,128,0.12);
  --warning:        #FBBF24;
  --warning-dim:    rgba(251,191,36,0.12);
  --danger:         #FB7185;
  --danger-dim:     rgba(251,113,133,0.12);
  --info:           #60A5FA;
  --info-dim:       rgba(96,165,250,0.12);

  /* Spacing scale */
  --sp-1: 4px;
  --sp-2: 8px;
  --sp-3: 12px;
  --sp-4: 16px;
  --sp-5: 20px;
  --sp-6: 24px;
  --sp-8: 32px;
  --sp-10: 40px;
  --sp-12: 48px;

  /* Radius */
  --r-sm:  6px;
  --r-md:  8px;
  --r-lg:  10px;
  --r-xl:  12px;
  --r-2xl: 14px;
  --r-3xl: 16px;

  /* Shadows */
  --shadow-sm:  0 1px 3px rgba(0,0,0,0.3);
  --shadow-md:  0 4px 12px rgba(0,0,0,0.35);
  --shadow-lg:  0 8px 24px rgba(0,0,0,0.4);

  /* Transitions */
  --t-fast:   150ms ease;
  --t-base:   200ms ease;
  --t-slow:   300ms ease;

  /* Font sizes */
  --text-xs:   11px;
  --text-sm:   12px;
  --text-base: 14px;
  --text-md:   15px;
  --text-lg:   16px;
  --text-xl:   20px;
  --text-2xl:  24px;
  --text-3xl:  32px;
  --text-4xl:  40px;

  /* Container */
  --max-width: 1400px;
}

/* ============================================================
   GLOBAL RESET & BASE
   ============================================================ */
*, *::before, *::after {
  box-sizing: border-box;
}

html {
  scroll-behavior: smooth;
}

.stApp {
  background-color: var(--bg-primary);
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  color: var(--text-primary);
  font-size: var(--text-base);
  line-height: 1.6;
}

.main .block-container {
  max-width: var(--max-width);
  padding-top: 0;
  padding-bottom: var(--sp-12);
  padding-left: var(--sp-8);
  padding-right: var(--sp-8);
}

/* ============================================================
   HIDE STREAMLIT DEFAULT ELEMENTS
   ============================================================ */
#MainMenu, footer, header { display: none !important; }
.stDeployButton { display: none !important; }

/* ============================================================
   SIDEBAR — Premium SaaS nav
   ============================================================ */
section[data-testid="stSidebar"] {
  background: var(--bg-secondary) !important;
  border-right: 1px solid var(--border-subtle) !important;
  width: 240px !important;
}

section[data-testid="stSidebar"] > div:first-child {
  padding: var(--sp-5) var(--sp-4);
}

/* ============================================================
   STREAMLIT INPUTS
   ============================================================ */
.stTextInput input,
.stSelectbox div[data-baseweb="select"] > div,
.stDateInput input,
.stNumberInput input,
.stTextArea textarea {
  background: var(--bg-surface) !important;
  color: var(--text-primary) !important;
  border: 1px solid var(--border-subtle) !important;
  border-radius: var(--r-md) !important;
  font-size: var(--text-base) !important;
  font-family: 'Inter', sans-serif !important;
  transition: border-color var(--t-base) !important;
}

.stTextInput input:focus,
.stSelectbox div[data-baseweb="select"] > div:focus-within {
  border-color: var(--accent-cyan) !important;
  box-shadow: 0 0 0 3px rgba(94,231,255,0.08) !important;
  outline: none !important;
}

.stTextInput label,
.stSelectbox label,
.stTextArea label,
.stCheckbox label {
  color: var(--text-secondary) !important;
  font-size: var(--text-sm) !important;
  font-weight: 500 !important;
}

/* ============================================================
   STREAMLIT BUTTONS
   ============================================================ */
.stButton button {
  background: var(--bg-surface) !important;
  color: var(--text-primary) !important;
  border: 1px solid var(--border-subtle) !important;
  border-radius: var(--r-md) !important;
  font-family: 'Inter', sans-serif !important;
  font-size: var(--text-base) !important;
  font-weight: 600 !important;
  padding: 8px 16px !important;
  transition: all var(--t-fast) !important;
  line-height: 1.4 !important;
  letter-spacing: -0.01em !important;
}

.stButton button:hover {
  background: var(--bg-hover) !important;
  border-color: var(--border-medium) !important;
  transform: none !important;
}

/* Primary button variant */
.btn-primary button {
  background: var(--accent-cyan) !important;
  color: #070A12 !important;
  border-color: transparent !important;
  font-weight: 700 !important;
}

.btn-primary button:hover {
  opacity: 0.9 !important;
}

/* ============================================================
   STREAMLIT TABS
   ============================================================ */
.stTabs [data-baseweb="tab-list"] {
  background: transparent !important;
  border-bottom: 1px solid var(--border-subtle) !important;
  gap: 0 !important;
  padding: 0 !important;
}

.stTabs [data-baseweb="tab"] {
  background: transparent !important;
  border: none !important;
  border-bottom: 2px solid transparent !important;
  color: var(--text-muted) !important;
  font-size: var(--text-base) !important;
  font-weight: 500 !important;
  padding: 10px 16px !important;
  margin-bottom: -1px !important;
  transition: all var(--t-fast) !important;
  border-radius: 0 !important;
}

.stTabs [data-baseweb="tab"]:hover {
  color: var(--text-secondary) !important;
  background: transparent !important;
}

.stTabs [aria-selected="true"] {
  color: var(--text-primary) !important;
  border-bottom-color: var(--accent-cyan) !important;
  background: transparent !important;
}

/* ============================================================
   STREAMLIT CONTAINERS — remove default borders
   ============================================================ */
div[data-testid="stVerticalBlockBorderWrapper"] {
  border: 1px solid var(--border-subtle) !important;
  border-radius: var(--r-2xl) !important;
  background: var(--bg-surface) !important;
  box-shadow: var(--shadow-sm) !important;
  padding: var(--sp-4) !important;
  margin-bottom: var(--sp-3) !important;
}

/* ============================================================
   SHARED COMPONENT TOKENS
   ============================================================ */

/* Status badges */
.sbi-badge {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  padding: 3px 8px;
  border-radius: var(--r-sm);
  font-size: var(--text-xs);
  font-weight: 600;
  letter-spacing: 0.03em;
  line-height: 1.6;
  border: 1px solid transparent;
}

.sbi-badge--success { background: var(--success-dim); color: var(--success); border-color: rgba(74,222,128,0.2); }
.sbi-badge--warning { background: var(--warning-dim); color: var(--warning); border-color: rgba(251,191,36,0.2); }
.sbi-badge--danger  { background: var(--danger-dim);  color: var(--danger);  border-color: rgba(251,113,133,0.2); }
.sbi-badge--info    { background: var(--info-dim);    color: var(--info);    border-color: rgba(96,165,250,0.2); }
.sbi-badge--cyan    { background: var(--accent-cyan-dim); color: var(--accent-cyan); border-color: rgba(94,231,255,0.2); }
.sbi-badge--violet  { background: var(--accent-violet-dim); color: var(--accent-violet); border-color: rgba(139,124,255,0.2); }
.sbi-badge--muted   { background: rgba(105,115,134,0.12); color: var(--text-muted); border-color: var(--border-subtle); }

/* AI element indicator */
.sbi-ai-label {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  font-size: var(--text-xs);
  font-weight: 600;
  color: var(--accent-violet);
  letter-spacing: 0.04em;
  text-transform: uppercase;
}

.sbi-ai-label::before {
  content: "✦";
  font-size: 9px;
}

/* Section titles */
.sbi-section-title {
  font-size: var(--text-xl);
  font-weight: 700;
  color: var(--text-primary);
  letter-spacing: -0.02em;
  margin: 0 0 var(--sp-4) 0;
}

.sbi-section-subtitle {
  font-size: var(--text-base);
  color: var(--text-secondary);
  margin: var(--sp-1) 0 var(--sp-5) 0;
}

/* Card base */
.sbi-card {
  background: var(--bg-surface);
  border: 1px solid var(--border-subtle);
  border-radius: var(--r-2xl);
  padding: var(--sp-5);
  transition: border-color var(--t-base);
}

.sbi-card:hover {
  border-color: var(--border-medium);
}

/* Metric display */
.sbi-metric {
  font-size: 28px;
  font-weight: 700;
  letter-spacing: -0.04em;
  color: var(--text-primary);
  line-height: 1.1;
}

.sbi-metric-label {
  font-size: var(--text-sm);
  color: var(--text-muted);
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  margin-bottom: var(--sp-2);
}

.sbi-metric-trend {
  font-size: var(--text-sm);
  font-weight: 600;
  margin-top: var(--sp-1);
}

.sbi-metric-trend--up   { color: var(--success); }
.sbi-metric-trend--down { color: var(--danger); }
.sbi-metric-trend--flat { color: var(--text-muted); }

/* Progress bar */
.sbi-progress-track {
  height: 4px;
  background: var(--border-subtle);
  border-radius: 999px;
  overflow: hidden;
  margin-top: var(--sp-2);
}

.sbi-progress-fill {
  height: 100%;
  border-radius: inherit;
  transition: width 0.4s ease;
}

/* Avatar */
.sbi-avatar {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: var(--r-lg);
  font-size: var(--text-sm);
  font-weight: 700;
  color: var(--accent-cyan);
  background: var(--accent-cyan-dim);
  border: 1px solid rgba(94,231,255,0.15);
  flex-shrink: 0;
}

.sbi-avatar--sm { width: 28px; height: 28px; font-size: 10px; }
.sbi-avatar--md { width: 32px; height: 32px; }
.sbi-avatar--lg { width: 40px; height: 40px; font-size: var(--text-base); }

/* Divider */
.sbi-divider {
  height: 1px;
  background: var(--border-subtle);
  margin: var(--sp-5) 0;
  border: none;
}

/* Warning banner */
.sbi-warning {
  display: flex;
  gap: var(--sp-3);
  align-items: flex-start;
  padding: var(--sp-3) var(--sp-4);
  background: var(--warning-dim);
  border: 1px solid rgba(251,191,36,0.2);
  border-radius: var(--r-lg);
  font-size: var(--text-sm);
  color: var(--warning);
  margin-bottom: var(--sp-4);
}

/* AI insight card */
.sbi-ai-card {
  background: linear-gradient(135deg, rgba(139,124,255,0.07), rgba(94,231,255,0.07));
  border: 1px solid rgba(139,124,255,0.18);
  border-radius: var(--r-2xl);
  padding: var(--sp-5);
}

/* Table base */
.sbi-table {
  width: 100%;
  border-collapse: collapse;
  font-size: var(--text-base);
}

.sbi-table th {
  text-align: left;
  padding: var(--sp-2) var(--sp-3);
  color: var(--text-muted);
  font-size: var(--text-xs);
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  border-bottom: 1px solid var(--border-subtle);
}

.sbi-table td {
  padding: var(--sp-3) var(--sp-3);
  color: var(--text-primary);
  border-bottom: 1px solid var(--border-subtle);
  vertical-align: middle;
}

.sbi-table tr:last-child td { border-bottom: none; }

.sbi-table tbody tr {
  transition: background var(--t-fast);
}

.sbi-table tbody tr:hover {
  background: var(--bg-hover);
}

/* Empty state */
.sbi-empty {
  text-align: center;
  padding: var(--sp-12) var(--sp-8);
  color: var(--text-muted);
}

.sbi-empty-icon {
  font-size: 32px;
  margin-bottom: var(--sp-4);
  opacity: 0.5;
}

.sbi-empty-title {
  font-size: var(--text-lg);
  font-weight: 600;
  color: var(--text-secondary);
  margin-bottom: var(--sp-2);
}

.sbi-empty-body {
  font-size: var(--text-base);
  color: var(--text-muted);
  max-width: 320px;
  margin: 0 auto var(--sp-5);
}

/* Timeline item */
.sbi-timeline-item {
  display: flex;
  gap: var(--sp-3);
  padding: var(--sp-3) 0;
  position: relative;
}

.sbi-timeline-line {
  width: 1px;
  background: var(--border-subtle);
  position: absolute;
  left: 15px;
  top: 42px;
  bottom: 0;
}

.sbi-timeline-dot {
  width: 32px;
  height: 32px;
  min-width: 32px;
  border-radius: var(--r-lg);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 13px;
  border: 1px solid var(--border-subtle);
  background: var(--bg-surface);
  flex-shrink: 0;
  position: relative;
  z-index: 1;
}

.sbi-timeline-body { flex: 1; padding-top: 4px; }
.sbi-timeline-meta {
  font-size: var(--text-xs);
  color: var(--text-muted);
  margin-bottom: 3px;
  display: flex;
  gap: var(--sp-2);
  align-items: center;
}
.sbi-timeline-title {
  font-size: var(--text-base);
  font-weight: 600;
  color: var(--text-primary);
  margin-bottom: 3px;
}
.sbi-timeline-desc {
  font-size: var(--text-sm);
  color: var(--text-secondary);
  line-height: 1.5;
}

/* ============================================================
   RESPONSIVE
   ============================================================ */
@media (max-width: 1024px) {
  .main .block-container {
    padding-left: var(--sp-5);
    padding-right: var(--sp-5);
  }
}

@media (max-width: 768px) {
  .main .block-container {
    padding-left: var(--sp-4);
    padding-right: var(--sp-4);
    padding-top: 0;
  }

  section[data-testid="stSidebar"] {
    width: 100% !important;
  }
}
</style>
"""


def inject_design_system():
    """Call this at the top of every authenticated page."""
    import streamlit as st
    st.markdown(DESIGN_SYSTEM_CSS, unsafe_allow_html=True)
