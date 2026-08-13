import streamlit as st


def render_chart_card(title, subtitle, chart):
    st.markdown(
        f"""
        <div class="chart-card">
            <div class="chart-card__header">
                <div class="section-header__eyebrow">Insight</div>
                <h3 style="margin: 6px 0 4px; font-size: 1.05rem; letter-spacing: -0.02em;">{title}</h3>
                <p style="margin: 0; color: var(--muted); font-size: 0.88rem; line-height: 1.5;">{subtitle}</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.altair_chart(chart, use_container_width=True)
