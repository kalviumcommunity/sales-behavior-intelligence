import streamlit as st

st.set_page_config(
    page_title="Sign In | Sales Behavior Intelligence",
    page_icon="◆",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─── Styles ───────────────────────────────────────────────────────
st.html("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

:root {
    --auth-bg: #050A12;
    --auth-surface: #0D1622;
    --auth-panel: #101925;
    --auth-text: #F5F7FB;
    --auth-text-sec: #A8B3C7;
    --auth-muted: #66758A;
    --auth-cyan: #58E6FF;
    --auth-violet: #8B7CFF;
    --auth-border: rgba(255,255,255,0.08);
    --auth-border-hover: rgba(255,255,255,0.14);
}

@keyframes authPulseDot {
    0%, 100% { opacity: 0.4; }
    50% { opacity: 1; box-shadow: 0 0 8px rgba(88,230,255,0.6); }
}

/* ── Base ── */
.stApp {
    background-color: var(--auth-bg) !important;
    background-image:
        radial-gradient(circle at 15% 35%, rgba(88,230,255,0.12), transparent 40%),
        radial-gradient(circle at 82% 45%, rgba(139,124,255,0.12), transparent 40%),
        radial-gradient(circle at 50% 100%, rgba(88,230,255,0.05), transparent 50%),
        linear-gradient(rgba(255,255,255,0.02) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255,255,255,0.02) 1px, transparent 1px);
    background-size: 100% 100%, 100% 100%, 100% 100%, 64px 64px, 64px 64px;
    font-family: 'Inter', sans-serif !important;
}

/* ── Hide Chrome ── */
#MainMenu, header[data-testid="stHeader"], footer,
[data-testid="stToolbar"], [data-testid="stDecoration"],
[data-testid="stStatusWidget"] { display: none !important; }
section[data-testid="stSidebar"] { display: none !important; }

/* ── Layout ── */
.main .block-container {
    max-width: 1280px !important;
    padding: 8vh 48px 48px !important;
    margin: 0 auto !important;
}
[data-testid="stVerticalBlock"] > div { gap: 0 !important; }
[data-testid="stMarkdownContainer"] p { margin: 0 !important; }

/* ── Left brand column HTML classes ── */
.auth-brand-col {
    padding: 40px 0;
}

.auth-back {
    font-size: 13px;
    color: var(--auth-muted);
    text-decoration: none;
    display: inline-flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 48px;
    transition: color 0.15s, transform 0.15s;
    font-weight: 500;
}
.auth-back:hover {
    color: var(--auth-cyan);
    transform: translateX(-2px);
}

.auth-brand-row {
    display: flex;
    align-items: center;
    gap: 14px;
    margin-bottom: 50px;
}
.auth-brand-icon {
    width: 40px; height: 40px;
    background: linear-gradient(135deg, var(--auth-cyan), var(--auth-violet));
    border-radius: 10px;
    display: flex; align-items: center; justify-content: center;
    font-size: 15px; font-weight: 800; color: #050A12;
    flex-shrink: 0;
    transition: box-shadow 0.3s ease;
}
.auth-brand-row:hover .auth-brand-icon {
    box-shadow: 0 0 24px rgba(88,230,255,0.25);
}
.auth-brand-name {
    font-size: 18px; font-weight: 700;
    color: var(--auth-text);
    letter-spacing: -0.01em; line-height: 1.2;
}
.auth-brand-name small {
    display: block; font-size: 12px;
    font-weight: 500; color: var(--auth-muted);
}

.auth-eyebrow {
    display: flex; align-items: center; gap: 8px;
    font-size: 11px; font-weight: 700;
    text-transform: uppercase; letter-spacing: 0.14em;
    color: var(--auth-cyan); margin-bottom: 16px;
}
.auth-eyebrow-dot {
    width: 6px; height: 6px; border-radius: 50%;
    background: var(--auth-cyan);
    animation: authPulseDot 2.5s ease-in-out infinite;
}

.auth-headline {
    font-size: clamp(36px, 4vw, 52px);
    font-weight: 800; line-height: 1.05;
    letter-spacing: -0.03em; margin-bottom: 24px;
    background: linear-gradient(90deg, #FFFFFF, #DDE7F7);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.auth-headline span {
    background: linear-gradient(90deg, #DFFBFF, #58E6FF);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.auth-desc {
    font-size: 17px; line-height: 1.6;
    color: var(--auth-text-sec);
    margin-bottom: 48px; max-width: 440px;
}

.auth-benefit-row {
    display: flex; align-items: center;
    gap: 14px; margin-bottom: 16px;
    font-size: 15px; font-weight: 500;
    color: var(--auth-text-sec);
    transition: transform 0.2s ease, color 0.2s ease;
    cursor: default;
}
.auth-check {
    width: 24px; height: 24px; border-radius: 50%;
    background: rgba(88,230,255,0.04);
    border: 1px solid rgba(88,230,255,0.15);
    display: flex; align-items: center; justify-content: center;
    font-size: 12px; color: var(--auth-cyan);
    font-weight: 700; flex-shrink: 0;
    transition: background 0.2s, border-color 0.2s, box-shadow 0.2s;
}
.auth-benefit-row:hover {
    transform: translateX(4px);
    color: var(--auth-text);
}
.auth-benefit-row:hover .auth-check {
    background: rgba(88,230,255,0.08);
    border-color: rgba(88,230,255,0.30);
    box-shadow: 0 0 12px rgba(88,230,255,0.15);
}

/* ── Right Column (Auth Panel) ── Glass Effect ── */
[data-testid="column"]:nth-of-type(2) {
    background: rgba(13,22,34,0.55) !important;
    backdrop-filter: blur(20px) saturate(1.4) !important;
    -webkit-backdrop-filter: blur(20px) saturate(1.4) !important;
    border: 1px solid rgba(255,255,255,0.12) !important;
    border-top: 1px solid rgba(255,255,255,0.18) !important;
    border-radius: 16px !important;
    padding: 40px !important;
    box-shadow:
        0 24px 80px rgba(0,0,0,0.35),
        0 0 60px rgba(88,230,255,0.06),
        0 0 120px rgba(139,124,255,0.04),
        inset 0 1px 0 rgba(255,255,255,0.05) !important;
    max-width: 440px !important;
    margin-left: auto !important;
    transition: box-shadow 0.3s ease, border-color 0.3s ease !important;
}
[data-testid="column"]:nth-of-type(2):hover {
    border-color: rgba(255,255,255,0.18) !important;
    box-shadow:
        0 24px 80px rgba(0,0,0,0.35),
        0 0 80px rgba(88,230,255,0.08),
        0 0 140px rgba(139,124,255,0.06),
        inset 0 1px 0 rgba(255,255,255,0.07) !important;
}

.auth-panel-header { margin-bottom: 32px; }
.auth-panel-title {
    font-size: 28px; font-weight: 750;
    color: #FFFFFF; margin-bottom: 8px;
    letter-spacing: -0.02em;
}
.auth-panel-sub {
    font-size: 15px; color: #93A4BB; line-height: 1.55;
}

/* ── Tab Control ── */
.stTabs [data-baseweb="tab-list"] {
    background: rgba(255,255,255,0.025) !important;
    border: 1px solid rgba(255,255,255,0.06) !important;
    border-radius: 8px !important;
    padding: 4px !important;
    gap: 4px !important;
    margin-bottom: 28px !important;
}
.stTabs [data-baseweb="tab"] {
    flex: 1 !important;
    border-radius: 6px !important;
    background: transparent !important;
    color: var(--auth-muted) !important;
    font-weight: 600 !important;
    font-size: 13px !important;
    padding: 8px 16px !important;
    transition: all 0.18s ease !important;
    border: none !important;
}
.stTabs [data-baseweb="tab"]:hover {
    color: var(--auth-text-sec) !important;
}
.stTabs [aria-selected="true"] {
    background: rgba(255,255,255,0.06) !important;
    color: #FFFFFF !important;
    box-shadow: 0 1px 4px rgba(0,0,0,0.2) !important;
    border-bottom: none !important;
}
[data-baseweb="tab-highlight"], [data-baseweb="tab-border"] { display: none !important; }

/* ── Inputs ── Frosted Glass ── */
.stTextInput > div > div > input,
.stTextInput > label + div > div > input {
    background: rgba(255,255,255,0.03) !important;
    backdrop-filter: blur(8px) !important;
    -webkit-backdrop-filter: blur(8px) !important;
    border: 1px solid rgba(255,255,255,0.10) !important;
    border-radius: 8px !important;
    color: var(--auth-text) !important;
    font-size: 14px !important;
    height: 48px !important;
    padding: 0 16px !important;
    transition: border-color 0.15s ease, box-shadow 0.15s ease, background 0.15s ease !important;
}
.stTextInput > div > div > input:hover {
    border-color: rgba(255,255,255,0.14) !important;
}
.stTextInput > div > div > input:focus {
    border-color: rgba(88,230,255,0.65) !important;
    box-shadow: 0 0 0 3px rgba(88,230,255,0.08) !important;
    background: #0D1622 !important;
}
.stTextInput label {
    font-size: 13px !important;
    font-weight: 600 !important;
    color: var(--auth-text-sec) !important;
}

/* ── Primary Button ── */
.stFormSubmitButton > button[kind="primary"] {
    background: linear-gradient(135deg, #4CE0FF, #7B6CFF) !important;
    color: #040A14 !important;
    border: none !important;
    font-weight: 700 !important;
    font-size: 15px !important;
    height: 48px !important;
    border-radius: 8px !important;
    transition: transform 0.18s ease, box-shadow 0.18s ease, filter 0.18s ease !important;
    text-shadow: 0 1px 2px rgba(0,0,0,0.1) !important;
}
.stFormSubmitButton > button[kind="primary"]:hover {
    transform: translateY(-1px) !important;
    box-shadow: 0 10px 35px rgba(88,230,255,0.25), 0 0 15px rgba(88,230,255,0.10) !important;
    filter: brightness(1.08) !important;
}

/* ── Social Buttons ── Frosted Glass ── */
.stButton > button[kind="secondary"] {
    background: rgba(255,255,255,0.03) !important;
    backdrop-filter: blur(8px) !important;
    -webkit-backdrop-filter: blur(8px) !important;
    border: 1px solid rgba(255,255,255,0.10) !important;
    color: var(--auth-text) !important;
    border-radius: 8px !important;
    font-weight: 600 !important;
    font-size: 14px !important;
    height: 46px !important;
    transition: all 0.18s ease !important;
}
.stButton > button[kind="secondary"]:hover {
    background: rgba(255,255,255,0.07) !important;
    border-color: rgba(255,255,255,0.20) !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 4px 16px rgba(0,0,0,0.2) !important;
}

/* ── Divider ── */
.auth-divider {
    display: flex; align-items: center;
    gap: 16px; margin: 28px 0;
    color: var(--auth-muted); font-size: 12px; font-weight: 500;
}
.auth-divider::before, .auth-divider::after {
    content: ''; flex: 1; height: 1px;
    background: rgba(255,255,255,0.08);
}

/* ── Checkbox ── */
.stCheckbox p {
    font-size: 13px !important;
    color: var(--auth-text-sec) !important;
}

/* ── Forgot Link ── */
.auth-forgot {
    font-size: 13px; color: var(--auth-cyan);
    text-decoration: none; font-weight: 500;
    float: right; margin-top: 6px;
    transition: color 0.15s;
}
.auth-forgot:hover { color: #8FF2FF; text-decoration: underline; }

/* ── Trust line ── */
.auth-secure {
    text-align: center; font-size: 11px;
    color: var(--auth-muted); margin-top: 32px;
    display: flex; align-items: center;
    justify-content: center; gap: 6px;
}

/* ── Responsive ── */
@media (max-width: 992px) {
    .main .block-container { padding: 40px 24px !important; }
    [data-testid="column"]:nth-of-type(2) {
        max-width: 100% !important; margin: 0 !important;
        padding: 32px !important;
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
}
</style>
""")

# ─── Layout ──────────────────────────────────────────────────────
left_col, right_col = st.columns([1.1, 1], gap="large")

with left_col:
    st.html("""
    <div class="auth-brand-col">
        <a href="/" class="auth-back" target="_top">← Back to website</a>

        <div class="auth-brand-row">
            <div class="auth-brand-icon">SBI</div>
            <div class="auth-brand-name">
                Sales Behavior Intelligence
                <small>Revenue Intelligence Platform</small>
            </div>
        </div>

        <div class="auth-eyebrow">
            <div class="auth-eyebrow-dot"></div>
            SALES INTELLIGENCE PLATFORM
        </div>
        <div class="auth-headline">Coach from <span>evidence.</span><br>Not intuition.</div>
        <div class="auth-desc">
            Sales Behavior Intelligence turns seller behavior, CRM activity, and deal signals into actionable intelligence for revenue teams.
        </div>

        <div class="auth-benefits">
            <div class="auth-benefit-row">
                <div class="auth-check">✓</div>
                Understand behavioral signals across your pipeline
            </div>
            <div class="auth-benefit-row">
                <div class="auth-check">✓</div>
                Detect deal risk earlier with AI-powered signals
            </div>
            <div class="auth-benefit-row">
                <div class="auth-check">✓</div>
                Coach reps with evidence, not anecdote
            </div>
        </div>
    </div>
    """)

with right_col:
    st.html("""
        <div class="auth-panel-header">
            <div class="auth-panel-title">Welcome back</div>
            <div class="auth-panel-sub">Sign in to your workspace to access pipeline intelligence,<br>deal risk signals, and coaching insights.</div>
        </div>
    """)

    tab1, tab2 = st.tabs(["Sign in", "Create account"])

    with tab1:
        with st.form("signin_form", clear_on_submit=False, border=False):
            email = st.text_input("Work email", placeholder="name@company.com")
            password = st.text_input("Password", type="password", placeholder="••••••••")

            c1, c2 = st.columns([1, 1])
            with c1:
                remember = st.checkbox("Remember me")
            with c2:
                st.html("<a href='#' class='auth-forgot'>Forgot password?</a>")

            st.html("<div style='height:8px;'></div>")
            submitted = st.form_submit_button("Sign in →", type="primary", use_container_width=True)

            if submitted:
                if email and password:
                    st.session_state.authenticated = True
                    st.switch_page("pages/dashboard.py")
                else:
                    st.error("Please enter your email and password.")

        st.html("<div class='auth-divider'>or continue with</div>")
        st.button("Continue with Google", key="google_signin", use_container_width=True, type="secondary")
        st.html("<div style='height:4px;'></div>")
        st.button("Continue with Microsoft", key="microsoft_signin", use_container_width=True, type="secondary")

    with tab2:
        with st.form("create_form", clear_on_submit=False, border=False):
            name = st.text_input("Full name", placeholder="Alex Rivera")
            email_create = st.text_input("Work email", placeholder="name@company.com")
            pass_create = st.text_input("Password", type="password", placeholder="••••••••")
            pass_confirm = st.text_input("Confirm password", type="password", placeholder="••••••••")

            st.html("<div style='height:8px;'></div>")
            created = st.form_submit_button("Create account →", type="primary", use_container_width=True)

            if created:
                if name and email_create and pass_create and pass_confirm:
                    st.session_state.authenticated = True
                    st.switch_page("pages/dashboard.py")
                else:
                    st.error("Please fill in all fields.")

        st.html("<div class='auth-divider'>or continue with</div>")
        st.button("Continue with Google", key="google_create", use_container_width=True, type="secondary")
        st.html("<div style='height:4px;'></div>")
        st.button("Continue with Microsoft", key="microsoft_create", use_container_width=True, type="secondary")

    st.html("""
        <div class="auth-secure">
            🔒 Secure workspace access
        </div>
    """)
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
