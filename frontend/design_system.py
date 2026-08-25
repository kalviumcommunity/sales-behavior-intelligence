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
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

:root {
  --sbi-bg-primary:    #060B14;
  --sbi-bg-secondary:  #0B101A;
  --sbi-bg-surface:    #101722;
  --sbi-bg-elevated:   #141C29;
  --sbi-bg-hover:      #1A2233;

  --sbi-text-primary:   #F5F7FB;
  --sbi-text-secondary: #A7B0C0;
  --sbi-text-muted:     #697386;
  --sbi-text-inverse:   #060B14;

  --sbi-cyan:       #5EE7FF;
  --sbi-violet:     #8B7CFF;
  --sbi-cyan-dim:   rgba(94,231,255,0.10);
  --sbi-violet-dim: rgba(139,124,255,0.10);

  --sbi-success:     #4ADE80;
  --sbi-success-dim: rgba(74,222,128,0.10);
  --sbi-warning:     #FBBF24;
  --sbi-warning-dim: rgba(251,191,36,0.10);
  --sbi-danger:      #FB7185;
  --sbi-danger-dim:  rgba(251,113,133,0.10);
  --sbi-info:        #60A5FA;
  --sbi-info-dim:    rgba(96,165,250,0.10);

  --sbi-border-subtle: rgba(255,255,255,0.06);
  --sbi-border-medium: rgba(255,255,255,0.10);

  --sbi-sp-1:  4px;  --sbi-sp-2:  8px;  --sbi-sp-3:  12px;
  --sbi-sp-4:  16px; --sbi-sp-5:  20px; --sbi-sp-6:  24px;
  --sbi-sp-8:  32px; --sbi-sp-10: 40px; --sbi-sp-12: 48px;
  --sbi-sp-16: 64px;

  --sbi-r-sm:  4px; --sbi-r-md: 8px;
  --sbi-r-lg: 10px; --sbi-r-xl: 12px;

  --sbi-shadow-sm: 0 1px 4px rgba(0,0,0,0.30);
  --sbi-shadow-md: 0 4px 16px rgba(0,0,0,0.40);
  --sbi-t-fast: 150ms ease; --sbi-t-base: 200ms ease;
  --sbi-max-width: 1380px;

  /* Glassmorphism Tokens */
  --sbi-glass-bg: rgba(16, 23, 34, 0.45);
  --sbi-glass-bg-hover: rgba(16, 23, 34, 0.65);
  --sbi-glass-border: rgba(255, 255, 255, 0.08);
  --sbi-glass-border-light: rgba(255, 255, 255, 0.15);
  --sbi-glass-blur: blur(24px);
  --sbi-glass-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
}

/* ============================================================
   GLOBAL RESET & BASE
   ============================================================ */
*, *::before, *::after { box-sizing: border-box; }
html { scroll-behavior: smooth; }

@keyframes sbiFadeInUp {
  0% { opacity: 0; transform: translateY(15px); }
  100% { opacity: 1; transform: translateY(0); }
}

.stApp {
  background-color: var(--sbi-bg-primary);
  background-image: 
    radial-gradient(circle at 10% 20%, rgba(94, 231, 255, 0.06) 0%, transparent 40%),
    radial-gradient(circle at 90% 80%, rgba(139, 124, 255, 0.06) 0%, transparent 40%),
    radial-gradient(circle at 50% 50%, rgba(255, 255, 255, 0.02) 0%, transparent 60%);
  background-attachment: fixed;
  font-family: 'Inter', system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  color: var(--sbi-text-primary);
  font-size: 14px;
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
}

h1, h2, h3, h4, h5, h6 {
  color: var(--sbi-text-primary);
  margin: 0;
  line-height: 1.2;
  font-family: 'Inter', system-ui, sans-serif;
}
h1 { font-size: 38px; font-weight: 750; letter-spacing: -0.035em; }
h2 { font-size: 24px; font-weight: 700; letter-spacing: -0.015em; }
h3 { font-size: 16px; font-weight: 650; }
p  { margin: 0; color: var(--sbi-text-secondary); font-size: 14px; }
a  { color: var(--sbi-cyan); text-decoration: none; }

[data-testid="stAppViewContainer"] > section.main { padding-top: 0 !important; }

.main .block-container {
  max-width: var(--sbi-max-width) !important;
  padding: var(--sbi-sp-6) var(--sbi-sp-8) var(--sbi-sp-16) !important;
  margin: 0 auto;
}

/* ============================================================
   HIDE STREAMLIT CHROME — COMPREHENSIVE
   ============================================================ */
