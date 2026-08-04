import streamlit as st


st.set_page_config(
    page_title="Authentication | Sales Behavior Intelligence",
    page_icon="◼",
    layout="wide",
    initial_sidebar_state="collapsed",
)


def render_stat_chip(label, value):
    st.markdown(
        f"""
        <div class="auth-chip">
            <span>{label}</span>
            <strong>{value}</strong>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_bullet_list(items):
    bullets = "".join(
        f"""
        <div class="auth-bullet">
            <div class="auth-bullet__icon">{item['icon']}</div>
            <div>
                <h4>{item['title']}</h4>
                <p>{item['body']}</p>
            </div>
        </div>
        """
        for item in items
    )
    st.markdown(f"<div class='auth-bullet-list'>{bullets}</div>", unsafe_allow_html=True)


AUTH_TRUST_POINTS = [
    {
        "icon": "◌",
        "title": "Secure workspace access",
        "body": "Premium sign-in surfaces designed to feel native to the existing dark SaaS system.",
    },
    {
        "icon": "◌",
        "title": "Mock identity flow",
        "body": "Frontend-only authentication interactions with polished states and no backend dependency.",
    },
    {
        "icon": "◌",
        "title": "Responsive by default",
        "body": "The layout compresses cleanly from desktop through mobile without changing the design language.",
    },
]


st.markdown(
    """
    <style>
    :root {
        --bg: #070b14;
        --bg-soft: #0d1220;
        --panel: rgba(13, 18, 32, 0.82);
        --panel-border: rgba(148, 163, 184, 0.16);
        --text: #eef4ff;
        --muted: #9aa7bd;
        --cyan: #56d8ff;
        --violet: #8d7cff;
    }

    .stApp {
        background:
            radial-gradient(circle at top left, rgba(86, 216, 255, 0.14), transparent 28%),
            radial-gradient(circle at top right, rgba(141, 124, 255, 0.16), transparent 24%),
            linear-gradient(180deg, #060913 0%, #0a1020 52%, #05070d 100%);
        color: var(--text);
    }

    .main .block-container {
        padding-top: 1.35rem;
        padding-bottom: 2.5rem;
        max-width: 1320px;
    }

    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, rgba(7, 11, 20, 0.98), rgba(11, 16, 30, 0.96));
        border-right: 1px solid rgba(148, 163, 184, 0.08);
    }

    h1, h2, h3, h4, p, span, div, li, label {
        color: var(--text);
    }

    .auth-shell,
    .auth-card,
    .auth-panel,
    .auth-features,
    .auth-chip,
    .auth-bullet {
        border: 1px solid var(--panel-border);
        background: var(--panel);
        border-radius: 24px;
        box-shadow: 0 18px 40px rgba(0, 0, 0, 0.26);
    }

    .auth-shell {
        position: relative;
        overflow: hidden;
        padding: 28px;
        margin-bottom: 16px;
        background: linear-gradient(135deg, rgba(13, 18, 32, 0.92), rgba(13, 18, 32, 0.72));
    }

    .auth-shell:before {
        content: "";
        position: absolute;
        inset: 0;
        background: linear-gradient(135deg, rgba(86, 216, 255, 0.08), transparent 35%, rgba(141, 124, 255, 0.08));
        pointer-events: none;
    }

    .eyebrow {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        font-size: 0.74rem;
        letter-spacing: 0.18em;
        text-transform: uppercase;
        color: var(--muted);
        margin-bottom: 12px;
    }

    .eyebrow:before {
        content: "";
        width: 9px;
        height: 9px;
        border-radius: 999px;
        background: linear-gradient(135deg, var(--cyan), var(--violet));
        box-shadow: 0 0 18px rgba(86, 216, 255, 0.5);
    }

    .auth-title {
        font-size: clamp(2.2rem, 4.5vw, 4.4rem);
        line-height: 0.98;
        margin: 0;
        letter-spacing: -0.04em;
    }

    .auth-copy {
        max-width: 760px;
        color: var(--muted);
        font-size: 1.02rem;
        line-height: 1.7;
        margin: 18px 0 22px;
    }

    .auth-chip-row {
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 12px;
        margin-top: 18px;
    }

    .auth-chip {
        padding: 14px 16px;
        display: grid;
        gap: 8px;
        min-height: 92px;
    }

    .auth-chip span {
        color: var(--muted);
        font-size: 0.74rem;
        text-transform: uppercase;
        letter-spacing: 0.14em;
    }

    .auth-chip strong {
        font-size: 1rem;
        line-height: 1.4;
    }

    .auth-card {
        padding: 22px;
        position: relative;
        overflow: hidden;
    }

    .auth-card__header {
        display: flex;
        align-items: flex-start;
        justify-content: space-between;
        gap: 12px;
        margin-bottom: 18px;
    }

    .auth-card__header h3 {
        margin: 0;
        font-size: 1.3rem;
    }

    .auth-card__header p {
        margin: 6px 0 0;
        color: var(--muted);
        line-height: 1.55;
    }

    .auth-badge {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        border-radius: 999px;
        padding: 8px 12px;
        border: 1px solid rgba(148, 163, 184, 0.16);
        background: rgba(255, 255, 255, 0.03);
        color: var(--text);
        font-size: 0.8rem;
        letter-spacing: 0.12em;
        text-transform: uppercase;
    }

    .auth-badge:before {
        content: "";
        width: 8px;
        height: 8px;
        border-radius: 999px;
        background: linear-gradient(135deg, var(--cyan), var(--violet));
        box-shadow: 0 0 18px rgba(86, 216, 255, 0.45);
    }

    .auth-feature-grid {
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 14px;
        margin-top: 18px;
    }

    .auth-features {
        padding: 18px;
    }

    .auth-features h4 {
        margin: 0 0 6px;
        font-size: 1rem;
    }

    .auth-features p {
        margin: 0;
        color: var(--muted);
        line-height: 1.6;
        font-size: 0.94rem;
    }

    .auth-panel {
        padding: 18px;
    }

    .auth-panel h4 {
        margin: 0 0 10px;
        font-size: 1rem;
    }

    .auth-panel p {
        margin: 0;
        color: var(--muted);
        line-height: 1.6;
        font-size: 0.94rem;
    }

    .auth-bullet-list {
        display: grid;
        gap: 12px;
    }

    .auth-bullet {
        display: flex;
        gap: 14px;
        padding: 16px;
    }

    .auth-bullet__icon {
        width: 36px;
        height: 36px;
        min-width: 36px;
        display: grid;
        place-items: center;
        border-radius: 12px;
        background: rgba(255, 255, 255, 0.04);
        color: var(--cyan);
        border: 1px solid rgba(86, 216, 255, 0.18);
    }

    .auth-bullet h4 {
        margin: 0 0 5px;
        font-size: 0.98rem;
    }

    .auth-bullet p {
        margin: 0;
        color: var(--muted);
        line-height: 1.55;
        font-size: 0.92rem;
    }

    .auth-footer {
        margin-top: 18px;
        padding: 18px 20px;
        border-radius: 22px;
        border: 1px solid var(--panel-border);
        background: linear-gradient(135deg, rgba(86, 216, 255, 0.08), rgba(141, 124, 255, 0.08), rgba(13, 18, 32, 0.94));
    }

    .auth-footer p {
        color: var(--muted);
        margin: 8px 0 0;
        line-height: 1.55;
    }

    .stTextInput input,
    .stNumberInput input,
    .stSelectbox div[data-baseweb="select"] > div,
    .stPassword input {
        background: rgba(255, 255, 255, 0.04) !important;
        color: var(--text) !important;
        border-color: rgba(148, 163, 184, 0.22) !important;
        border-radius: 16px !important;
    }

    .stTextInput label,
    .stPassword label,
    .stSelectbox label,
    .stCheckbox label {
        color: var(--muted) !important;
    }

    .stForm {
        background: rgba(255, 255, 255, 0.02);
        border: 1px solid rgba(148, 163, 184, 0.14);
        border-radius: 20px;
        padding: 16px;
    }

    .stButton button {
        border-radius: 999px;
        border: 1px solid rgba(148, 163, 184, 0.18);
        background: rgba(255, 255, 255, 0.04);
        color: var(--text);
        font-weight: 700;
        padding: 0.72rem 1rem;
    }

    .stButton button:hover {
        border-color: rgba(86, 216, 255, 0.5);
        transform: translateY(-1px);
    }

    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: rgba(255, 255, 255, 0.02);
        padding: 6px;
        border-radius: 999px;
        border: 1px solid rgba(148, 163, 184, 0.12);
    }

    .stTabs [data-baseweb="tab"] {
        border-radius: 999px;
        color: var(--muted);
        background: transparent;
        padding: 10px 16px;
    }

    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, rgba(86, 216, 255, 0.14), rgba(141, 124, 255, 0.14));
        color: var(--text);
    }

    @media (max-width: 1100px) {
        .auth-chip-row,
        .auth-feature-grid {
            grid-template-columns: 1fr 1fr;
        }
    }

    @media (max-width: 720px) {
        .auth-chip-row,
        .auth-feature-grid {
            grid-template-columns: 1fr;
        }

        .auth-shell {
            padding: 22px;
        }

        .auth-card__header {
            flex-direction: column;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)


with st.sidebar:
    st.markdown("### Sales Behavior Intelligence")
    st.caption("Evidence-first coaching for revenue teams.")
    st.markdown("---")
    st.markdown("#### Mode")
    st.markdown("Authentication preview")
    st.markdown("#### View")
    st.markdown("Mock sign-in and account creation")
    st.markdown("#### Status")
    st.success("Frontend only")
    st.info("No backend or API calls")


left_col, right_col = st.columns([1.15, 0.95], gap="large")

with left_col:
    st.markdown(
        """
        <div class="auth-shell">
            <div class="eyebrow">Secure access for modern sales teams</div>
            <h1 class="auth-title">Enter the workspace with the same premium feel as the product.</h1>
            <p class="auth-copy">
                This authentication page keeps the same dark glass aesthetic as the landing experience while
                giving managers and reps a focused, responsive sign-in surface built entirely from mock data.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<div class='auth-panel'>", unsafe_allow_html=True)
    render_bullet_list(AUTH_TRUST_POINTS)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div style='height: 14px;'></div>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class="auth-panel">
            <h4>Why teams land here</h4>
            <p>
                Login, onboarding, and workspace creation all stay aligned with the same palette, type scale,
                rounded surfaces, and hover treatment used throughout the rest of the app.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with right_col:
    st.markdown(
        """
        <div class="auth-card">
            <div class="auth-card__header">
                <div>
                    <div class="eyebrow">Authentication</div>
                    <h3>Sign in or create a team workspace</h3>
                    <p>Mock interaction states only. Use the tabs below to preview both flows.</p>
                </div>
                <div class="auth-badge">Secure preview</div>
            </div>
        """,
        unsafe_allow_html=True,
    )

    sign_in_tab, create_tab = st.tabs(["Sign in", "Create account"])

    with sign_in_tab:
        with st.form("sign_in_form", border=False):
            email = st.text_input("Work email", placeholder="alex@company.com")
            password = st.text_input("Password", type="password", placeholder="Enter your password")
            remember_me = st.checkbox("Keep me signed in")

            submit = st.form_submit_button("Sign in", use_container_width=True)

            if submit:
                if email and password:
                    st.success("Mock sign-in complete. No backend request was made.")
                    st.caption(f"Remember me: {'Yes' if remember_me else 'No'}")
                else:
                    st.error("Enter both email and password to continue.")

        st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)
        col_google, col_microsoft = st.columns(2)
        with col_google:
            if st.button("Continue with Google", use_container_width=True):
                st.toast("Mock Google sign-in selected.", icon="◌")
        with col_microsoft:
            if st.button("Continue with Microsoft", use_container_width=True):
                st.toast("Mock Microsoft sign-in selected.", icon="◌")

    with create_tab:
        with st.form("create_account_form", border=False):
            full_name = st.text_input("Full name", placeholder="Alex Rivera")
            work_email = st.text_input("Work email", placeholder="alex@company.com", key="create_email")
            team_size = st.selectbox("Team size", ["1-5 reps", "6-20 reps", "21-50 reps", "50+ reps"])
            use_case = st.selectbox("Primary use case", ["Pipeline coaching", "Deal inspection", "Rep benchmarking", "Executive reporting"])
            password_create = st.text_input("Create password", type="password", placeholder="Choose a secure password")

            submit_create = st.form_submit_button("Create account", use_container_width=True)

            if submit_create:
                if full_name and work_email and password_create:
                    st.success("Mock account creation complete. Your workspace is ready for preview.")
                    st.caption(f"Team size: {team_size} · Use case: {use_case}")
                else:
                    st.error("Fill in your name, email, and password to continue.")

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div style='height: 16px;'></div>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class="auth-card">
            <div class="eyebrow">What this unlocks</div>
            <div class="auth-feature-grid">
                <div class="auth-features">
                    <h4>Behavioral coaching</h4>
                    <p>Surface specific seller actions that correlate with deal momentum.</p>
                </div>
                <div class="auth-features">
                    <h4>Pipeline visibility</h4>
                    <p>Review deal risk, stage health, and follow-up quality in one place.</p>
                </div>
                <div class="auth-features">
                    <h4>Rep performance</h4>
                    <p>Compare habits across sellers and tailor 1:1 coaching with evidence.</p>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


st.markdown("<div style='height: 16px;'></div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    render_stat_chip("Access Mode", "Mock frontend only")
with col2:
    render_stat_chip("Responsive Layout", "Desktop to mobile")
with col3:
    render_stat_chip("Design System", "Matches landing page")


st.markdown(
    """
    <div class="auth-footer">
        <div class="eyebrow">Consistent app experience</div>
        <h3 style="margin:0; font-size:1.4rem;">A focused entry point that looks and feels like the rest of Sales Behavior Intelligence.</h3>
        <p>
            The page uses the same cyan-and-violet glassmorphism language, rounded surfaces, and compact spacing
            from the landing screen so the auth experience remains part of one premium SaaS product.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)