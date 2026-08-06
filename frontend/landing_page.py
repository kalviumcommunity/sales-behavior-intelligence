import streamlit as st

from frontend.landing_data import (
    LANDING_BENEFITS,
    LANDING_FAQS,
    LANDING_FEATURES,
    LANDING_LOGOS,
    LANDING_NAV,
    LANDING_QUICK_LINKS,
    LANDING_RESOURCES,
    LANDING_STEPS,
    LANDING_STATS,
    LANDING_TESTIMONIALS,
)


def _section_id(value):
    return value.lower().replace(" ", "-")


def render_landing_page():
    st.set_page_config(
        page_title="Sales Behavior Intelligence",
        page_icon="◼",
        layout="wide",
        initial_sidebar_state="collapsed",
    )

    st.markdown(
        """
        <style>
        :root {
            --bg: #050814;
            --bg-soft: #0a1220;
            --panel: rgba(11, 18, 32, 0.72);
            --panel-strong: rgba(12, 19, 35, 0.9);
            --panel-border: rgba(148, 163, 184, 0.14);
            --text: #eef4ff;
            --muted: #98a5bc;
            --cyan: #57d8ff;
            --violet: #9c84ff;
            --green: #5fd6a0;
            --gold: #f2cf73;
        }

        html {
            scroll-behavior: smooth;
        }

        .stApp {
            background:
                radial-gradient(circle at 10% 10%, rgba(87, 216, 255, 0.14), transparent 24%),
                radial-gradient(circle at 90% 5%, rgba(156, 132, 255, 0.15), transparent 22%),
                linear-gradient(180deg, #040712 0%, #070d18 52%, #04060b 100%);
            color: var(--text);
        }

        .main .block-container {
            padding-top: 0.8rem;
            padding-bottom: 2.6rem;
            max-width: 1440px;
        }

        section[data-testid="stSidebar"] {
            display: none;
        }

        h1, h2, h3, h4, p, span, div, li, label {
            color: var(--text);
        }

        .section-shell,
        .feature-card,
        .trust-pill,
        .step-card,
        .preview-device,
        .benefit-card,
        .testimonial-card,
        .faq-shell,
        .cta-shell,
        .footer-shell,
        .nav-shell,
        .metric-chip {
            border: 1px solid var(--panel-border);
            background: var(--panel);
            border-radius: 28px;
            box-shadow: 0 24px 64px rgba(0, 0, 0, 0.28);
        }

        .nav-shell {
            position: sticky;
            top: 12px;
            z-index: 50;
            margin-bottom: 18px;
            backdrop-filter: blur(18px);
            -webkit-backdrop-filter: blur(18px);
        }

        .nav-inner {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 18px;
            padding: 16px 22px;
        }

        .brand {
            display: flex;
            align-items: center;
            gap: 14px;
            min-width: 0;
        }

        .brand-mark {
            width: 44px;
            height: 44px;
            border-radius: 16px;
            display: grid;
            place-items: center;
            background: linear-gradient(135deg, rgba(87, 216, 255, 0.22), rgba(156, 132, 255, 0.22));
            border: 1px solid rgba(87, 216, 255, 0.18);
            color: var(--text);
            font-weight: 800;
        }

        .brand-name {
            display: grid;
            gap: 2px;
        }

        .brand-name strong {
            font-size: 1rem;
            letter-spacing: -0.02em;
        }

        .brand-name span {
            color: var(--muted);
            font-size: 0.82rem;
        }

        .nav-links {
            display: flex;
            align-items: center;
            gap: 20px;
            flex-wrap: wrap;
        }

        .nav-links a {
            color: var(--muted);
            text-decoration: none;
            font-size: 0.94rem;
            transition: color 0.2s ease;
        }

        .nav-links a:hover {
            color: var(--text);
        }

        .nav-cta {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            padding: 12px 18px;
            border-radius: 999px;
            text-decoration: none;
            color: #071019;
            background: linear-gradient(135deg, var(--cyan), var(--violet));
            font-weight: 800;
            white-space: nowrap;
        }

        .hero-shell {
            position: relative;
            overflow: hidden;
            border: 1px solid var(--panel-border);
            background: linear-gradient(135deg, rgba(11, 18, 32, 0.96), rgba(11, 18, 32, 0.72));
            border-radius: 36px;
            box-shadow: 0 34px 90px rgba(0, 0, 0, 0.4);
            padding: 30px;
        }

        .hero-shell:before {
            content: "";
            position: absolute;
            inset: 0;
            background:
                radial-gradient(circle at 15% 18%, rgba(87, 216, 255, 0.12), transparent 20%),
                radial-gradient(circle at 82% 20%, rgba(156, 132, 255, 0.12), transparent 18%);
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
        }

        .eyebrow:before {
            content: "";
            width: 9px;
            height: 9px;
            border-radius: 999px;
            background: linear-gradient(135deg, var(--cyan), var(--violet));
            box-shadow: 0 0 18px rgba(87, 216, 255, 0.48);
        }

        .hero-grid {
            display: grid;
            grid-template-columns: 1.15fr 0.95fr;
            gap: 28px;
            align-items: center;
        }

        .hero-title {
            margin: 12px 0 16px;
            font-size: clamp(3rem, 7vw, 5.8rem);
            line-height: 0.95;
            letter-spacing: -0.06em;
            max-width: 11ch;
        }

        .hero-copy {
            max-width: 700px;
            color: var(--muted);
            font-size: 1.06rem;
            line-height: 1.75;
            margin-bottom: 26px;
        }

        .cta-row {
            display: flex;
            flex-wrap: wrap;
            gap: 14px;
            margin-bottom: 24px;
        }

        .cta-button,
        .cta-button-secondary {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            padding: 14px 22px;
            border-radius: 999px;
            text-decoration: none;
            font-weight: 800;
            font-size: 0.96rem;
        }

        .cta-button {
            color: #071019;
            background: linear-gradient(135deg, var(--cyan), var(--violet));
        }

        .cta-button-secondary {
            color: var(--text);
            border: 1px solid rgba(148, 163, 184, 0.2);
            background: rgba(255, 255, 255, 0.04);
        }

        .metric-row {
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 12px;
            max-width: 560px;
        }

        .metric-chip {
            padding: 14px 16px;
        }

        .metric-chip strong {
            display: block;
            font-size: 1.45rem;
            margin-bottom: 4px;
        }

        .metric-chip span {
            color: var(--muted);
            font-size: 0.84rem;
        }

        .mockup {
            position: relative;
            padding: 18px;
            border-radius: 30px;
            background: linear-gradient(180deg, rgba(10, 16, 31, 0.88), rgba(9, 13, 24, 0.84));
            border: 1px solid rgba(148, 163, 184, 0.14);
            box-shadow: 0 28px 80px rgba(0, 0, 0, 0.42);
        }

        .mockup-top {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 12px;
            margin-bottom: 16px;
        }

        .mockup-dots {
            display: flex;
            gap: 6px;
        }

        .mockup-dots span {
            width: 10px;
            height: 10px;
            border-radius: 999px;
            background: rgba(255, 255, 255, 0.18);
        }

        .mockup-panel {
            display: grid;
            gap: 12px;
        }

        .mockup-stage,
        .mockup-chart,
        .mockup-insight {
            border-radius: 22px;
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(148, 163, 184, 0.12);
            padding: 16px;
        }

        .mockup-stage {
            display: grid;
            gap: 10px;
        }

        .mockup-stage__title {
            font-size: 0.82rem;
            letter-spacing: 0.14em;
            text-transform: uppercase;
            color: var(--muted);
        }

        .mockup-stage__value {
            font-size: 1.5rem;
            font-weight: 800;
        }

        .mockup-bars {
            display: grid;
            gap: 10px;
        }

        .mockup-bar {
            display: grid;
            gap: 6px;
        }

        .mockup-bar span {
            color: var(--muted);
            font-size: 0.82rem;
        }

        .mockup-track {
            height: 10px;
            border-radius: 999px;
            background: rgba(255, 255, 255, 0.06);
            overflow: hidden;
        }

        .mockup-fill {
            height: 100%;
            border-radius: inherit;
            background: linear-gradient(135deg, var(--cyan), var(--violet));
        }

        .section-heading {
            max-width: 760px;
            margin-bottom: 28px;
        }

        .section-heading h2 {
            font-size: clamp(2rem, 4vw, 3.5rem);
            letter-spacing: -0.05em;
            line-height: 1.02;
            margin: 10px 0 14px;
        }

        .section-heading p {
            color: var(--muted);
            font-size: 1.02rem;
            line-height: 1.75;
        }

        .trusted-row {
            display: grid;
            grid-template-columns: repeat(6, minmax(0, 1fr));
            gap: 14px;
        }

        .trust-pill {
            padding: 20px 18px;
            text-align: center;
            color: var(--muted);
            font-weight: 700;
            letter-spacing: 0.02em;
        }

        .feature-grid {
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 16px;
        }

        .feature-card {
            padding: 24px;
            min-height: 220px;
        }

        .feature-icon {
            width: 52px;
            height: 52px;
            border-radius: 18px;
            display: grid;
            place-items: center;
            background: linear-gradient(135deg, rgba(87, 216, 255, 0.16), rgba(156, 132, 255, 0.16));
            border: 1px solid rgba(87, 216, 255, 0.18);
            margin-bottom: 20px;
            font-size: 1.1rem;
        }

        .feature-card h3 {
            font-size: 1.3rem;
            margin: 0 0 10px;
        }

        .feature-card p {
            color: var(--muted);
            line-height: 1.7;
            margin: 0;
        }

        .steps-row {
            display: grid;
            grid-template-columns: repeat(4, minmax(0, 1fr));
            gap: 16px;
            align-items: stretch;
        }

        .step-card {
            padding: 22px;
            position: relative;
        }

        .step-card:after {
            content: "↓";
            position: absolute;
            right: -10px;
            top: 50%;
            transform: translateY(-50%);
            color: rgba(255, 255, 255, 0.22);
            font-size: 1.2rem;
        }

        .step-card:last-child:after {
            display: none;
        }

        .step-card__num {
            color: var(--cyan);
            font-weight: 800;
            letter-spacing: 0.14em;
            text-transform: uppercase;
            font-size: 0.74rem;
        }

        .step-card h3 {
            margin: 14px 0 10px;
            font-size: 1.28rem;
        }

        .step-card p {
            color: var(--muted);
            line-height: 1.7;
            margin: 0;
        }

        .preview-grid {
            display: grid;
            grid-template-columns: 1.2fr 0.8fr;
            gap: 18px;
            align-items: center;
        }

        .preview-device {
            padding: 22px;
            background: linear-gradient(180deg, rgba(12, 18, 33, 0.96), rgba(8, 12, 22, 0.92));
        }

        .preview-surface {
            border-radius: 26px;
            padding: 22px;
            background:
                radial-gradient(circle at top right, rgba(156, 132, 255, 0.2), transparent 22%),
                radial-gradient(circle at top left, rgba(87, 216, 255, 0.16), transparent 24%),
                rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(148, 163, 184, 0.12);
        }

        .preview-header {
            display: flex;
            justify-content: space-between;
            gap: 16px;
            align-items: center;
            margin-bottom: 18px;
        }

        .preview-title {
            font-size: 1.4rem;
            font-weight: 800;
        }

        .preview-status {
            color: #071019;
            background: linear-gradient(135deg, var(--gold), #ffdca4);
            border-radius: 999px;
            padding: 8px 12px;
            font-size: 0.8rem;
            font-weight: 800;
        }

        .preview-grid-mini {
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 12px;
            margin-bottom: 16px;
        }

        .preview-mini {
            border-radius: 18px;
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(148, 163, 184, 0.12);
            padding: 14px;
        }

        .preview-mini span {
            display: block;
            color: var(--muted);
            font-size: 0.82rem;
            margin-bottom: 6px;
        }

        .preview-mini strong {
            font-size: 1.1rem;
        }

        .preview-chart {
            display: grid;
            gap: 10px;
        }

        .preview-chart__bar {
            height: 12px;
            border-radius: 999px;
            background: linear-gradient(90deg, rgba(87, 216, 255, 0.22), rgba(156, 132, 255, 0.18));
            position: relative;
            overflow: hidden;
        }

        .preview-chart__bar:after {
            content: "";
            position: absolute;
            inset: 0;
            width: 70%;
            background: linear-gradient(90deg, var(--cyan), var(--violet));
            border-radius: inherit;
        }

        .preview-insight {
            padding: 24px;
            display: grid;
            gap: 16px;
        }

        .preview-insight h3 {
            margin: 0;
            font-size: 1.7rem;
        }

        .preview-insight p {
            color: var(--muted);
            line-height: 1.8;
            margin: 0;
        }

        .benefit-grid {
            display: grid;
            grid-template-columns: repeat(2, minmax(0, 1fr));
            gap: 16px;
        }

        .benefit-card {
            padding: 26px;
        }

        .benefit-card h3 {
            margin: 0 0 16px;
            font-size: 1.3rem;
        }

        .benefit-card ul {
            margin: 0;
            padding-left: 20px;
            color: var(--muted);
            line-height: 1.8;
        }

        .benefit-card li + li {
            margin-top: 12px;
        }

        .testimonial-grid {
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 16px;
        }

        .testimonial-card {
            padding: 24px;
            min-height: 220px;
            display: grid;
            align-content: space-between;
        }

        .testimonial-card p {
            font-size: 1.04rem;
            line-height: 1.8;
            margin: 0 0 18px;
            color: #dfe7f6;
        }

        .testimonial-card strong {
            display: block;
            margin-bottom: 4px;
        }

        .faq-shell {
            padding: 26px;
        }

        .faq-item {
            border-bottom: 1px solid rgba(148, 163, 184, 0.12);
            padding: 6px 0;
        }

        .faq-item summary {
            cursor: pointer;
            list-style: none;
            font-weight: 700;
            font-size: 1.02rem;
            padding: 16px 0;
        }

        .faq-item summary::-webkit-details-marker {
            display: none;
        }

        .faq-item p {
            color: var(--muted);
            line-height: 1.8;
            margin: 0 0 16px;
        }

        .cta-shell {
            padding: 36px;
            text-align: center;
            background:
                radial-gradient(circle at top, rgba(87, 216, 255, 0.16), transparent 28%),
                radial-gradient(circle at right, rgba(156, 132, 255, 0.14), transparent 26%),
                rgba(255, 255, 255, 0.03);
        }

        .cta-shell h2 {
            font-size: clamp(2rem, 4vw, 3.8rem);
            letter-spacing: -0.05em;
            margin: 0 0 14px;
        }

        .cta-shell p {
            color: var(--muted);
            line-height: 1.8;
            max-width: 760px;
            margin: 0 auto 24px;
        }

        .footer-shell {
            padding: 28px;
            margin-top: 18px;
        }

        .footer-grid {
            display: grid;
            grid-template-columns: 1.2fr repeat(3, 0.7fr);
            gap: 20px;
        }

        .footer-title {
            font-size: 1.02rem;
            margin-bottom: 12px;
            font-weight: 800;
        }

        .footer-shell a {
            color: var(--muted);
            text-decoration: none;
            display: block;
            margin-bottom: 10px;
        }

        .footer-shell a:hover {
            color: var(--text);
        }

        .footer-note {
            margin-top: 24px;
            padding-top: 18px;
            border-top: 1px solid rgba(148, 163, 184, 0.12);
            color: var(--muted);
            display: flex;
            justify-content: space-between;
            gap: 12px;
            flex-wrap: wrap;
        }

        .social-row {
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
        }

        .social-chip {
            width: 36px;
            height: 36px;
            border-radius: 999px;
            display: grid;
            place-items: center;
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid rgba(148, 163, 184, 0.12);
            color: var(--text);
        }

        .section-space {
            height: 26px;
        }

        @media (max-width: 1200px) {
            .hero-grid,
            .preview-grid,
            .footer-grid {
                grid-template-columns: 1fr;
            }

            .feature-grid,
            .testimonial-grid,
            .benefit-grid {
                grid-template-columns: repeat(2, minmax(0, 1fr));
            }

            .trusted-row,
            .steps-row {
                grid-template-columns: repeat(3, minmax(0, 1fr));
            }
        }

        @media (max-width: 780px) {
            .nav-inner {
                align-items: flex-start;
                flex-direction: column;
            }

            .nav-links {
                gap: 14px;
            }

            .hero-shell,
            .cta-shell,
            .footer-shell,
            .faq-shell,
            .preview-device {
                padding: 20px;
            }

            .hero-title {
                max-width: none;
            }

            .metric-row,
            .feature-grid,
            .testimonial-grid,
            .benefit-grid,
            .trusted-row,
            .steps-row,
            .preview-grid-mini {
                grid-template-columns: 1fr;
            }

            .step-card:after {
                display: none;
            }

            .cta-row {
                flex-direction: column;
            }

            .cta-button,
            .cta-button-secondary,
            .nav-cta {
                width: 100%;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    nav_links_html = "".join(f'<a href="#{_section_id(item)}">{item}</a>' for item in LANDING_NAV)

    st.markdown(
        f"""
        <div class="nav-shell">
            <div class="nav-inner">
                <div class="brand">
                    <div class="brand-mark">◼</div>
                    <div class="brand-name">
                        <strong>Sales Behavior Intelligence</strong>
                        <span>Understand why deals win or lose</span>
                    </div>
                </div>
                <div class="nav-links">
                    {nav_links_html}
                </div>
                <a class="nav-cta" href="#get-started">Get Started</a>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="hero-shell">
            <div class="hero-grid">
                <div>
                    <div class="eyebrow">Behavioral intelligence for revenue teams</div>
                    <h1 class="hero-title">Understand why your sales team wins or loses deals.</h1>
                    <p class="hero-copy">
                        Sales Behavior Intelligence reveals the behaviors behind pipeline movement so managers can coach with evidence,
                        spot deal risk earlier, and scale the habits that actually create revenue.
                        It turns CRM activity, conversations, and stage changes into a premium operating system for coaching.
                    </p>
                    <div class="cta-row">
                        <a class="cta-button" href="#get-started">Get Started</a>
                        <a class="cta-button-secondary" href="#product-preview">Watch Demo</a>
                    </div>
                    <div class="metric-row">
                        """
        ,
        unsafe_allow_html=True,
    )

    for metric in LANDING_STATS:
        st.markdown(
            f"""
            <div class="metric-chip">
                <strong>{metric['value']}</strong>
                <span>{metric['label']}</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        """
                    </div>
                </div>
                <div>
                    <div class="mockup">
                        <div class="mockup-top">
                            <div class="mockup-dots"><span></span><span></span><span></span></div>
                            <div class="eyebrow">Premium product preview</div>
                        </div>
                        <div class="mockup-panel">
                            <div class="mockup-stage">
                                <div class="mockup-stage__title">Active pipeline health</div>
                                <div class="mockup-stage__value">$1.84M at risk-aware visibility</div>
                            </div>
                            <div class="mockup-grid">
                                <div class="mockup-chart">
                                    <div class="mockup-stage__title">Revenue trend</div>
                                    <div class="mockup-bars" style="margin-top: 12px;">
                                        <div class="mockup-bar"><span>Q1</span><div class="mockup-track"><div class="mockup-fill" style="width: 58%;"></div></div></div>
                                        <div class="mockup-bar"><span>Q2</span><div class="mockup-track"><div class="mockup-fill" style="width: 76%;"></div></div></div>
                                        <div class="mockup-bar"><span>Q3</span><div class="mockup-track"><div class="mockup-fill" style="width: 89%;"></div></div></div>
                                    </div>
                                </div>
                                <div class="mockup-insight">
                                    <div class="mockup-stage__title">Latest coaching cue</div>
                                    <div class="mockup-stage__value" style="font-size: 1.1rem;">Add finance stakeholder before proposal.</div>
                                    <div class="mockup-stage__title">96% confidence</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<div class='section-space'></div>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class="section-heading" id="trusted-by">
            <div class="eyebrow">Trusted by modern revenue teams</div>
            <h2>Designed to feel like a premium operating layer, not another internal dashboard.</h2>
            <p>Placeholder logos keep the focus on the product story while signaling the kind of teams this is built for.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    trusted_cols = st.columns(6)
    for column, logo in zip(trusted_cols, LANDING_LOGOS):
        with column:
            st.markdown(f"<div class='trust-pill'>{logo}</div>", unsafe_allow_html=True)

    st.markdown("<div class='section-space'></div>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class="section-heading" id="features">
            <div class="eyebrow">Features</div>
            <h2>Everything managers need to understand deal outcomes at a glance.</h2>
            <p>Each capability is focused on one job: connect behavior to revenue so managers know what to coach next.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    feature_cols = st.columns(3)
    for index, feature in enumerate(LANDING_FEATURES):
        with feature_cols[index % 3]:
            st.markdown(
                f"""
                <div class="feature-card">
                    <div class="feature-icon">{feature['icon']}</div>
                    <h3>{feature['title']}</h3>
                    <p>{feature['body']}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )
        if index % 3 == 2 and index < len(LANDING_FEATURES) - 1:
            feature_cols = st.columns(3)

    st.markdown("<div class='section-space'></div>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class="section-heading" id="solutions">
            <div class="eyebrow">How it works</div>
            <h2>A simple four-step flow from data to coaching action.</h2>
            <p>The product is intentionally easy to explain: connect the data, interpret the behavior, and coach with confidence.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    step_cols = st.columns(4)
    for column, step in zip(step_cols, LANDING_STEPS):
        with column:
            st.markdown(
                f"""
                <div class="step-card">
                    <div class="step-card__num">{step['step']}</div>
                    <h3>{step['title']}</h3>
                    <p>{step['body']}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown("<div class='section-space'></div>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class="section-heading" id="product-preview">
            <div class="eyebrow">Product preview</div>
            <h2>A beautiful preview of the product, without exposing the full dashboard on the landing page.</h2>
            <p>The mockup shows enough of the experience to spark interest while keeping the actual app experience behind login.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="preview-grid">
            <div class="preview-device">
                <div class="preview-surface">
                    <div class="preview-header">
                        <div>
                            <div class="eyebrow">Sales intelligence preview</div>
                            <div class="preview-title">Manager command center</div>
                        </div>
                        <div class="preview-status">Live signal</div>
                    </div>
                    <div class="preview-grid-mini">
                        <div class="preview-mini"><span>Total Pipeline</span><strong>$1.84M</strong></div>
                        <div class="preview-mini"><span>High Risk Deals</span><strong>5</strong></div>
                        <div class="preview-mini"><span>Coaching Alerts</span><strong>12</strong></div>
                    </div>
                    <div class="preview-chart">
                        <div class="preview-chart__bar"></div>
                        <div class="preview-chart__bar" style="opacity: 0.78;"></div>
                        <div class="preview-chart__bar" style="opacity: 0.6;"></div>
                    </div>
                </div>
            </div>
            <div class="preview-insight">
                <div class="eyebrow">Why teams adopt it</div>
                <h3>It explains performance in a language managers can act on immediately.</h3>
                <p>
                    The interface is built to feel calm, premium, and credible. Instead of overwhelming visitors with dense widgets,
                    it shows just enough structure to communicate the product value in seconds.
                </p>
                <p>
                    This preview mirrors the dashboard experience after login, but remains intentionally simplified for the public site.
                </p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<div class='section-space'></div>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class="section-heading" id="about">
            <div class="eyebrow">Benefits</div>
            <h2>What changes when behavior is visible.</h2>
            <p>A quick comparison that shows how the product changes the manager workflow from reactive to evidence-led.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    benefit_cols = st.columns(2)
    for column, benefit in zip(benefit_cols, LANDING_BENEFITS):
        with column:
            items = "".join(f"<li>{item}</li>" for item in benefit["items"])
            st.markdown(
                f"""
                <div class="benefit-card">
                    <h3>{benefit['label']}</h3>
                    <ul>{items}</ul>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown("<div class='section-space'></div>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class="section-heading">
            <div class="eyebrow">Testimonials</div>
            <h2>Built for teams that want coaching to feel clear, fast, and repeatable.</h2>
        </div>
        """,
        unsafe_allow_html=True,
    )

    testimonial_cols = st.columns(3)
    for column, testimonial in zip(testimonial_cols, LANDING_TESTIMONIALS):
        with column:
            st.markdown(
                f"""
                <div class="testimonial-card">
                    <div>
                        <p>“{testimonial['quote']}”</p>
                    </div>
                    <div>
                        <strong>{testimonial['name']}</strong>
                        <span>{testimonial['role']}</span>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown("<div class='section-space'></div>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class="section-heading" id="contact">
            <div class="eyebrow">FAQ</div>
            <h2>Questions answered before the first demo.</h2>
        </div>
        """,
        unsafe_allow_html=True,
    )

    faq_html = "".join(
        f"""
        <details class="faq-item">
            <summary>{faq['question']}</summary>
            <p>{faq['answer']}</p>
        </details>
        """
        for faq in LANDING_FAQS
    )

    st.markdown(f"<div class='faq-shell'>{faq_html}</div>", unsafe_allow_html=True)

    st.markdown("<div class='section-space'></div>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class="cta-shell" id="get-started">
            <div class="eyebrow">Final call to action</div>
            <h2>Start coaching from evidence, not guesswork.</h2>
            <p>
                Give managers a premium layer of behavioral intelligence that turns deal signals into better coaching, faster intervention,
                and more predictable revenue.
            </p>
            <div class="cta-row" style="justify-content: center; margin-bottom: 0;">
                <a class="cta-button" href="pages/1_Authentication.py">Get Started</a>
                <a class="cta-button-secondary" href="#trusted-by">Explore the product</a>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    footer_quick = "".join(f"<a href='#{_section_id(item)}'>{item}</a>" for item in LANDING_QUICK_LINKS)
    footer_resources = "".join(f"<a href='#{_section_id(item)}'>{item}</a>" for item in LANDING_RESOURCES)

    st.markdown(
        f"""
        <div class="footer-shell">
            <div class="footer-grid">
                <div>
                    <div class="brand" style="margin-bottom: 14px;">
                        <div class="brand-mark">◼</div>
                        <div class="brand-name">
                            <strong>Sales Behavior Intelligence</strong>
                            <span>Premium behavioral coaching for modern sales teams</span>
                        </div>
                    </div>
                    <p style="color: var(--muted); line-height: 1.8; margin: 0; max-width: 380px;">
                        Understand why deals win or lose with a clear behavioral layer on top of your CRM and communication data.
                    </p>
                </div>
                <div>
                    <div class="footer-title">Quick Links</div>
                    {footer_quick}
                </div>
                <div>
                    <div class="footer-title">Resources</div>
                    {footer_resources}
                </div>
                <div>
                    <div class="footer-title">Social</div>
                    <div class="social-row">
                        <div class="social-chip">x</div>
                        <div class="social-chip">in</div>
                        <div class="social-chip">gh</div>
                    </div>
                </div>
            </div>
            <div class="footer-note">
                <span>© 2026 Sales Behavior Intelligence. All rights reserved.</span>
                <span>Dark premium SaaS landing page concept.</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