#MainMenu,
footer,
header[data-testid="stHeader"],
[data-testid="stToolbar"],
[data-testid="stStatusWidget"],
.viewerBadge_container__r5tak,
.styles_viewerBadge__CvC9N,
#stDecoration { display: none !important; }

/* Hide native multipage sidebar nav — CRITICAL */
[data-testid="stSidebarNav"],
[data-testid="stSidebarNavSeparator"],
[data-testid="stSidebarNavItems"],
section[data-testid="stSidebar"] nav,
section[data-testid="stSidebar"] ul:first-of-type,
ul[data-testid="stSidebarNavItems"] { display: none !important; visibility: hidden !important; height: 0 !important; }


/* ============================================================
   STREAMLIT LAYOUT NORMALIZATION
   ============================================================ */
[data-testid="stVerticalBlock"] > [data-testid="stVerticalBlockBorderWrapper"],
[data-testid="stVerticalBlock"] > div { gap: 0 !important; }

[data-testid="stVerticalBlockBorderWrapper"] {
  border: none !important;
  box-shadow: none !important;
  background: transparent !important;
  padding: 0 !important;
  margin: 0 !important;
}
[data-testid="stMarkdownContainer"] { margin-bottom: 0 !important; }
[data-testid="stMarkdownContainer"] p { margin: 0 !important; }

[data-testid="stHorizontalBlock"] {
  gap: 16px !important;
  align-items: stretch !important;
}

/* ============================================================
   STREAMLIT WIDGET OVERRIDES
   ============================================================ */
.stTextInput input,
.stSelectbox div[data-baseweb="select"] > div,
.stDateInput input,
.stNumberInput input,
.stTextArea textarea {
  background: rgba(255,255,255,0.03) !important;
  backdrop-filter: blur(12px) !important;
  -webkit-backdrop-filter: blur(12px) !important;
  color: var(--sbi-text-primary) !important;
  border: 1px solid var(--sbi-glass-border) !important;
  border-radius: var(--sbi-r-md) !important;
  font-size: 14px !important;
  font-family: 'Inter', sans-serif !important;
  transition: border-color var(--sbi-t-base) !important;
  padding: 8px 12px !important;
}
.stTextInput input:focus, .stTextArea textarea:focus {
  border-color: rgba(94,231,255,0.35) !important;
  box-shadow: 0 0 0 2px rgba(94,231,255,0.07) !important;
  outline: none !important;
}

.stTextInput label, .stSelectbox label, .stTextArea label,
.stCheckbox label, .stRadio label, .stSlider label,
.stNumberInput label, .stToggle label {
  color: var(--sbi-text-secondary) !important;
  font-size: 12px !important;
  font-weight: 500 !important;
  font-family: 'Inter', sans-serif !important;
}

.stButton button {
  background: var(--sbi-glass-bg) !important;
  backdrop-filter: var(--sbi-glass-blur) !important;
  -webkit-backdrop-filter: var(--sbi-glass-blur) !important;
  color: var(--sbi-text-primary) !important;
  border: 1px solid var(--sbi-glass-border) !important;
  border-radius: var(--sbi-r-md) !important;
  font-family: 'Inter', sans-serif !important;
  font-size: 13px !important;
  font-weight: 600 !important;
  padding: 8px 16px !important;
  transition: all var(--sbi-t-fast) !important;
  line-height: 1.4 !important;
  min-height: 36px !important;
}
.stButton button:hover {
  background: var(--sbi-glass-bg-hover) !important;
  border-color: var(--sbi-glass-border-light) !important;
  color: var(--sbi-text-primary) !important;
}

.stTabs [data-baseweb="tab-list"] {
  background: transparent !important;
  border-bottom: 1px solid var(--sbi-border-subtle) !important;
  gap: 0 !important; padding: 0 !important;
}
.stTabs [data-baseweb="tab"] {
  background: transparent !important;
  border: none !important;
  border-bottom: 2px solid transparent !important;
  color: var(--sbi-text-muted) !important;
  font-size: 13px !important; font-weight: 500 !important;
  padding: 10px 16px !important;
  margin-bottom: -1px !important;
  transition: all var(--sbi-t-fast) !important;
  border-radius: 0 !important;
  font-family: 'Inter', sans-serif !important;
}
.stTabs [data-baseweb="tab"]:hover { color: var(--sbi-text-secondary) !important; }
.stTabs [aria-selected="true"] {
  color: var(--sbi-text-primary) !important;
  border-bottom-color: var(--sbi-cyan) !important;
  font-weight: 600 !important;
}
.stTabs [data-baseweb="tab-panel"] { padding: 0 !important; background: transparent !important; }

