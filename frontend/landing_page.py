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
            padding-top: 1.5rem;
            padding-bottom: 4rem;
            max-width: 1280px;
            margin: 0 auto;
            padding-left: 32px;
            padding-right: 32px;
        }

        @media (max-width: 1024px) {
            .main .block-container {
                padding-left: 24px;
                padding-right: 24px;
            }
        }

        @media (max-width: 640px) {
            .main .block-container {
                padding-left: 20px;
                padding-right: 20px;
                padding-top: 1rem;
                padding-bottom: 3rem;
            }
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
            top: 0;
            z-index: 50;
            margin-bottom: 48px;
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border: 1px solid rgba(148, 163, 184, 0.08);
            background: rgba(5, 8, 20, 0.8);
        }

        .nav-inner {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 32px;
            padding: 16px 32px;
            max-width: 1280px;
            margin: 0 auto;
        }

        @media (max-width: 1024px) {
            .nav-inner {
                padding: 16px 24px;
            }
        }

        @media (max-width: 768px) {
            .nav-inner {
                gap: 16px;
                padding: 12px 20px;
            }

            .nav-links {
                display: none;
            }
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
            overflow: visible;
            border: none;
            background: transparent;
            border-radius: 0;
            box-shadow: none;
            padding: 60px 0;
        }

        .hero-shell:before {
            display: none;
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
            grid-template-columns: 1fr 1fr;
            gap: 80px;
            align-items: center;
        }

        .hero-title {
            margin: 16px 0 24px;
            font-size: clamp(48px, 6vw, 72px);
            line-height: 1.1;
            letter-spacing: -0.03em;
            max-width: 650px;
            color: var(--text) !important;
            font-weight: 700;
        }

        .hero-copy {
            max-width: 580px;
            color: var(--muted) !important;
            font-size: 18px;
            line-height: 1.6;
            margin-bottom: 32px;
        }

        @media (max-width: 1280px) {
            .hero-grid {
                gap: 60px;
            }
        }

        @media (max-width: 1024px) {
            .hero-grid {
                grid-template-columns: 1fr;
                gap: 48px;
            }

            .hero-title {
                font-size: 48px;
            }
        }

        .cta-row {
            display: flex;
            flex-wrap: wrap;
            gap: 16px;
            margin-bottom: 32px;
        }

        .cta-button,
        .cta-button-secondary {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            padding: 12px 28px;
            border-radius: 8px;
            text-decoration: none;
            font-weight: 600;
            font-size: 15px;
            height: 48px;
            transition: all 0.2s ease;
        }

        .cta-button {
            color: #fff;
            background: linear-gradient(135deg, #2563eb, #7c3aed);
            border: 1px solid transparent;
        }

        .cta-button:hover {
            opacity: 0.9;
            transform: translateY(-2px);
        }

        .cta-button-secondary {
            color: var(--text);
            border: 1px solid rgba(148, 163, 184, 0.3);
            background: transparent;
        }

        .cta-button-secondary:hover {
            border-color: rgba(148, 163, 184, 0.6);
            background: rgba(255, 255, 255, 0.05);
        }

        @media (max-width: 640px) {
            .cta-row {
                flex-direction: column;
            }

            .cta-button,
            .cta-button-secondary {
                width: 100%;
            }
        }

        .metric-row {
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 16px;
            max-width: 500px;
        }

        .metric-chip {
            padding: 16px 20px;
            border-radius: 12px;
            border: 1px solid rgba(148, 163, 184, 0.15);
            background: rgba(11, 18, 32, 0.5);
        }

        .metric-chip strong {
            display: block;
            font-size: 24px;
            margin-bottom: 6px;
            font-weight: 700;
        }

        .metric-chip span {
            color: var(--muted);
            font-size: 12px;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            line-height: 1.4;
        }

        @media (max-width: 640px) {
            .metric-row {
                grid-template-columns: repeat(2, 1fr);
            }
        }

        .mockup {
            position: relative;
            padding: 24px;
            border-radius: 16px;
            background: linear-gradient(135deg, rgba(15, 23, 42, 0.8), rgba(15, 23, 42, 0.6));
            border: 1px solid rgba(148, 163, 184, 0.12);
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
        }

        .mockup-top {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 12px;
            margin-bottom: 20px;
        }

        .mockup-dots {
            display: flex;
            gap: 8px;
        }

        .mockup-dots span {
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.15);
        }

        .mockup-panel {
            display: grid;
            gap: 16px;
        }

        .mockup-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 16px;
        }

        .mockup-stage,
        .mockup-chart,
        .mockup-insight {
            border-radius: 12px;
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid rgba(148, 163, 184, 0.1);
            padding: 18px;
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
            max-width: 800px;
            margin-bottom: 48px;
        }

        .section-heading h2 {
            font-size: clamp(36px, 5vw, 52px);
            letter-spacing: -0.02em;
            line-height: 1.15;
            margin: 12px 0 18px;
            font-weight: 700;
        }

        .section-heading p {
            color: var(--muted);
            font-size: 17px;
            line-height: 1.7;
            margin: 0;
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
            gap: 24px;
            margin-bottom: 80px;
        }

        .feature-card {
            padding: 28px;
            border-radius: 16px;
            background: rgba(255, 255, 255, 0.02);
            border: 1px solid rgba(148, 163, 184, 0.1);
            min-height: auto;
            transition: all 0.3s ease;
        }

        .feature-card:hover {
            background: rgba(255, 255, 255, 0.04);
            border-color: rgba(148, 163, 184, 0.2);
            transform: translateY(-4px);
        }

        .feature-icon {
            width: 48px;
            height: 48px;
            border-radius: 12px;
            display: grid;
            place-items: center;
            background: rgba(87, 216, 255, 0.1);
            border: 1px solid rgba(87, 216, 255, 0.2);
            margin-bottom: 18px;
            font-size: 1.2rem;
        }

        .feature-card h3 {
            font-size: 18px;
            margin: 0 0 12px;
            font-weight: 600;
            color: var(--text);
        }

        .feature-card p {
            color: var(--muted);
            line-height: 1.7;
            margin: 0;
            font-size: 15px;
        }

        @media (max-width: 1024px) {
            .feature-grid {
                grid-template-columns: repeat(2, minmax(0, 1fr));
                gap: 20px;
            }
        }

        @media (max-width: 640px) {
            .feature-grid {
                grid-template-columns: 1fr;
            }
        }

        .steps-row {
            display: grid;
            grid-template-columns: repeat(4, minmax(0, 1fr));
            gap: 20px;
            align-items: stretch;
            margin-bottom: 80px;
        }

        .step-card {
            padding: 28px;
            position: relative;
            border-radius: 16px;
            background: rgba(255, 255, 255, 0.02);
            border: 1px solid rgba(148, 163, 184, 0.1);
        }

        .step-card:after {
            content: "→";
            position: absolute;
            right: -26px;
            top: 50%;
            transform: translateY(-50%);
            color: rgba(255, 255, 255, 0.15);
            font-size: 1.4rem;
        }

        .step-card:last-child:after {
            display: none;
        }

        .step-card__num {
            color: var(--cyan);
            font-weight: 700;
            letter-spacing: 0.12em;
            text-transform: uppercase;
            font-size: 11px;
        }

        .step-card h3 {
            margin: 16px 0 12px;
            font-size: 17px;
            font-weight: 600;
            color: var(--text);
        }

        .step-card p {
            color: var(--muted);
            line-height: 1.6;
            margin: 0;
            font-size: 14px;
        }

        @media (max-width: 1024px) {
            .steps-row {
                grid-template-columns: repeat(2, minmax(0, 1fr));
                gap: 16px;
            }

            .step-card:nth-child(2):after,
            .step-card:nth-child(4):after {
                display: none;
            }
        }

        @media (max-width: 640px) {
            .steps-row {
                grid-template-columns: 1fr;
            }

            .step-card:after {
                display: none;
            }
        }

        .preview-grid {
            display: grid;
            grid-template-columns: 1.6fr 1fr;
            gap: 60px;
            align-items: center;
            margin-bottom: 80px;
        }

        .preview-device {
            padding: 28px;
            background: linear-gradient(135deg, rgba(15, 23, 42, 0.9), rgba(15, 23, 42, 0.7));
            border-radius: 16px;
            border: 1px solid rgba(148, 163, 184, 0.12);
        }

        .preview-surface {
            border-radius: 12px;
            padding: 24px;
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid rgba(148, 163, 184, 0.1);
        }

        .preview-header {
            display: flex;
            justify-content: space-between;
            gap: 16px;
            align-items: center;
            margin-bottom: 20px;
        }

        .preview-title {
            font-size: 16px;
            font-weight: 600;
            color: var(--text);
        }

        .preview-status {
            color: #fff;
            background: linear-gradient(135deg, #10b981, #059669);
            border-radius: 6px;
            padding: 6px 12px;
            font-size: 12px;
            font-weight: 600;
        }

        .preview-grid-mini {
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 12px;
            margin-bottom: 18px;
        }

        .preview-mini {
            border-radius: 10px;
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(148, 163, 184, 0.1);
            padding: 14px;
        }

        .preview-mini span {
            display: block;
            color: var(--muted);
            font-size: 11px;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            margin-bottom: 6px;
        }

        .preview-mini strong {
            font-size: 18px;
            font-weight: 700;
            color: var(--text);
        }

        .preview-chart {
            display: grid;
            gap: 12px;
        }

        .preview-chart__bar {
            height: 10px;
            border-radius: 6px;
            background: rgba(148, 163, 184, 0.15);
            position: relative;
            overflow: hidden;
        }

        .preview-chart__bar:after {
            content: "";
            position: absolute;
            inset: 0;
            width: 70%;
            background: linear-gradient(90deg, #2563eb, #7c3aed);
            border-radius: inherit;
        }

        .preview-insight {
            padding: 0;
            display: grid;
            gap: 16px;
        }

        .preview-insight h3 {
            margin: 0;
            font-size: 26px;
            line-height: 1.2;
            font-weight: 700;
        }

        .preview-insight p {
            color: var(--muted);
            line-height: 1.7;
            margin: 0;
            font-size: 15px;
        }

        @media (max-width: 1024px) {
            .preview-grid {
                grid-template-columns: 1fr;
                gap: 40px;
            }
        }

        .benefit-grid {
            display: grid;
            grid-template-columns: repeat(2, minmax(0, 1fr));
            gap: 24px;
            margin-bottom: 80px;
        }

        .benefit-card {
            padding: 32px;
            border-radius: 16px;
            background: rgba(255, 255, 255, 0.02);
            border: 1px solid rgba(148, 163, 184, 0.1);
        }

        .benefit-card h3 {
            margin: 0 0 20px;
            font-size: 18px;
            font-weight: 600;
            color: var(--text);
        }

        .benefit-card ul {
            margin: 0;
            padding-left: 20px;
            color: var(--muted);
            line-height: 1.8;
            font-size: 15px;
        }

        .benefit-card li + li {
            margin-top: 14px;
        }

        @media (max-width: 768px) {
            .benefit-grid {
                grid-template-columns: 1fr;
            }
        }

        .testimonial-grid {
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 24px;
            margin-bottom: 80px;
        }

        .testimonial-card {
            padding: 28px;
            min-height: auto;
            display: grid;
            align-content: space-between;
            border-radius: 16px;
            background: rgba(255, 255, 255, 0.02);
            border: 1px solid rgba(148, 163, 184, 0.1);
        }

        .testimonial-card p {
            font-size: 15px;
            line-height: 1.8;
            margin: 0 0 20px;
            color: var(--text);
        }

        .testimonial-card strong {
            display: block;
            margin-bottom: 4px;
            font-weight: 600;
            color: var(--text);
        }

        .testimonial-card span {
            font-size: 13px;
            color: var(--muted);
        }

        @media (max-width: 1024px) {
            .testimonial-grid {
                grid-template-columns: repeat(2, minmax(0, 1fr));
            }
        }

        @media (max-width: 640px) {
            .testimonial-grid {
                grid-template-columns: 1fr;
            }
        }

        .faq-shell {
            padding: 32px;
            border-radius: 16px;
            background: rgba(255, 255, 255, 0.02);
            border: 1px solid rgba(148, 163, 184, 0.1);
            margin-bottom: 80px;
        }

        .faq-item {
            border-bottom: 1px solid rgba(148, 163, 184, 0.1);
            padding: 20px 0;
        }

        .faq-item:last-child {
            border-bottom: none;
        }

        .faq-item summary {
            cursor: pointer;
            list-style: none;
            font-weight: 600;
            font-size: 16px;
            padding: 0;
            color: var(--text);
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .faq-item summary::-webkit-details-marker {
            display: none;
        }

        .faq-item summary:after {
            content: "+";
            font-size: 20px;
            color: var(--muted);
            transition: transform 0.3s ease;
        }

        .faq-item[open] summary:after {
            content: "−";
        }

        .faq-item p {
            color: var(--muted);
            line-height: 1.7;
            margin: 16px 0 0;
            font-size: 15px;
        }

        .cta-shell {
            padding: 48px;
            text-align: center;
            background: linear-gradient(135deg, rgba(15, 23, 42, 0.8), rgba(15, 23, 42, 0.6));
            border: 1px solid rgba(148, 163, 184, 0.12);
            border-radius: 16px;
            margin-bottom: 80px;
        }

        .cta-shell h2 {
            font-size: clamp(36px, 4vw, 48px);
            letter-spacing: -0.02em;
            margin: 0 0 16px;
            font-weight: 700;
        }

        .cta-shell p {
            color: var(--muted);
            line-height: 1.7;
            max-width: 700px;
            margin: 0 auto 32px;
            font-size: 16px;
        }

        .cta-shell .cta-row {
            justify-content: center;
            margin-bottom: 0;
        }

        @media (max-width: 768px) {
            .cta-shell {
                padding: 32px;
            }
        }

        .footer-shell {
            padding: 48px;
            margin-top: 0;
            border-top: 1px solid rgba(148, 163, 184, 0.1);
        }

        .footer-grid {
            display: grid;
            grid-template-columns: 1.3fr repeat(3, 1fr);
            gap: 40px;
            margin-bottom: 32px;
        }

        .footer-title {
            font-size: 14px;
            margin-bottom: 16px;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            color: var(--text);
        }

        .footer-shell a {
            color: var(--muted);
            text-decoration: none;
            display: block;
            margin-bottom: 12px;
            font-size: 14px;
            transition: color 0.2s ease;
        }

        .footer-shell a:hover {
            color: var(--text);
        }

        .footer-note {
            margin: 0;
            padding: 0;
            border: none;
            color: var(--muted);
            display: flex;
            justify-content: space-between;
            gap: 16px;
            flex-wrap: wrap;
            font-size: 13px;
        }

        .social-row {
            display: flex;
            gap: 12px;
            flex-wrap: wrap;
        }

        .social-chip {
            width: 36px;
            height: 36px;
            border-radius: 8px;
            display: grid;
            place-items: center;
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(148, 163, 184, 0.15);
            color: var(--text);
            font-size: 13px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s ease;
        }

        .social-chip:hover {
            background: rgba(255, 255, 255, 0.1);
            border-color: rgba(148, 163, 184, 0.3);
        }

        @media (max-width: 1024px) {
            .footer-grid {
                grid-template-columns: repeat(2, 1fr);
                gap: 30px;
            }

            .footer-shell {
                padding: 32px;
            }
        }

        @media (max-width: 640px) {
            .footer-grid {
                grid-template-columns: 1fr;
            }

            .footer-note {
                flex-direction: column;
                justify-content: flex-start;
            }
        }

        .section-space {
            height: 60px;
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

        @media (max-width: 1024px) {
            .section-space {
                height: 48px;
            }
        }

        @media (max-width: 768px) {
            .section-space {
                height: 36px;
            }

            .nav-inner {
                gap: 12px;
            }

            .hero-shell,
            .cta-shell,
            .footer-shell,
            .faq-shell,
            .preview-device {
                border-radius: 12px;
            }

            .hero-title {
                font-size: 36px;
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

            .trusted-row {
                grid-template-columns: repeat(3, minmax(0, 1fr));
            }
        }

        @media (max-width: 480px) {
            .main .block-container {
                padding-left: 16px;
                padding-right: 16px;
            }

            .hero-title {
                font-size: 28px;
                margin-bottom: 16px;
            }

            .hero-copy {
                font-size: 15px;
            }

            .section-heading h2 {
                font-size: 28px;
            }

            .nav-links {
                display: none !important;
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

    metric_chips_html = "".join(
        f"""
        <div class="metric-chip">
            <strong>{metric['value']}</strong>
            <span>{metric['label']}</span>
        </div>
        """
        for metric in LANDING_STATS
    )

    st.markdown(
        f"""
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
                        {metric_chips_html}
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
