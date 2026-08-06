import streamlit as st


def render_quick_action_card(label, description, icon="◌"):
    if st.button(f"{icon} {label}", use_container_width=True, key=f"quick_action_{label}"):
        st.toast(f"{label} launched", icon=icon)

    st.caption(description)