[data-testid="stMetricValue"] {
  font-size: 24px !important; font-weight: 700 !important;
  color: var(--sbi-text-primary) !important; font-family: 'Inter', sans-serif !important;
}
[data-testid="stMetricLabel"] {
  color: var(--sbi-text-muted) !important; font-size: 11px !important;
  font-weight: 600 !important; text-transform: uppercase !important;
  letter-spacing: 0.05em !important;
}

/* ============================================================
   SHARED UTILITY CLASSES (SBI Design System)
   ============================================================ */
.sbi-badge {
  display: inline-flex; align-items: center; gap: 4px;
  padding: 3px 8px; border-radius: var(--sbi-r-sm);
  font-size: 11px; font-weight: 650; letter-spacing: 0.02em;
  border: 1px solid transparent; white-space: nowrap;
  font-family: 'Inter', sans-serif;
}
.sbi-badge--success { background: var(--sbi-success-dim); color: var(--sbi-success); border-color: rgba(74,222,128,0.18); }
.sbi-badge--warning { background: var(--sbi-warning-dim); color: var(--sbi-warning); border-color: rgba(251,191,36,0.18); }
.sbi-badge--danger  { background: var(--sbi-danger-dim);  color: var(--sbi-danger);  border-color: rgba(251,113,133,0.18); }
.sbi-badge--info    { background: var(--sbi-info-dim);    color: var(--sbi-info);    border-color: rgba(96,165,250,0.18); }
.sbi-badge--cyan    { background: var(--sbi-cyan-dim); color: var(--sbi-cyan); border-color: rgba(94,231,255,0.18); }
.sbi-badge--violet  { background: var(--sbi-violet-dim); color: var(--sbi-violet); border-color: rgba(139,124,255,0.18); }
.sbi-badge--neutral { background: rgba(105,115,134,0.10); color: var(--sbi-text-muted); border-color: var(--sbi-border-subtle); }

.sbi-btn {
  display: inline-flex; align-items: center; justify-content: center; gap: 6px;
  border-radius: var(--sbi-r-md); font-weight: 600; font-size: 13px;
  font-family: 'Inter', sans-serif; cursor: pointer;
  transition: all var(--sbi-t-fast); text-decoration: none;
  border: 1px solid var(--sbi-border-subtle); padding: 0 14px; height: 36px; white-space: nowrap;
}
.sbi-btn-primary {
  display: inline-flex; align-items: center; justify-content: center; gap: 6px;
  background: linear-gradient(135deg, rgba(94,231,255,0.15), rgba(139,124,255,0.15));
  border: 1px solid rgba(94,231,255,0.22); color: var(--sbi-cyan);
  border-radius: var(--sbi-r-md); font-weight: 600; font-size: 13px;
  font-family: 'Inter', sans-serif; cursor: pointer;
  transition: all var(--sbi-t-fast); text-decoration: none; padding: 0 16px; height: 36px;
}
.sbi-btn-primary:hover {
  background: linear-gradient(135deg, rgba(94,231,255,0.22), rgba(139,124,255,0.22));
  border-color: rgba(94,231,255,0.38); color: var(--sbi-cyan);
}
.sbi-btn-secondary {
  display: inline-flex; align-items: center; justify-content: center; gap: 6px;
  background: var(--sbi-bg-elevated); border: 1px solid var(--sbi-border-subtle);
  color: var(--sbi-text-secondary); border-radius: var(--sbi-r-md); font-weight: 600;
  font-size: 13px; font-family: 'Inter', sans-serif; cursor: pointer;
  transition: all var(--sbi-t-fast); text-decoration: none; padding: 0 16px; height: 36px;
}
.sbi-btn-secondary:hover {
  background: var(--sbi-bg-hover); border-color: var(--sbi-border-medium); color: var(--sbi-text-primary);
}

.sbi-ai-label {
  display: inline-flex; align-items: center; gap: 4px; font-size: 10px; font-weight: 700;
  color: var(--sbi-violet); letter-spacing: 0.07em; text-transform: uppercase; font-family: 'Inter', sans-serif;
}
.sbi-ai-label::before { content: "✦"; font-size: 9px; }

