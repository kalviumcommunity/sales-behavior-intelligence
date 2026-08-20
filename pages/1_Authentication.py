import streamlit as st

st.set_page_config(
    page_title="Authentication | Sales Behavior Intelligence",
    page_icon="◆",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.html(
    """
    <style>
    :root {
        --sbi-bg-primary: #060B14;
        --sbi-bg-surface: #101722;
        --sbi-text-primary: #F5F7FB;
        --sbi-text-secondary: #A7B0C0;
        --sbi-cyan: #5EE7FF;
        --sbi-violet: #8B7CFF;
    }
    
    .stApp {
        background-color: var(--sbi-bg-primary);
        color: var(--sbi-text-primary);
        font-family: 'Inter', sans-serif;
    }
    
    /* Hide Streamlit Chrome */
    #MainMenu, header[data-testid="stHeader"], footer, [data-testid="stToolbar"] { display: none !important; }
    section[data-testid="stSidebar"] { display: none !important; }
    
    /* Center Layout */
    .main .block-container {
        max-width: 1200px !important;
        padding: 64px 32px !important;
        margin: 0 auto;
    }
    
    /* Auth Split Layout */
    .auth-container {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 64px;
        align-items: center;
        min-height: 80vh;
    }
    
    .auth-left {
        padding-right: 32px;
    }
    
    .auth-brand {
        display: flex;
        align-items: center;
        gap: 12px;
        font-weight: 700;
        font-size: 18px;
        margin-bottom: 48px;
    }
    .auth-brand-icon {
        width: 36px;
        height: 36px;
        background: linear-gradient(135deg, var(--sbi-cyan), var(--sbi-violet));
        border-radius: 8px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: #060B14;
        font-weight: 800;
        font-size: 16px;
    }
    
    .auth-headline {
        font-size: 48px;
        font-weight: 800;
        line-height: 1.1;
        letter-spacing: -0.02em;
        margin-bottom: 32px;
    }
    
    .auth-benefit {
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 16px;
        font-size: 16px;
        font-weight: 500;
        color: var(--sbi-text-secondary);
    }
    
    .auth-benefit-icon {
        color: var(--sbi-cyan);
        font-weight: 700;
    }
    
    .auth-panel {
        background: var(--sbi-bg-surface);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 12px;
        padding: 40px;
        box-shadow: 0 12px 32px rgba(0,0,0,0.3);
    }
    
    /* Overrides */
    .stTextInput input, .stPassword input {
        background: rgba(255,255,255,0.02) !important;
        border: 1px solid rgba(255,255,255,0.1) !important;
        color: var(--sbi-text-primary) !important;
        border-radius: 8px !important;
        padding: 10px 12px !important;
    }
    .stTextInput input:focus, .stPassword input:focus {
        border-color: var(--sbi-cyan) !important;
    }
    .stButton > button {
        border-radius: 8px !important;
        font-weight: 600 !important;
        height: 44px !important;
    }
    .stButton > button[kind="primary"] {
        background: linear-gradient(135deg, var(--sbi-cyan), var(--sbi-violet)) !important;
        color: #060B14 !important;
        border: none !important;
    }
    
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
        margin-bottom: 24px;
        border-bottom: 1px solid rgba(255,255,255,0.08);
        padding: 0;
    }
    .stTabs [data-baseweb="tab"] {
        padding: 8px 0;
        background: transparent !important;
        color: var(--sbi-text-secondary);
        font-weight: 600;
    }
    .stTabs [aria-selected="true"] {
        color: var(--sbi-text-primary) !important;
        border-bottom: 2px solid var(--sbi-cyan) !important;
    }
    
    @media (max-width: 992px) {
        .auth-container { grid-template-columns: 1fr; gap: 40px; }
        .auth-left { padding-right: 0; }
        .auth-headline { font-size: 36px; }
    }
    </style>
    
    <div class="auth-container">
        <div class="auth-left">
            <div class="auth-brand">
                <div class="auth-brand-icon">SBI</div>
                Sales Behavior Intelligence
            </div>
            <div class="auth-headline">Coach from evidence.<br>Not intuition.</div>
            <div class="auth-benefit">
                <span class="auth-benefit-icon">✓</span> Behavioral intelligence
            </div>
            <div class="auth-benefit">
                <span class="auth-benefit-icon">✓</span> Deal risk detection
            </div>
            <div class="auth-benefit">
                <span class="auth-benefit-icon">✓</span> AI-powered coaching
            </div>
        </div>
        <div class="auth-panel" id="auth-panel">
    """)

tab1, tab2 = st.tabs(["Sign in", "Create account"])

with tab1:
    with st.form("signin_form", clear_on_submit=False, border=False):
        email = st.text_input("Email", placeholder="name@company.com")
        password = st.text_input("Password", type="password", placeholder="••••••••")
        
        c1, c2 = st.columns([1, 1])
        with c1:
            remember = st.checkbox("Remember me")
        with c2:
            st.html("<div style='text-align: right; margin-top: 8px;'><a href='#' style='font-size: 14px; color: var(--sbi-text-secondary);'>Forgot password?</a></div>")
            
        st.html("<div style='height: 16px;'></div>")
        submitted = st.form_submit_button("Sign in", type="primary", use_container_width=True)
        
        if submitted:
            if email and password:
                st.session_state.authenticated = True
                st.switch_page("pages/dashboard.py")
            else:
                st.error("Please enter your email and password.")
                
    st.html("<div style='height: 24px;'></div>")
    sc1, sc2 = st.columns(2)
    with sc1:
        st.button("Continue with Google", use_container_width=True)
    with sc2:
        st.button("Continue with Microsoft", use_container_width=True)

with tab2:
    with st.form("create_form", clear_on_submit=False, border=False):
        name = st.text_input("Name", placeholder="Alex Rivera")
        email_create = st.text_input("Email", placeholder="name@company.com")
        pass_create = st.text_input("Password", type="password", placeholder="••••••••")
        pass_confirm = st.text_input("Confirm password", type="password", placeholder="••••••••")
        
        st.html("<div style='height: 16px;'></div>")
        created = st.form_submit_button("Create account", type="primary", use_container_width=True)
        
        if created:
            if name and email_create and pass_create and pass_confirm:
                st.session_state.authenticated = True
                st.switch_page("pages/dashboard.py")
            else:
                st.error("Please fill in all fields.")

st.html("</div></div>")