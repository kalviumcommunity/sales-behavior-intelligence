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
        [data-testid="stAppViewContainer"] > section.main, section[data-testid="stMain"] { padding-top: 0 !important; }
        .main .block-container, [data-testid="stMainBlockContainer"], .block-container {
            max-width: 1320px;
            padding-top: 0 !important;
            margin-top: 0 !important;
            padding-left: 0 !important;
            padding-right: 0 !important;
            margin: 0 auto;
        }

        /* Prevent Streamlit spacing */
        [data-testid="stVerticalBlock"] > div { gap: 0 !important; }
        [data-testid="stMarkdownContainer"] p { margin: 0 !important; }

        /* ─── ANIMATIONS ─── */
        @keyframes lpSlideDown {
            0% { transform: translateY(-100%); }
            100% { transform: translateY(0); }
        }
        @keyframes lpFadeInUp {
            0% { opacity: 0; transform: translateY(30px); }
            100% { opacity: 1; transform: translateY(0); }
        }
        @keyframes lpFadeInRight {
            0% { opacity: 0; transform: translateX(40px); }
            100% { opacity: 1; transform: translateX(0); }
        }

        .anim-slide-down { animation: lpSlideDown 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards; }
        
        .anim-fade-up { opacity: 0; animation: lpFadeInUp 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards; }
        .anim-fade-right { opacity: 0; animation: lpFadeInRight 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards; }
        
        .delay-100 { animation-delay: 100ms; }
        .delay-200 { animation-delay: 200ms; }
        .delay-300 { animation-delay: 300ms; }
        .delay-400 { animation-delay: 400ms; }
        .delay-500 { animation-delay: 500ms; }
        .delay-600 { animation-delay: 600ms; }
        .delay-700 { animation-delay: 700ms; }

        /* ─── NAVBAR ─── */
        .lp-nav-wrapper {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            z-index: 9999;
            background: rgba(6, 11, 20, 0.85);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border-bottom: 1px solid rgba(255,255,255,0.05);
            /* animation added in HTML */
        }
        .lp-nav {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 16px 32px;
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
            padding: 110px 32px 80px; /* 64px for navbar + 46px actual visible gap */
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

    # ─── NAVBAR & HERO ───
    st.html(
        """
        <div class="lp-nav-wrapper anim-slide-down">
            <div class="lp-nav">
                <div class="lp-brand">
                    <div class="lp-brand-icon">SBI</div>
                    Sales Behavior Intelligence
                </div>
                <div class="lp-nav-actions">
                    <div class="lp-nav-links" style="margin-right: 16px;">
                        <a href="#product">Product</a>
                        <a href="#how-it-works">How it Works</a>
                        <a href="#benefits">Insights</a>
                    </div>
                    <a href="Authentication" target="_self" class="lp-btn-secondary" style="padding: 10px 24px; font-size: 14px;">Sign In</a>
                    <a href="Authentication" target="_self" class="lp-btn-primary" style="padding: 10px 24px; font-size: 14px;">Get Started</a>
                </div>
            </div>
        </div>

        <div class="lp-hero">
            <div>
                <div class="lp-eyebrow anim-fade-up">Behavioral Intelligence for Revenue Teams</div>
                <div class="lp-h1 anim-fade-up delay-100">Know why deals move.<br>Know what to do next.</div>
                <div class="lp-subtitle anim-fade-up delay-200">Sales Behavior Intelligence reveals the seller behaviors behind pipeline movement so managers can identify risk earlier, coach with evidence, and repeat the behaviors that create revenue.</div>
                <div style="display: flex; gap: 16px;" class="anim-fade-up delay-300">
                    <a href="#" class="lp-btn-primary">Start analyzing pipeline</a>
                    <a href="#" class="lp-btn-secondary">Watch Demo</a>
                </div>
                <div class="lp-hero-features anim-fade-up delay-400">
                    <span>✓ Evidence-driven coaching</span>
                    <span>✓ Early risk detection</span>
                    <span>✓ AI-powered insights</span>
                </div>
            </div>
            <div class="lp-preview anim-fade-right delay-200">
                <div class="lp-preview-header">
                    <div class="lp-preview-dot"></div>
                    <div class="lp-preview-dot"></div>
                    <div class="lp-preview-dot"></div>
                </div>
                <div class="lp-preview-body">
                    <div class="lp-preview-card anim-fade-up delay-400" style="border-left: 3px solid var(--lp-cyan);">
                        <div style="font-size: 11px; color: var(--lp-muted); text-transform: uppercase; margin-bottom: 4px;">Pipeline Health</div>
                        <div style="font-size: 24px; font-weight: 800;">$1.84M</div>
                    </div>
                    <div class="lp-preview-card anim-fade-up delay-500" style="border-left: 3px solid var(--lp-violet);">
                        <div style="font-size: 11px; color: var(--lp-muted); text-transform: uppercase; margin-bottom: 8px;">AI Coaching Insight</div>
                        <div style="font-size: 14px; margin-bottom: 4px; font-weight: 600;">Follow-up timing has increased 28%.</div>
                        <div style="font-size: 13px; color: var(--lp-muted);">Deals with slower follow-up are progressing 1.4x slower.</div>
                    </div>
                    <div class="lp-preview-card anim-fade-up delay-600" style="border-left: 3px solid #FB7185;">
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
    st.html("""
    <style>
    .lp-cta-section {
        position: relative;
        padding: 120px 32px;
        text-align: center;
        overflow: hidden;
        border-top: 1px solid rgba(255,255,255,0.05);
    }
    .lp-cta-glow {
        position: absolute;
        inset: 0;
        background:
            radial-gradient(ellipse at 50% 60%, rgba(94,231,255,0.07) 0%, transparent 55%),
            radial-gradient(ellipse at 50% 40%, rgba(139,124,255,0.05) 0%, transparent 45%);
        pointer-events: none;
        z-index: 0;
    }
    .lp-cta-inner {
        position: relative;
        z-index: 1;
        max-width: 960px;
        margin: 0 auto;
    }
    .lp-cta-eyebrow {
        font-size: 11px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.14em;
        color: var(--lp-cyan);
        margin-bottom: 20px;
        opacity: 0.85;
    }
    .lp-cta-headline {
        font-size: clamp(36px, 4vw, 52px);
        font-weight: 800;
        line-height: 1.07;
        letter-spacing: -0.035em;
        color: var(--lp-text);
        margin-bottom: 20px;
    }
    .lp-cta-sub {
        font-size: 17px;
        line-height: 1.65;
        color: var(--lp-muted);
        max-width: 620px;
        margin: 0 auto 40px;
    }
    .lp-cta-buttons {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 12px;
        flex-wrap: wrap;
        margin-bottom: 40px;
    }
    .lp-cta-btn-primary {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: linear-gradient(135deg, var(--lp-cyan), var(--lp-violet));
        color: #060B14 !important;
        font-weight: 700;
        font-size: 15px;
        padding: 0 28px;
        height: 50px;
        border-radius: 8px;
        text-decoration: none !important;
        border: none;
        cursor: pointer;
        transition: transform 0.2s, box-shadow 0.2s;
        box-shadow: 0 4px 20px rgba(94,231,255,0.18);
    }
    .lp-cta-btn-primary:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 28px rgba(94,231,255,0.28);
    }
    .lp-cta-btn-secondary {
        display: inline-flex;
        align-items: center;
        height: 50px;
        padding: 0 24px;
        border-radius: 8px;
        border: 1px solid rgba(255,255,255,0.12);
        background: rgba(255,255,255,0.03);
        color: var(--lp-text) !important;
        font-weight: 600;
        font-size: 15px;
        text-decoration: none !important;
        cursor: pointer;
        transition: background 0.2s, border-color 0.2s;
    }
    .lp-cta-btn-secondary:hover {
        background: rgba(255,255,255,0.07);
        border-color: rgba(255,255,255,0.22);
    }
    .lp-cta-trust {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 6px;
        font-size: 12px;
        color: var(--lp-muted);
        opacity: 0.7;
        flex-wrap: wrap;
    }
    .lp-cta-trust-dot {
        width: 3px;
        height: 3px;
        border-radius: 50%;
        background: var(--lp-muted);
        opacity: 0.5;
        display: inline-block;
    }
    @media (max-width: 640px) {
        .lp-cta-section { padding: 80px 20px; }
        .lp-cta-buttons { flex-direction: column; align-items: stretch; }
        .lp-cta-btn-primary, .lp-cta-btn-secondary {
            justify-content: center;
            width: 100%;
            max-width: 340px;
            margin: 0 auto;
        }
    }
    </style>

    <div class="lp-cta-section">
        <div class="lp-cta-glow"></div>
        <div class="lp-cta-inner">
            <div class="lp-cta-eyebrow">Ready to see your pipeline differently</div>
            <div class="lp-cta-headline">
                Turn sales activity into<br>better decisions.
            </div>
            <div class="lp-cta-sub">
                Turn CRM activity, deal behavior, and seller signals into clear actions your team can take today. Understand what is happening, why it is happening, and what to do next.
            </div>
            <div class="lp-cta-buttons">
                <a href="#" class="lp-cta-btn-primary" onclick="window.parent.document.querySelector('[data-testid=\\"stSidebarNav\\"]')">
                    Start analyzing your pipeline →
                </a>
                <a href="#" class="lp-cta-btn-secondary">
                    Book a demo
                </a>
            </div>
            <div class="lp-cta-trust">
                <span>Built for modern revenue teams</span>
                <span class="lp-cta-trust-dot"></span>
                <span>Behavioral intelligence</span>
                <span class="lp-cta-trust-dot"></span>
                <span>Deal risk detection</span>
                <span class="lp-cta-trust-dot"></span>
                <span>AI coaching</span>
            </div>
        </div>
    </div>
    """)
