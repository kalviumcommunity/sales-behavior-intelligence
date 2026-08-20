import streamlit as st

from frontend.landing_data import (
    LANDING_BENEFITS,
    LANDING_FAQS,
    LANDING_FEATURES,
    LANDING_LOGOS,
    LANDING_STEPS,
    LANDING_TESTIMONIALS,
)

def render_landing_page():
    st.set_page_config(
        page_title="Sales Behavior Intelligence",
        page_icon="◆",
        layout="wide",
        initial_sidebar_state="collapsed",
    )

    st.html(
        """
        <style>
        /* ─── BASE ─── */
        :root {
            --lp-bg: #060B14;
            --lp-text: #F5F7FB;
            --lp-muted: #8A98B4;
            --lp-cyan: #5EE7FF;
            --lp-violet: #8B7CFF;
        }

        .stApp {
            background-color: var(--lp-bg);
            background-image: 
                radial-gradient(circle at 15% 15%, rgba(94, 231, 255, 0.05), transparent 30%),
                radial-gradient(circle at 85% 85%, rgba(139, 124, 255, 0.05), transparent 30%);
            color: var(--lp-text);
            font-family: 'Inter', sans-serif;
        }

        #MainMenu, header[data-testid="stHeader"], footer, [data-testid="stToolbar"] { display: none !important; }
        section[data-testid="stSidebar"] { display: none !important; }
        .main .block-container {
            max-width: 1320px;
            padding: 0 !important;
            margin: 0 auto;
        }

        /* Prevent Streamlit spacing */
        [data-testid="stVerticalBlock"] > div { gap: 0 !important; }
        [data-testid="stMarkdownContainer"] p { margin: 0 !important; }

        /* ─── NAVBAR ─── */
        .lp-nav {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 24px 32px;
            max-width: 1320px;
            margin: 0 auto;
        }
        .lp-brand {
            display: flex;
            align-items: center;
            gap: 12px;
            font-weight: 700;
            font-size: 16px;
            color: var(--lp-text);
        }
        .lp-brand-icon {
            width: 32px;
            height: 32px;
            background: linear-gradient(135deg, var(--lp-cyan), var(--lp-violet));
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #060B14;
            font-weight: 800;
        }
        .lp-nav-links {
            display: flex;
            gap: 32px;
        }
        .lp-nav-links a {
            color: var(--lp-muted);
            text-decoration: none;
            font-size: 14px;
            font-weight: 500;
            transition: color 0.2s;
        }
        .lp-nav-links a:hover { color: var(--lp-text); }
        
        .lp-nav-actions {
            display: flex;
            align-items: center;
            gap: 16px;
        }

        /* ─── HERO ─── */
        .lp-hero {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 64px;
            padding: 80px 32px;
            align-items: center;
        }
        .lp-eyebrow {
            color: var(--lp-cyan);
            font-size: 12px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.12em;
            margin-bottom: 16px;
        }
        .lp-h1 {
            font-size: clamp(40px, 5vw, 68px);
            font-weight: 800;
            line-height: 1.05;
            letter-spacing: -0.04em;
            margin-bottom: 24px;
            color: var(--lp-text);
        }
        .lp-subtitle {
            font-size: 18px;
            line-height: 1.6;
            color: var(--lp-muted);
            margin-bottom: 40px;
            max-width: 520px;
        }
        .lp-btn-primary {
            background: linear-gradient(135deg, var(--lp-cyan), var(--lp-violet)) !important;
            color: #060B14 !important;
            padding: 14px 28px;
            border-radius: 8px;
            text-decoration: none !important;
            font-weight: 700;
            display: inline-block;
            transition: transform 0.2s;
        }
        .lp-btn-primary:hover { transform: translateY(-2px); }
        
        .lp-btn-secondary {
            border: 1px solid rgba(255,255,255,0.1) !important;
            color: var(--lp-text) !important;
            padding: 14px 28px;
            border-radius: 8px;
            text-decoration: none !important;
            font-weight: 600;
            display: inline-block;
            transition: background 0.2s;
        }
        .lp-btn-secondary:hover { background: rgba(255,255,255,0.05) !important; }

        .lp-hero-features {
            margin-top: 32px;
            display: flex;
            gap: 24px;
            font-size: 13px;
            color: var(--lp-muted);
            font-weight: 500;
        }

        /* ─── PRODUCT PREVIEW ─── */
        .lp-preview {
            background: #0B101A;
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 20px 40px rgba(0,0,0,0.4);
        }
        .lp-preview-header {
            background: rgba(255,255,255,0.02);
            padding: 12px 16px;
            border-bottom: 1px solid rgba(255,255,255,0.05);
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .lp-preview-dot {
            width: 10px;
            height: 10px;
            border-radius: 50%;
            background: #333;
        }
        .lp-preview-dot:nth-child(1) { background: #FF5F56; }
        .lp-preview-dot:nth-child(2) { background: #FFBD2E; }
        .lp-preview-dot:nth-child(3) { background: #27C93F; }
        
        .lp-preview-body { padding: 24px; }
        .lp-preview-card {
            background: rgba(255,255,255,0.02);
            border: 1px solid rgba(255,255,255,0.05);
            border-radius: 8px;
            padding: 16px;
            margin-bottom: 12px;
        }

        /* ─── METRICS STRIP ─── */
        .lp-metrics {
            display: flex;
            justify-content: space-around;
            padding: 64px 32px;
            border-top: 1px solid rgba(255,255,255,0.05);
            border-bottom: 1px solid rgba(255,255,255,0.05);
            background: rgba(255,255,255,0.01);
        }
        .lp-metric { text-align: center; }
        .lp-metric-val { font-size: 32px; font-weight: 800; color: var(--lp-text); margin-bottom: 8px; }
        .lp-metric-lbl { font-size: 13px; color: var(--lp-muted); text-transform: uppercase; letter-spacing: 0.1em; }

        /* ─── SECTION HEADER ─── */
        .lp-section { padding: 96px 32px; }
        .lp-section-header { text-align: center; margin-bottom: 64px; }
        .lp-section-title { font-size: 36px; font-weight: 800; margin-bottom: 16px; letter-spacing: -0.02em; }
        .lp-section-desc { font-size: 18px; color: var(--lp-muted); max-width: 600px; margin: 0 auto; line-height: 1.6; }

        /* ─── FEATURES GRID ─── */
        .lp-features-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 24px;
        }
        .lp-feature {
            padding: 32px;
            background: rgba(255,255,255,0.02);
            border: 1px solid rgba(255,255,255,0.05);
            border-radius: 12px;
            transition: background 0.2s;
        }
        .lp-feature:hover { background: rgba(255,255,255,0.04); }
        .lp-feature-icon {
            font-size: 24px;
            color: var(--lp-cyan);
            margin-bottom: 16px;
        }
        .lp-feature-title { font-size: 18px; font-weight: 700; margin-bottom: 12px; }
        .lp-feature-desc { font-size: 14px; color: var(--lp-muted); line-height: 1.6; }

        /* ─── HOW IT WORKS TIMELINE ─── */
        .lp-timeline {
            display: flex;
            justify-content: space-between;
            gap: 24px;
            position: relative;
        }
        .lp-timeline::before {
            content: '';
            position: absolute;
            top: 24px;
            left: 0;
            right: 0;
            height: 2px;
            background: rgba(255,255,255,0.05);
            z-index: 0;
        }
        .lp-step { flex: 1; position: relative; z-index: 1; }
        .lp-step-num {
            width: 48px;
            height: 48px;
            background: var(--lp-bg);
            border: 2px solid var(--lp-cyan);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 800;
            font-size: 14px;
            margin-bottom: 24px;
        }
        .lp-step-title { font-size: 18px; font-weight: 700; margin-bottom: 12px; }
        .lp-step-desc { font-size: 14px; color: var(--lp-muted); line-height: 1.6; }

        /* ─── RESPONSIVE ─── */
        @media (max-width: 1024px) {
            .lp-hero { grid-template-columns: 1fr; text-align: center; padding: 64px 24px; }
            .lp-subtitle { margin: 0 auto 40px; }
            .lp-hero-features { justify-content: center; }
            .lp-features-grid { grid-template-columns: repeat(2, 1fr); }
            .lp-nav-links { display: none; }
        }
        @media (max-width: 768px) {
            .lp-features-grid { grid-template-columns: 1fr; }
            .lp-timeline { flex-direction: column; }
            .lp-timeline::before {
                top: 0; bottom: 0; left: 24px; width: 2px; height: auto;
            }
            .lp-step { display: flex; gap: 24px; text-align: left; }
            .lp-step-num { margin-bottom: 0; flex-shrink: 0; }
            .lp-metrics { flex-direction: column; gap: 40px; }
        }
        </style>
        """)

    # Note: Streamlit buttons trigger a rerun. For external styling we can use Streamlit session state and switch_page.
    # To keep the marketing page fully styled and handle clicks correctly without jumping, 
    # we use st.button styled via CSS for the auth navigation, or simple logic.

    # ─── NAVBAR ───
    st.html(
        """
        <div class="lp-nav">
            <div class="lp-brand">
                <div class="lp-brand-icon">SBI</div>
                Sales Behavior Intelligence
            </div>
            <div class="lp-nav-links">
                <a href="#product">Product</a>
                <a href="#how-it-works">How it Works</a>
                <a href="#benefits">Insights</a>
            </div>
        </div>
        """)

    # Use actual streamlit buttons for the auth actions so they work, floating them via a container
    col_nav1, col_nav2, col_nav3 = st.columns([1, 8, 2.5])
    with col_nav3:
        sub_c1, sub_c2 = st.columns(2)
        with sub_c1:
            if st.button("Sign In", type="secondary", use_container_width=True):
                st.switch_page("pages/1_Authentication.py")
        with sub_c2:
            if st.button("Get Started", type="primary", use_container_width=True):
                st.switch_page("pages/1_Authentication.py")

    # ─── HERO ───
    st.html(
        """
        <div class="lp-hero">
            <div>
                <div class="lp-eyebrow">Behavioral Intelligence for Revenue Teams</div>
                <div class="lp-h1">Know why deals move.<br>Know what to do next.</div>
                <div class="lp-subtitle">Sales Behavior Intelligence reveals the seller behaviors behind pipeline movement so managers can identify risk earlier, coach with evidence, and repeat the behaviors that create revenue.</div>
                <div style="display: flex; gap: 16px;">
                    <a href="#" class="lp-btn-primary">Start analyzing pipeline</a>
                    <a href="#" class="lp-btn-secondary">Watch Demo</a>
                </div>
                <div class="lp-hero-features">
                    <span>✓ Evidence-driven coaching</span>
                    <span>✓ Early risk detection</span>
                    <span>✓ AI-powered insights</span>
                </div>
            </div>
            <div class="lp-preview">
                <div class="lp-preview-header">
                    <div class="lp-preview-dot"></div>
                    <div class="lp-preview-dot"></div>
                    <div class="lp-preview-dot"></div>
                </div>
                <div class="lp-preview-body">
                    <div class="lp-preview-card" style="border-left: 3px solid var(--lp-cyan);">
                        <div style="font-size: 11px; color: var(--lp-muted); text-transform: uppercase; margin-bottom: 4px;">Pipeline Health</div>
                        <div style="font-size: 24px; font-weight: 800;">$1.84M</div>
                    </div>
                    <div class="lp-preview-card" style="border-left: 3px solid var(--lp-violet);">
                        <div style="font-size: 11px; color: var(--lp-muted); text-transform: uppercase; margin-bottom: 8px;">AI Coaching Insight</div>
                        <div style="font-size: 14px; margin-bottom: 4px; font-weight: 600;">Follow-up timing has increased 28%.</div>
                        <div style="font-size: 13px; color: var(--lp-muted);">Deals with slower follow-up are progressing 1.4x slower.</div>
                    </div>
                    <div class="lp-preview-card" style="border-left: 3px solid #FB7185;">
                        <div style="font-size: 11px; color: var(--lp-muted); text-transform: uppercase; margin-bottom: 8px;">Risk Indicator</div>
                        <div style="font-size: 13px;">Executive stakeholder not engaged in Acme Corp deal.</div>
                    </div>
                </div>
            </div>
        </div>
        """)

    # ─── METRICS STRIP ───
    st.html(
        """
        <div class="lp-metrics">
            <div class="lp-metric">
                <div class="lp-metric-val">$12.4M+</div>
                <div class="lp-metric-lbl">Pipeline Analyzed</div>
            </div>
            <div class="lp-metric">
                <div class="lp-metric-val">1,240+</div>
                <div class="lp-metric-lbl">Deals Monitored</div>
            </div>
            <div class="lp-metric">
                <div class="lp-metric-val">18K+</div>
                <div class="lp-metric-lbl">Behavioral Signals</div>
            </div>
            <div class="lp-metric">
                <div class="lp-metric-val">32%</div>
                <div class="lp-metric-lbl">Manager Time Saved</div>
            </div>
        </div>
        """)

    # ─── FEATURES ───
    features_html = ""
    for f in LANDING_FEATURES:
        features_html += f"""
        <div class="lp-feature">
            <div class="lp-feature-icon">{f['icon']}</div>
            <div class="lp-feature-title">{f['title']}</div>
            <div class="lp-feature-desc">{f['body']}</div>
        </div>
        """

    st.html(
        f"""
        <div id="product" class="lp-section">
            <div class="lp-section-header">
                <div class="lp-section-title">CRM tells you what happened. We tell you why.</div>
                <div class="lp-section-desc">Traditional management relies on manual inspection and late risk detection. Sales Behavior Intelligence delivers early warnings, evidence-based coaching, and continuous intelligence.</div>
            </div>
            <div class="lp-features-grid">
                {features_html}
            </div>
        </div>
        """)

    # ─── HOW IT WORKS ───
    steps_html = ""
    for s in LANDING_STEPS:
        steps_html += f"""
        <div class="lp-step">
            <div class="lp-step-num">{s['step']}</div>
            <div>
                <div class="lp-step-title">{s['title']}</div>
                <div class="lp-step-desc">{s['body']}</div>
            </div>
        </div>
        """

    st.html(
        f"""
        <div id="how-it-works" class="lp-section" style="background: rgba(255,255,255,0.01);">
            <div class="lp-section-header">
                <div class="lp-section-title">From scattered activity to clear signals.</div>
                <div class="lp-section-desc">How Sales Behavior Intelligence works securely with your existing revenue stack.</div>
            </div>
            <div class="lp-timeline">
                {steps_html}
            </div>
        </div>
        """)
    
    # ─── FINAL CTA ───
    st.html(
        """
        <div class="lp-section" style="text-align: center;">
            <div class="lp-section-title">Turn sales activity into better decisions.</div>
            <div style="height: 32px;"></div>
        </div>
        """)
    
    col_cta1, col_cta2, col_cta3 = st.columns([3, 2, 3])
    with col_cta2:
        if st.button("Start analyzing your pipeline", type="primary", use_container_width=True):
            st.switch_page("pages/1_Authentication.py")
        if st.button("Book a demo", type="secondary", use_container_width=True):
            st.toast("Demo request received.")
