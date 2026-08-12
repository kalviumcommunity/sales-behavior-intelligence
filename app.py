import streamlit as st

# Imports from modular frontend package
from frontend.mock_data import MOCK_REPS, MOCK_DEALS, MOCK_TIMELINES, MOCK_COACHING_CARDS
from frontend.components.metrics import render_kpi_metrics
from frontend.views.pipeline_overview import render_pipeline_overview
from frontend.views.deal_deep_dive import render_deal_deep_dive
from frontend.views.rep_coaching import render_rep_coaching

# Page Configuration
st.set_page_config(
    page_title="Sales Behavior Intelligence",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for rich aesthetics and clean UI styling
st.markdown(
    """
    <style>
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
    }
    .stMetric {
        background-color: #f8fafc;
        border: 1px solid #e2e8f0;
        padding: 14px;
        border-radius: 10px;
        box-shadow: 0 1px 2px rgba(0,0,0,0.03);
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 12px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 48px;
        white-space: pre-wrap;
        background-color: #f1f5f9;
        border-radius: 8px;
        font-weight: 600;
        color: #475569;
        padding: 0px 20px;
    }
    .stTabs [aria-selected="true"] {
        background-color: #2563eb !important;
        color: #ffffff !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header Section
st.title("🧠 Sales Behavior Intelligence Platform")
st.caption("Evidence-based coaching insights extracted from CRM events, email timestamps, and call transcripts.")

st.markdown("---")

# Global Top KPI Bar
render_kpi_metrics(MOCK_DEALS)

st.markdown("<br>", unsafe_allow_html=True)

# Main Dashboard Navigation Tabs
tab1, tab2, tab3 = st.tabs([
    "📊 Pipeline Risk Matrix",
    "🔍 Deal Deep Dive & Timeline",
    "👤 Rep Coaching & Analytics",
])

with tab1:
    render_pipeline_overview(MOCK_DEALS)

with tab2:
    render_deal_deep_dive(MOCK_DEALS, MOCK_TIMELINES, MOCK_COACHING_CARDS)

with tab3:
    render_rep_coaching(MOCK_REPS, MOCK_DEALS)

# Sidebar Information
with st.sidebar:
    st.image("https://img.icons8.com/color/96/brain--v1.png", width=64)
    st.markdown("### **Sales Behavior Intelligence**")
    st.caption("Sprint 1 Frontend Skeleton")
    st.markdown("---")
    st.markdown("##### 👥 Active Persona View")
    st.radio("Switch Role Perspective", ["David (Sales Manager)", "Maya (Sales Rep)", "Priya (RevOps Lead)"])
    st.markdown("---")
    st.markdown("##### 🛠️ System Status")
    status_col1, status_col2 = st.columns(2)
    with status_col1:
        st.success("UI: Mock", icon="✅")
    with status_col2:
        st.info("API: Spr2", icon="⏳")