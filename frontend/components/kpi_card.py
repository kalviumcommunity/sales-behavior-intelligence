import streamlit as st


def render_kpi_card(label, value, detail, accent="cyan"):
    st.markdown(
        f"""
        <div class="kpi-card kpi-{accent}">
            <div class="kpi-label">{label}</div>
            <div class="kpi-value">{value}</div>
            <div class="kpi-detail">{detail}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
