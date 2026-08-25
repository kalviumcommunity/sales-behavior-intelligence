"""
Consumer Dashboard View
A limited-access view for users with the 'consumer' role.
"""
import streamlit as st


def render_consumer_dashboard():
    st.markdown("### 🛒 Consumer Dashboard")
    st.caption(f"Welcome back, **{st.session_state.get('username', 'User')}**!")
    
    st.info("Your account has consumer-level access. Advanced management tools and pipeline risk analytics are restricted to Admin accounts.")
    
    st.markdown("#### Quick Actions")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.button("View My Profile", use_container_width=True)
    with col2:
        st.button("My Activity Log", use_container_width=True)
    with col3:
        st.button("Contact Support", use_container_width=True)
