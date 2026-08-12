import streamlit as st


def render_chart_card(title, subtitle, chart):
    st.markdown(
        f"""
        <div class="chart-card">
            <div class="section-header">
                <div>
                    <div class="section-header__eyebrow">Insight</div>
                    <h3>{title}</h3>
                    <p>{subtitle}</p>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.altair_chart(chart, use_container_width=True)
