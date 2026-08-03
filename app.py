import streamlit as st

from frontend.mock_data import MOCK_COACHING_CARDS, MOCK_DEALS, MOCK_REPS, MOCK_TIMELINES


st.set_page_config(
    page_title="Sales Behavior Intelligence",
    page_icon="◼",
    layout="wide",
    initial_sidebar_state="expanded",
)


def money(value):
    return f"${value:,.0f}"


def render_stat_card(label, value, detail, accent="cyan"):
    st.markdown(
        f"""
        <div class="stat-card stat-{accent}">
            <div class="stat-label">{label}</div>
            <div class="stat-value">{value}</div>
            <div class="stat-detail">{detail}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_feature_card(title, body, tag):
    st.markdown(
        f"""
        <div class="feature-card">
            <div class="feature-tag">{tag}</div>
            <h3>{title}</h3>
            <p>{body}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_preview_deal(deal):
    timeline = MOCK_TIMELINES.get(deal["id"], [])
    coaching_cards = MOCK_COACHING_CARDS.get(deal["id"], [])

    st.markdown(
        f"""
        <div class="preview-panel">
            <div class="preview-panel__header">
                <div>
                    <div class="eyebrow">Live behavioral preview</div>
                    <h3>{deal['name']}</h3>
                </div>
                <div class="risk-pill risk-{deal['risk_level'].lower()}">{deal['risk_level']} risk</div>
            </div>
            <div class="preview-grid">
                <div class="preview-metric">
                    <span>Value</span>
                    <strong>{money(deal['amount'])}</strong>
                </div>
                <div class="preview-metric">
                    <span>Stage</span>
                    <strong>{deal['stage']}</strong>
                </div>
                <div class="preview-metric">
                    <span>Risk score</span>
                    <strong>{deal['risk_score']}/100</strong>
                </div>
                <div class="preview-metric">
                    <span>Owner</span>
                    <strong>{deal['rep_name']}</strong>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    timeline_html = "".join(
        f"""
        <div class="timeline-item">
            <div class="timeline-date">{event['date']}</div>
            <div class="timeline-title">{event['icon']} {event['title']}</div>
            <div class="timeline-details">{event['details']}</div>
        </div>
        """
        for event in timeline[:3]
    )
    coaching_html = "".join(
        f"""
        <div class="coaching-item">
            <div class="coaching-severity">{card['severity']}</div>
            <div class="coaching-title">{card['flag_title']}</div>
            <div class="coaching-action">{card['action']}</div>
        </div>
        """
        for card in coaching_cards[:2]
    )

    st.markdown(
        f"""
        <div class="preview-split">
            <div class="preview-column">
                <div class="eyebrow">Recent signal trail</div>
                {timeline_html or '<div class="empty-state">No timeline events available.</div>'}
            </div>
            <div class="preview-column">
                <div class="eyebrow">Suggested coaching</div>
                {coaching_html or '<div class="empty-state">No coaching flags available.</div>'}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


total_pipeline = sum(deal["amount"] for deal in MOCK_DEALS)
high_risk_deals = [deal for deal in MOCK_DEALS if deal["risk_level"] == "High"]
avg_risk_score = round(sum(deal["risk_score"] for deal in MOCK_DEALS) / len(MOCK_DEALS))
coaching_cards_total = sum(len(cards) for cards in MOCK_COACHING_CARDS.values())
active_reps = len(MOCK_REPS)


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
        --cyan-soft: rgba(86, 216, 255, 0.16);
        --violet: #8d7cff;
        --violet-soft: rgba(141, 124, 255, 0.16);
        --green: #49d19d;
        --green-soft: rgba(73, 209, 157, 0.16);
        --orange: #ffb86b;
        --orange-soft: rgba(255, 184, 107, 0.16);
    }

    .stApp {
        background:
            radial-gradient(circle at top left, rgba(86, 216, 255, 0.14), transparent 28%),
            radial-gradient(circle at top right, rgba(141, 124, 255, 0.16), transparent 24%),
            linear-gradient(180deg, #060913 0%, #0a1020 52%, #05070d 100%);
        color: var(--text);
    }

    .main .block-container {
        padding-top: 1.25rem;
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

    .hero-shell {
        border: 1px solid var(--panel-border);
        background: linear-gradient(135deg, rgba(13, 18, 32, 0.92), rgba(13, 18, 32, 0.72));
        border-radius: 28px;
        box-shadow: 0 30px 80px rgba(0, 0, 0, 0.42);
        overflow: hidden;
        position: relative;
        padding: 28px;
    }

    .hero-shell:before {
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

    .hero-title {
        font-size: clamp(2.5rem, 5vw, 4.8rem);
        line-height: 0.98;
        margin: 0;
        letter-spacing: -0.04em;
    }

    .hero-copy {
        max-width: 720px;
        color: var(--muted);
        font-size: 1.02rem;
        line-height: 1.7;
        margin-top: 18px;
        margin-bottom: 22px;
    }

    .cta-row {
        display: flex;
        flex-wrap: wrap;
        gap: 12px;
        margin-bottom: 8px;
    }

    .cta-pill {
        border-radius: 999px;
        padding: 11px 18px;
        border: 1px solid var(--panel-border);
        background: rgba(255, 255, 255, 0.03);
        color: var(--text);
        font-weight: 700;
        font-size: 0.92rem;
    }

    .cta-pill.primary {
        background: linear-gradient(135deg, var(--cyan), var(--violet));
        color: #071019;
        border-color: transparent;
    }

    .hero-right {
        display: grid;
        gap: 14px;
    }

    .info-card,
    .stat-card,
    .feature-card,
    .preview-panel,
    .preview-column,
    .signal-card {
        border: 1px solid var(--panel-border);
        background: var(--panel);
        border-radius: 22px;
        box-shadow: 0 18px 40px rgba(0, 0, 0, 0.26);
    }

    .info-card {
        padding: 18px;
    }

    .mini-metric {
        display: grid;
        gap: 4px;
    }

    .mini-metric strong {
        font-size: 1.45rem;
    }

    .mini-metric span {
        color: var(--muted);
        font-size: 0.84rem;
    }

    .stat-card {
        padding: 18px 18px 16px;
        min-height: 138px;
    }

    .stat-label {
        color: var(--muted);
        font-size: 0.8rem;
        text-transform: uppercase;
        letter-spacing: 0.14em;
    }

    .stat-value {
        font-size: 1.85rem;
        line-height: 1.1;
        margin: 12px 0 8px;
        font-weight: 800;
    }

    .stat-detail {
        color: var(--muted);
        font-size: 0.92rem;
        line-height: 1.45;
    }

    .stat-cyan {
        background: linear-gradient(180deg, rgba(86, 216, 255, 0.1), rgba(13, 18, 32, 0.92));
    }

    .stat-violet {
        background: linear-gradient(180deg, rgba(141, 124, 255, 0.1), rgba(13, 18, 32, 0.92));
    }

    .stat-green {
        background: linear-gradient(180deg, rgba(73, 209, 157, 0.1), rgba(13, 18, 32, 0.92));
    }

    .stat-orange {
        background: linear-gradient(180deg, rgba(255, 184, 107, 0.12), rgba(13, 18, 32, 0.92));
    }

    .section-heading {
        margin: 22px 0 8px;
        font-size: 1.8rem;
        letter-spacing: -0.03em;
    }

    .section-subtitle {
        color: var(--muted);
        margin-bottom: 18px;
        line-height: 1.6;
    }

    .feature-card {
        padding: 20px;
        height: 100%;
    }

    .feature-card h3 {
        margin: 0 0 10px;
        font-size: 1.15rem;
    }

    .feature-card p {
        color: var(--muted);
        line-height: 1.65;
        margin: 0;
    }

    .feature-tag {
        display: inline-flex;
        border-radius: 999px;
        padding: 5px 10px;
        margin-bottom: 12px;
        font-size: 0.72rem;
        letter-spacing: 0.14em;
        text-transform: uppercase;
        background: rgba(255, 255, 255, 0.05);
        color: var(--muted);
    }

    .preview-panel {
        padding: 20px;
    }

    .preview-panel__header {
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        gap: 14px;
        margin-bottom: 18px;
    }

    .preview-panel h3 {
        margin: 0;
        font-size: 1.35rem;
    }

    .preview-grid {
        display: grid;
        grid-template-columns: repeat(4, minmax(0, 1fr));
        gap: 12px;
    }

    .preview-metric {
        padding: 14px;
        border-radius: 16px;
        background: rgba(255, 255, 255, 0.035);
        border: 1px solid rgba(148, 163, 184, 0.12);
        display: grid;
        gap: 8px;
    }

    .preview-metric span {
        color: var(--muted);
        font-size: 0.8rem;
        text-transform: uppercase;
        letter-spacing: 0.12em;
    }

    .preview-metric strong {
        font-size: 1.08rem;
    }

    .preview-split {
        display: grid;
        grid-template-columns: repeat(2, minmax(0, 1fr));
        gap: 18px;
        margin-top: 18px;
    }

    .preview-column {
        padding: 18px;
    }

    .timeline-item,
    .coaching-item {
        padding: 14px 0;
        border-bottom: 1px solid rgba(148, 163, 184, 0.1);
    }

    .timeline-item:last-child,
    .coaching-item:last-child {
        border-bottom: none;
        padding-bottom: 0;
    }

    .timeline-date,
    .coaching-severity {
        color: var(--muted);
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 0.14em;
        margin-bottom: 6px;
    }

    .timeline-title,
    .coaching-title {
        font-weight: 700;
        margin-bottom: 6px;
    }

    .timeline-details,
    .coaching-action {
        color: var(--muted);
        line-height: 1.55;
        font-size: 0.93rem;
    }

    .risk-pill {
        border-radius: 999px;
        padding: 8px 12px;
        font-size: 0.78rem;
        letter-spacing: 0.14em;
        text-transform: uppercase;
        border: 1px solid rgba(148, 163, 184, 0.16);
    }

    .risk-high { background: rgba(239, 68, 68, 0.12); color: #ff9e9e; }
    .risk-medium { background: rgba(245, 158, 11, 0.12); color: #ffd08a; }
    .risk-low { background: rgba(34, 197, 94, 0.12); color: #95f3ba; }

    .signal-grid {
        display: grid;
        grid-template-columns: repeat(4, minmax(0, 1fr));
        gap: 14px;
    }

    .signal-card {
        padding: 18px;
    }

    .signal-card h4 {
        margin: 0 0 8px;
        font-size: 1rem;
    }

    .signal-card p {
        margin: 0;
        color: var(--muted);
        line-height: 1.55;
    }

    .empty-state {
        color: var(--muted);
        padding: 8px 0;
    }

    .footer-shell {
        margin-top: 22px;
        padding: 22px 24px;
        border-radius: 22px;
        border: 1px solid var(--panel-border);
        background: linear-gradient(135deg, rgba(86, 216, 255, 0.08), rgba(141, 124, 255, 0.08), rgba(13, 18, 32, 0.94));
    }

    .footer-shell p {
        color: var(--muted);
        margin: 8px 0 0;
    }

    @media (max-width: 1100px) {
        .preview-grid,
        .signal-grid,
        .preview-split {
            grid-template-columns: 1fr 1fr;
        }
    }

    @media (max-width: 720px) {
        .preview-grid,
        .signal-grid,
        .preview-split {
            grid-template-columns: 1fr;
        }

        .preview-panel__header {
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
    st.markdown("Landing page preview")
    st.markdown("#### View")
    st.markdown("Manager dashboard ready")
    st.markdown("#### Status")
    st.success("Mock data connected")
    st.info("Frontend built in Streamlit")


st.markdown(
    """
    <div class="hero-shell">
        <div class="eyebrow">Behavioral intelligence for modern sales teams</div>
        <div class="hero-grid">
            <div>
                <h1 class="hero-title">See the behaviors behind every deal outcome.</h1>
                <p class="hero-copy">
                    Sales Behavior Intelligence turns CRM activity, email cadence, meeting notes, and call transcripts
                    into evidence-backed coaching. The result is a sharper pipeline view, faster intervention on risk,
                    and a repeatable coaching system managers can actually use.
                </p>
                <div class="cta-row">
                    <div class="cta-pill primary">Explore the product</div>
                    <div class="cta-pill">Review coaching insights</div>
                    <div class="cta-pill">Inspect deal signals</div>
                </div>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("<div style='height: 18px;'></div>", unsafe_allow_html=True)

left_hero, right_hero = st.columns([1.5, 1])
with left_hero:
    st.markdown(
        """
        <div class="info-card">
            <div class="eyebrow">Why teams use it</div>
            <div class="mini-metric">
                <strong>Move from intuition to evidence.</strong>
                <span>Replace vague coaching with specific behavioral patterns tied to stage progression, deal health, and rep performance.</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
with right_hero:
    st.markdown(
        """
        <div class="info-card">
            <div class="eyebrow">Current demo mode</div>
            <div class="mini-metric">
                <strong>Mock pipeline + live-style previews</strong>
                <span>Built from representative deals, coaching flags, and timeline events.</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)

stat1, stat2, stat3, stat4 = st.columns(4)
with stat1:
    render_stat_card("Total active pipeline", money(total_pipeline), f"{len(MOCK_DEALS)} open opportunities", "cyan")
with stat2:
    render_stat_card("High-risk exposure", money(sum(deal['amount'] for deal in high_risk_deals)), f"{len(high_risk_deals)} deals flagged", "orange")
with stat3:
    render_stat_card("Average risk score", f"{avg_risk_score}/100", "Behavior-based scoring across the current book", "violet")
with stat4:
    render_stat_card("Coaching actions surfaced", f"{coaching_cards_total}", f"Across {active_reps} active reps", "green")

st.markdown("<div style='height: 8px;'></div>", unsafe_allow_html=True)
st.markdown("## Product story")
st.markdown(
    "<p class='section-subtitle'>The layout below mirrors the dark, panel-driven feel of the reference image: sharp cards, compact evidence blocks, and a product-first narrative rather than a blank marketing page.</p>",
    unsafe_allow_html=True,
)

feature_col1, feature_col2, feature_col3 = st.columns(3)
with feature_col1:
    render_feature_card(
        "Pipeline risk matrix",
        "Spot where opportunities are stalling, filter by rep or segment, and surface the highest-value deals needing intervention first.",
        "Pipeline",
    )
with feature_col2:
    render_feature_card(
        "Deal deep dive timeline",
        "Combine CRM changes, call transcripts, and email lag into a single chronological trail that makes the root cause visible.",
        "Evidence",
    )
with feature_col3:
    render_feature_card(
        "Rep coaching view",
        "Benchmark seller behavior, identify repeatable strengths, and guide the next best coaching move for each rep.",
        "Coaching",
    )

st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)

signal_col1, signal_col2, signal_col3, signal_col4 = st.columns(4)
with signal_col1:
    st.markdown(
        """
        <div class="signal-card">
            <h4>Follow-up timing</h4>
            <p>Flag proposal lag, slow post-demo response, and passive check-ins before momentum drops.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
with signal_col2:
    st.markdown(
        """
        <div class="signal-card">
            <h4>Stakeholder coverage</h4>
            <p>Detect single-threaded deals and expose missing executive, finance, or procurement engagement.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
with signal_col3:
    st.markdown(
        """
        <div class="signal-card">
            <h4>Next-step clarity</h4>
            <p>Show whether each interaction ends with a booked follow-up or just a vague promise to reconnect.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
with signal_col4:
    st.markdown(
        """
        <div class="signal-card">
            <h4>Rep talk patterns</h4>
            <p>Surface talk-time imbalance and thin discovery patterns that often lead to weak qualification.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("<div style='height: 16px;'></div>", unsafe_allow_html=True)
st.markdown("## Live preview")
st.markdown(
    "<p class='section-subtitle'>A highlighted opportunity from the mock dataset shows how the landing page can preview the eventual product experience.</p>",
    unsafe_allow_html=True,
)

render_preview_deal(MOCK_DEALS[0])

st.markdown(
    """
    <div class="footer-shell">
        <div class="eyebrow">Built for sales leaders, reps, and RevOps</div>
        <h3 style="margin:0; font-size:1.45rem;">One view for risk, coaching, and deal momentum.</h3>
        <p>
            This landing page now presents the product as a sharp, dark, evidence-driven experience that matches the reference style
            while staying grounded in the existing sales-behavior data model.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)