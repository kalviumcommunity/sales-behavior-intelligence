"""
Authentication View (Login / Signup)
Handles user login and role assignment based on credentials.
"""
import streamlit as st

def render_auth_page():
    st.html("<h2 style='text-align: center;'>Welcome to Sales Behavior Intelligence</h2>")
    st.html("<p style='text-align: center; color: #6b7280;'>Please log in or sign up to access your dashboard.</p>")

    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        tab1, tab2 = st.tabs(["Login", "Sign Up"])

        with tab1:
            with st.form("login_form"):
                st.subheader("Login")
                username = st.text_input("Username", placeholder="e.g. admin24 or user123")
                password = st.text_input("Password", type="password")
                submit_button = st.form_submit_button("Log In", type="primary", use_container_width=True)

                if submit_button:
                    if not username or not password:
                        st.error("Please enter both username and password.")
                    else:
                        # Hardcoded logic per requirements
                        if username == "admin24" and password == "1234":
                            st.session_state.role = "admin"
                        else:
                            # Default to consumer role for any other valid login for now
                            st.session_state.role = "consumer"
                        
                        st.session_state.logged_in = True
                        st.session_state.username = username
                        st.success(f"Successfully logged in as {st.session_state.role}!")
                        st.rerun()

        with tab2:
            with st.form("signup_form"):
                st.subheader("Sign Up")
                new_username = st.text_input("Choose Username")
                new_password = st.text_input("Choose Password", type="password")
                confirm_password = st.text_input("Confirm Password", type="password")
                signup_button = st.form_submit_button("Sign Up", type="primary", use_container_width=True)

                if signup_button:
                    if not new_username or not new_password:
                        st.error("Please fill in all fields.")
                    elif new_password != confirm_password:
                        st.error("Passwords do not match.")
                    else:
                        st.session_state.role = "consumer"
                        st.session_state.logged_in = True
                        st.session_state.username = new_username
                        st.success("Account created successfully!")
                        st.rerun()
