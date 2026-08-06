import streamlit as st


def render_section_header(title, subtitle="", action_label=""):
    left, right = st.columns([4, 1], vertical_alignment="center")
    with left:
        st.markdown(
            f"""
            <div class="section-header">
                <div>
                    <div class="section-header__eyebrow">Manager dashboard</div>
                    <h3>{title}</h3>
                    <p>{subtitle}</p>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    if action_label:
        with right:
            st.button(action_label, use_container_width=True, key=f"section_action_{title}")