.sbi-ai-panel {
  background: linear-gradient(135deg, rgba(139,124,255,0.15), rgba(94,231,255,0.15));
  backdrop-filter: var(--sbi-glass-blur);
  -webkit-backdrop-filter: var(--sbi-glass-blur);
  border: 1px solid var(--sbi-glass-border-light);
  box-shadow: var(--sbi-glass-shadow);
  border-radius: var(--sbi-r-xl); padding: var(--sbi-sp-5);
}

.sbi-card {
  background: var(--sbi-glass-bg);
  backdrop-filter: var(--sbi-glass-blur);
  -webkit-backdrop-filter: var(--sbi-glass-blur);
  border: 1px solid var(--sbi-glass-border);
  box-shadow: var(--sbi-glass-shadow);
  border-radius: var(--sbi-r-xl); padding: var(--sbi-sp-5);
  animation: sbiFadeInUp 0.5s ease-out forwards;
}

.sbi-section-title {
  font-size: 17px; font-weight: 700; color: var(--sbi-text-primary);
  margin: 0 0 4px 0; letter-spacing: -0.01em; font-family: 'Inter', sans-serif;
}
.sbi-section-subtitle {
  font-size: 13px; color: var(--sbi-text-muted); margin: 0 0 20px 0; font-family: 'Inter', sans-serif;
}
.sbi-divider { height: 1px; background: var(--sbi-border-subtle); margin: var(--sbi-sp-6) 0; border: none; }

.sbi-text-muted     { color: var(--sbi-text-muted) !important; }
.sbi-text-secondary { color: var(--sbi-text-secondary) !important; }
.sbi-text-cyan      { color: var(--sbi-cyan) !important; }
.sbi-text-violet    { color: var(--sbi-violet) !important; }
.sbi-text-success   { color: var(--sbi-success) !important; }
.sbi-text-warning   { color: var(--sbi-warning) !important; }
.sbi-text-danger    { color: var(--sbi-danger) !important; }
.sbi-text-sm   { font-size: 12px !important; }
.sbi-text-xs   { font-size: 11px !important; }
.sbi-text-base { font-size: 14px !important; }
.sbi-font-bold     { font-weight: 700 !important; }
.sbi-font-semibold { font-weight: 600 !important; }
.sbi-font-medium   { font-weight: 500 !important; }

/* Metric strip layout */
.sbi-kpi-grid {
  display: grid;
  gap: 1px;
  background: var(--sbi-glass-border);
  border: 1px solid var(--sbi-glass-border);
  border-radius: var(--sbi-r-xl);
  overflow: hidden;
  margin-bottom: 32px;
  box-shadow: var(--sbi-glass-shadow);
  animation: sbiFadeInUp 0.5s ease-out forwards;
}
.sbi-kpi-cell {
  background: var(--sbi-glass-bg);
  backdrop-filter: var(--sbi-glass-blur);
  -webkit-backdrop-filter: var(--sbi-glass-blur);
  padding: 16px 20px;
}
.sbi-kpi-label {
  font-size: 10px; font-weight: 700; text-transform: uppercase;
  letter-spacing: 0.08em; color: var(--sbi-text-muted); margin-bottom: 6px;
}
.sbi-kpi-value {
  font-size: 22px; font-weight: 800; letter-spacing: -0.025em;
  color: var(--sbi-text-primary); line-height: 1; margin-bottom: 3px;
}
.sbi-kpi-detail { font-size: 11px; color: var(--sbi-text-muted); }
.sbi-kpi-trend-up   { color: var(--sbi-success); font-size: 11px; font-weight: 600; }
.sbi-kpi-trend-down { color: var(--sbi-danger);  font-size: 11px; font-weight: 600; }

/* Tables */
.sbi-table-wrapper { width: 100%; overflow-x: auto; }
.sbi-table {
  width: 100%; border-collapse: collapse;
  font-size: 13px; text-align: left; font-family: 'Inter', sans-serif;
}
.sbi-table th {
  color: var(--sbi-text-muted); font-size: 10px; font-weight: 700;
  text-transform: uppercase; letter-spacing: 0.07em;
  padding: 10px 14px; border-bottom: 1px solid var(--sbi-border-subtle); white-space: nowrap;
}
.sbi-table td {
  padding: 12px 14px; color: var(--sbi-text-primary);
  border-bottom: 1px solid var(--sbi-border-subtle); vertical-align: middle;
}
.sbi-table tbody tr:hover { background: var(--sbi-bg-hover); }
.sbi-table tr:last-child td { border-bottom: none; }

/* Empty state */
.sbi-empty { text-align: center; padding: 56px 24px; color: var(--sbi-text-muted); }
.sbi-empty-icon { font-size: 28px; margin-bottom: 12px; opacity: 0.6; }
.sbi-empty-title { font-size: 15px; font-weight: 600; color: var(--sbi-text-secondary); margin-bottom: 6px; }
.sbi-empty-desc  { font-size: 13px; color: var(--sbi-text-muted); }

/* ============================================================
   GAMIFICATION & LEADERBOARD UI
   ============================================================ */
.sbi-leaderboard-row {
  display: flex; align-items: center; justify-content: space-between;
  padding: 16px 20px; margin-bottom: 12px;
  background: var(--sbi-glass-bg);
  backdrop-filter: var(--sbi-glass-blur);
  -webkit-backdrop-filter: var(--sbi-glass-blur);
  border: 1px solid var(--sbi-glass-border);
  box-shadow: var(--sbi-glass-shadow);
  border-radius: var(--sbi-r-xl);
  transition: all var(--sbi-t-base);
  animation: sbiFadeInUp 0.5s ease-out forwards;
  background: var(--sbi-bg-surface);
  border: 1px solid var(--sbi-border-subtle);
  border-radius: var(--sbi-r-xl);
  transition: all var(--sbi-t-base);
}
.sbi-leaderboard-row:hover {
  background: var(--sbi-bg-hover);
  border-color: var(--sbi-border-medium);
  transform: translateY(-2px);
  box-shadow: var(--sbi-shadow-md);
}

.sbi-avatar-container {
  position: relative; display: inline-flex; align-items: center; justify-content: center;
  width: 48px; height: 48px; border-radius: 12px; font-weight: 700; font-size: 16px;
  background: var(--sbi-bg-elevated); z-index: 1;
}
.sbi-avatar-rank {
  position: absolute; top: -8px; left: -8px; width: 22px; height: 22px;
  border-radius: 50%; display: flex; align-items: center; justify-content: center;
  font-size: 11px; font-weight: 800; color: #fff; z-index: 2;
  box-shadow: 0 2px 6px rgba(0,0,0,0.4);
}
.sbi-rank-1 .sbi-avatar-container { background: linear-gradient(135deg, rgba(255,215,0,0.2), rgba(255,165,0,0.1)); border: 2px solid #FFD700; color: #FFD700; }
.sbi-rank-1 .sbi-avatar-rank { background: linear-gradient(135deg, #FFD700, #FFA500); }

.sbi-rank-2 .sbi-avatar-container { background: linear-gradient(135deg, rgba(192,192,192,0.2), rgba(169,169,169,0.1)); border: 2px solid #C0C0C0; color: #C0C0C0; }
.sbi-rank-2 .sbi-avatar-rank { background: linear-gradient(135deg, #E0E0E0, #A9A9A9); color: #333; }

.sbi-rank-3 .sbi-avatar-container { background: linear-gradient(135deg, rgba(205,127,50,0.2), rgba(139,69,19,0.1)); border: 2px solid #CD7F32; color: #CD7F32; }
.sbi-rank-3 .sbi-avatar-rank { background: linear-gradient(135deg, #CD7F32, #8B4513); }

.sbi-rank-other .sbi-avatar-container { background: var(--sbi-bg-elevated); border: 1px solid var(--sbi-border-medium); color: var(--sbi-text-secondary); }
.sbi-rank-other .sbi-avatar-rank { background: var(--sbi-bg-elevated); border: 1px solid var(--sbi-border-medium); color: var(--sbi-text-muted); }

.sbi-achievements-container {
  display: flex; gap: 8px; flex-wrap: wrap; margin-top: 4px;
}
.sbi-achievement-badge {
  display: inline-flex; align-items: center; gap: 4px;
  background: var(--sbi-bg-elevated);
  border: 1px solid var(--sbi-border-subtle);
  padding: 4px 8px; border-radius: 20px;
  font-size: 11px; font-weight: 600; color: var(--sbi-text-secondary);
}
.sbi-achievement-badge span.icon { font-size: 12px; }

@media (max-width: 1024px) {
  .main .block-container { padding: var(--sbi-sp-4) var(--sbi-sp-5) var(--sbi-sp-10) !important; }
}
@media (max-width: 768px) {
  .main .block-container { padding: var(--sbi-sp-3) var(--sbi-sp-4) var(--sbi-sp-8) !important; }
  h1 { font-size: 22px !important; }
}
</style>
"""


def inject_design_system():
    """Call this at the top of every page."""
    import streamlit as st

    st.html(DESIGN_SYSTEM_CSS)
