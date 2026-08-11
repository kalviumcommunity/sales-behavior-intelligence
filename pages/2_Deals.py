import streamlit as st

from frontend.components.kpi_card import render_kpi_card
from frontend.components.sidebar import render_sidebar
from frontend.deals_data import CURRENT_DATE, DEALS


st.set_page_config(
    page_title="Deals | Sales Behavior Intelligence",
    page_icon="◪",
    layout="wide",
    initial_sidebar_state="expanded",
)

if not st.session_state.get("authenticated"):
    st.switch_page("pages/1_Authentication.py")


def _format_currency(value):
    if value >= 1_000_000:
        amount = f"{value / 1_000_000:.2f}".rstrip("0").rstrip(".")
        return f"${amount}M"
    if value >= 1_000:
        return f"${value / 1_000:.0f}K"
    return f"${value:,.0f}"


def _stage_slug(stage):
    return stage.lower().replace(" ", "-")


def _deal_size_bucket(amount):
    if amount < 100_000:
        return "Under $100K"
    if amount < 250_000:
        return "$100K - $250K"
    if amount < 500_000:
        return "$250K - $500K"
    return "$500K+"


def _close_date_bucket(close_date):
    delta_days = (close_date - CURRENT_DATE).days
    if delta_days < 0:
        return "Past due"
    if delta_days <= 7:
        return "Due in 7 days"
    if delta_days <= 30:
        return "Due in 30 days"
    return "This quarter"


def _selected_rep_options(deals):
    reps = sorted({deal["rep_name"] for deal in deals})
    return ["All reps", *reps]


def _reset_filters():
    st.session_state.deals_search = ""
    st.session_state.deals_stage_filter = "All stages"
    st.session_state.deals_risk_filter = "All risk"
    st.session_state.deals_rep_filter = "All reps"
    st.session_state.deals_size_filter = "All sizes"
    st.session_state.deals_close_filter = "All close dates"
    st.session_state.deals_sort_filter = "Deal Value"


def _get_filtered_deals(deals):
    search_value = st.session_state.deals_search.strip().lower()
    stage_filter = st.session_state.deals_stage_filter
    risk_filter = st.session_state.deals_risk_filter
    rep_filter = st.session_state.deals_rep_filter
    deal_size_filter = st.session_state.deals_size_filter
    close_date_filter = st.session_state.deals_close_filter
    sort_value = st.session_state.deals_sort_filter

    filtered = []
    for deal in deals:
        if search_value:
            searchable = " ".join(
                [
                    deal["company"],
                    deal["deal_name"],
                    deal["rep_name"],
                    deal["next_step"],
                    deal["ai_signal"],
                ]
            ).lower()
            if search_value not in searchable:
                continue

        if stage_filter != "All stages" and deal["stage"] != stage_filter:
            continue

        if risk_filter != "All risk" and deal["risk_level"] != risk_filter:
            continue

        if rep_filter != "All reps" and deal["rep_name"] != rep_filter:
            continue

        if deal_size_filter != "All sizes" and _deal_size_bucket(deal["amount"]) != deal_size_filter:
            continue

        if close_date_filter != "All close dates" and _close_date_bucket(deal["expected_close_date"]) != close_date_filter:
            continue

        filtered.append(deal)

    sort_rules = {
        "Deal Value": ("amount", True),
        "Risk Score": ("risk_score", True),
        "Last Activity": ("last_activity_date", True),
        "Close Date": ("expected_close_date", False),
    }
    sort_key, reverse = sort_rules[sort_value]
    filtered.sort(key=lambda item: item[sort_key], reverse=reverse)
    return filtered


def _render_stage_badge(stage):
    stage_class = _stage_slug(stage)
    st.markdown(
        f"<span class='deal-badge deal-badge--stage deal-badge--{stage_class}'>{stage}</span>",
        unsafe_allow_html=True,
    )


def _render_risk_badge(risk_level):
    st.markdown(
        f"<span class='deal-badge deal-badge--risk deal-badge--risk-{risk_level.lower()}'>{risk_level}</span>",
        unsafe_allow_html=True,
    )


def _render_ai_signal(signal):
    st.markdown(f"<div class='deal-signal'>{signal}</div>", unsafe_allow_html=True)


def _render_rep(rep_name):
    initials = "".join(part[0] for part in rep_name.split()[:2]).upper()
    st.markdown(
        f"""
        <div class='deal-rep'>
            <div class='deal-rep__avatar'>{initials}</div>
            <div class='deal-rep__name'>{rep_name}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def _render_summary(total_pipeline, open_deals, at_risk_deals, average_deal_value):
    metric_cols = st.columns(4)
    metrics = [
        ("Total Pipeline", _format_currency(total_pipeline), "+12.4% this month", "cyan"),
        ("Open Deals", str(open_deals), "3 new this week", "blue"),
        ("At-Risk Deals", str(at_risk_deals), "Needs manager attention", "rose"),
        ("Average Deal Value", _format_currency(average_deal_value), "Filtered view average", "violet"),
    ]

    for column, metric in zip(metric_cols, metrics):
        with column:
            render_kpi_card(metric[0], metric[1], metric[2], metric[3])


def _render_toolbar(options):
    with st.container(border=True):
        st.markdown(
            """
            <div class='deals-toolbar__header'>
                <div class='section-eyebrow'>Search and filters</div>
                <h3>Refine the pipeline view</h3>
                <p>Search is live, filters are stateful, and sorting changes the order of the visible deals.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        search_col, sort_col, clear_col = st.columns([4.6, 1.7, 1.1], vertical_alignment="bottom")
        with search_col:
            st.text_input(
                "Search Deals",
                key="deals_search",
                placeholder="Search company, deal, or owner...",
            )
        with sort_col:
            st.selectbox(
                "Sort by",
                ["Deal Value", "Risk Score", "Last Activity", "Close Date"],
                key="deals_sort_filter",
            )
        with clear_col:
            st.button("Clear Filters", use_container_width=True, key="deals_clear_filters", on_click=_reset_filters)

        filter_cols = st.columns(5)
        with filter_cols[0]:
            st.selectbox("Stage", options["stages"], key="deals_stage_filter")
        with filter_cols[1]:
            st.selectbox("Risk", options["risks"], key="deals_risk_filter")
        with filter_cols[2]:
            st.selectbox("Sales Rep", options["reps"], key="deals_rep_filter")
        with filter_cols[3]:
            st.selectbox("Deal Size", options["sizes"], key="deals_size_filter")
        with filter_cols[4]:
            st.selectbox("Close Date", options["close_dates"], key="deals_close_filter")


def _render_deal_row(deal):
    with st.container(border=True):
        top_cols = st.columns([2.4, 1, 1, 0.9, 1.1, 1, 1, 0.8], vertical_alignment="center")

        with top_cols[0]:
            st.markdown(
                f"""
                <div class='deal-primary'>
                    <div class='deal-primary__company'>{deal['company']}</div>
                    <div class='deal-primary__name'>{deal['deal_name']}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with top_cols[1]:
            st.markdown(
                f"""
                <div class='deal-field'>
                    <span class='deal-field__label'>Value</span>
                    <strong>{_format_currency(deal['amount'])}</strong>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with top_cols[2]:
            _render_stage_badge(deal["stage"])
        with top_cols[3]:
            _render_risk_badge(deal["risk_level"])
        with top_cols[4]:
            _render_rep(deal["rep_name"])
        with top_cols[5]:
            st.markdown(
                f"""
                <div class='deal-field'>
                    <span class='deal-field__label'>Last Activity</span>
                    <strong>{deal['last_activity_label']}</strong>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with top_cols[6]:
            st.markdown(
                f"""
                <div class='deal-field'>
                    <span class='deal-field__label'>Expected Close</span>
                    <strong>{deal['expected_close_date'].strftime('%b %d')}</strong>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with top_cols[7]:
            if st.button("Open", key=f"deal_open_{deal['id']}", use_container_width=True):
                st.session_state.deals_selected_deal = deal
                st.toast(f"Selected {deal['company']} for future deal details navigation.", icon="◼")
                st.rerun()

        bottom_cols = st.columns([1.2, 2.1])
        with bottom_cols[0]:
            st.markdown(
                f"""
                <div class='deal-field'>
                    <span class='deal-field__label'>Next Step</span>
                    <strong>{deal['next_step']}</strong>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with bottom_cols[1]:
            _render_ai_signal(deal["ai_signal"])


def _render_empty_state():
    with st.container(border=True):
        st.markdown(
            """
            <div class='empty-state'>
                <div class='empty-state__eyebrow'>No results</div>
                <h3>No deals match your filters.</h3>
                <p>Try adjusting your search or clearing one or more filters.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        empty_action_col1, empty_action_col2 = st.columns([1, 1])
        with empty_action_col1:
            st.button("Clear Filters", use_container_width=True, key="empty_clear_filters", on_click=_reset_filters)
        with empty_action_col2:
            st.button("Keep Searching", use_container_width=True, disabled=True)


st.session_state.setdefault("dashboard_sidebar_collapsed", False)
st.session_state.setdefault("dashboard_active_item", "Deals")
st.session_state.setdefault("deals_selected_deal", None)
st.session_state.setdefault("deals_search", "")
st.session_state.setdefault("deals_stage_filter", "All stages")
st.session_state.setdefault("deals_risk_filter", "All risk")
st.session_state.setdefault("deals_rep_filter", "All reps")
st.session_state.setdefault("deals_size_filter", "All sizes")
st.session_state.setdefault("deals_close_filter", "All close dates")
st.session_state.setdefault("deals_sort_filter", "Deal Value")

st.markdown(
    """
    <style>
    :root {
        --bg: #06101d;
        --panel: rgba(11, 18, 32, 0.82);
        --panel-strong: rgba(13, 21, 37, 0.92);
        --panel-border: rgba(148, 163, 184, 0.15);
        --text: #edf4ff;
        --muted: #93a4bd;
        --cyan: #57d8ff;
        --violet: #9a86ff;
        --blue: #7ab8ff;
        --green: #59d19b;
        --orange: #ffb76a;
        --rose: #ff8ea7;
    }

    .stApp {
        background:
            radial-gradient(circle at 0% 0%, rgba(87, 216, 255, 0.14), transparent 28%),
            radial-gradient(circle at 100% 0%, rgba(154, 134, 255, 0.16), transparent 24%),
            linear-gradient(180deg, #040812 0%, #0a1220 48%, #05070d 100%);
        color: var(--text);
    }

    .main .block-container {
        padding-top: 1rem;
        padding-bottom: 2.2rem;
        max-width: 1520px;
    }

    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, rgba(7, 11, 20, 0.98), rgba(11, 16, 30, 0.96));
        border-right: 1px solid rgba(148, 163, 184, 0.1);
    }

    h1, h2, h3, h4, p, span, div, li, label {
        color: var(--text);
    }

    .sidebar-shell,
    .sidebar-user-card,
    .sidebar-collapsed-card,
    .kpi-card,
    .deals-toolbar__header,
    .empty-state,
    .selected-deal-card,
    .deal-badge,
    .deal-signal,
    .deal-rep,
    .deal-field,
    .deal-primary {
        border: 1px solid var(--panel-border);
        background: var(--panel);
        border-radius: 22px;
        box-shadow: 0 20px 52px rgba(0, 0, 0, 0.24);
    }

    .page-header {
        display: flex;
        justify-content: space-between;
        gap: 20px;
        align-items: flex-start;
        padding: 24px;
        border: 1px solid var(--panel-border);
        background: linear-gradient(135deg, rgba(13, 18, 32, 0.95), rgba(13, 18, 32, 0.72));
        border-radius: 28px;
        margin-bottom: 16px;
    }

    .page-header h1 {
        margin: 6px 0 8px;
        font-size: clamp(2.2rem, 4.5vw, 3.4rem);
        letter-spacing: -0.04em;
    }

    .page-header p {
        margin: 0;
        color: var(--muted);
        max-width: 760px;
        line-height: 1.6;
    }

    .page-eyebrow,
    .section-eyebrow,
    .kpi-label,
    .deal-field__label,
    .empty-state__eyebrow {
        color: var(--muted);
        text-transform: uppercase;
        letter-spacing: 0.14em;
        font-size: 0.72rem;
    }

    .page-actions {
        display: flex;
        gap: 10px;
        flex-wrap: wrap;
        justify-content: flex-end;
    }

    .kpi-card {
        position: relative;
        padding: 16px 18px;
        min-height: 122px;
        overflow: hidden;
    }

    .kpi-card:before {
        content: "";
        position: absolute;
        inset: 0;
        opacity: 0.9;
        pointer-events: none;
        background: linear-gradient(135deg, rgba(87, 216, 255, 0.08), transparent 35%, rgba(154, 134, 255, 0.08));
    }

    .kpi-value {
        font-size: 1.85rem;
        font-weight: 800;
        letter-spacing: -0.04em;
        margin: 10px 0 4px;
    }

    .kpi-detail {
        color: var(--muted);
        font-size: 0.92rem;
        line-height: 1.45;
    }

    .kpi-cyan { border-color: rgba(87, 216, 255, 0.24); }
    .kpi-blue { border-color: rgba(122, 184, 255, 0.24); }
    .kpi-rose { border-color: rgba(255, 142, 167, 0.24); }
    .kpi-violet { border-color: rgba(154, 134, 255, 0.24); }

    .deals-toolbar__header,
    .selected-deal-card,
    .empty-state {
        padding: 18px 20px;
        margin-bottom: 14px;
    }

    .deals-toolbar__header h3,
    .selected-deal-card h3,
    .empty-state h3 {
        margin: 6px 0 8px;
        font-size: 1.15rem;
        letter-spacing: -0.02em;
    }

    .deals-toolbar__header p,
    .selected-deal-card p,
    .empty-state p {
        margin: 0;
        color: var(--muted);
        line-height: 1.6;
    }

    .deal-list-header {
        display: grid;
        grid-template-columns: 2.4fr 1fr 1fr 0.9fr 1.1fr 1fr 1fr 0.8fr;
        gap: 12px;
        padding: 0 10px 10px;
        color: var(--muted);
        text-transform: uppercase;
        letter-spacing: 0.12em;
        font-size: 0.7rem;
    }

    .deal-primary {
        padding: 14px 16px;
        background: rgba(255, 255, 255, 0.02);
        border-radius: 12px;
    }

    .deal-primary__company {
        font-size: 1rem;
        font-weight: 800;
        margin-bottom: 4px;
        color: var(--text);
    }

    .deal-primary__name {
        color: var(--muted);
        font-size: 0.92rem;
        line-height: 1.45;
    }

    .deal-field {
        padding: 12px 14px;
        background: rgba(255, 255, 255, 0.02);
        min-height: 74px;
        display: grid;
        align-content: center;
        border-radius: 12px;
    }

    .deal-field strong {
        font-size: 0.96rem;
        line-height: 1.35;
        word-break: break-word;
        color: var(--text);
        display: block;
    }

    .deal-field__label {
        color: var(--muted);
        text-transform: uppercase;
        letter-spacing: 0.14em;
        font-size: 0.72rem;
        margin-bottom: 4px;
        display: block;
    }

    .deal-badge {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        padding: 8px 12px;
        border-radius: 999px;
        font-size: 0.78rem;
        font-weight: 700;
        line-height: 1;
        width: fit-content;
    }

    .deal-badge--stage {
        background: rgba(122, 184, 255, 0.1);
        border-color: rgba(122, 184, 255, 0.22);
    }

    .deal-badge--stage.discovery { color: #9fe6ff; }
    .deal-badge--stage.qualification { color: #7ab8ff; }
    .deal-badge--stage.proposal { color: #b9a8ff; }
    .deal-badge--stage.negotiation { color: #ffbf7d; }
    .deal-badge--stage.contract { color: #92dfc0; }
    .deal-badge--stage.closed-won { color: #67d8a4; }
    .deal-badge--stage.closed-lost { color: #ff9db3; }

    .deal-badge--risk-low {
        background: rgba(89, 209, 155, 0.12);
        border-color: rgba(89, 209, 155, 0.24);
        color: #8be2b9;
    }

    .deal-badge--risk-medium {
        background: rgba(255, 183, 106, 0.12);
        border-color: rgba(255, 183, 106, 0.24);
        color: #ffcc8f;
    }

    .deal-badge--risk-high {
        background: rgba(255, 142, 167, 0.12);
        border-color: rgba(255, 142, 167, 0.24);
        color: #ffadb9;
    }

    .deal-rep {
        display: inline-flex;
        align-items: center;
        gap: 10px;
        padding: 10px 12px;
        background: rgba(255, 255, 255, 0.02);
        border-radius: 14px;
    }

    .deal-rep__avatar {
        width: 32px;
        height: 32px;
        min-width: 32px;
        display: grid;
        place-items: center;
        border-radius: 12px;
        background: linear-gradient(135deg, rgba(87, 216, 255, 0.18), rgba(154, 134, 255, 0.18));
        border: 1px solid rgba(87, 216, 255, 0.16);
        font-size: 0.78rem;
        font-weight: 800;
        color: var(--cyan);
    }

    .deal-rep__name {
        font-size: 0.92rem;
        font-weight: 700;
        color: var(--text);
    }

    .deal-signal {
        padding: 12px 14px;
        background: linear-gradient(135deg, rgba(87, 216, 255, 0.08), rgba(154, 134, 255, 0.08));
        color: var(--text);
        line-height: 1.45;
        font-size: 0.92rem;
    }

    .selected-deal-card {
        border-color: rgba(87, 216, 255, 0.22);
        background: linear-gradient(135deg, rgba(87, 216, 255, 0.08), rgba(154, 134, 255, 0.08), rgba(13, 18, 32, 0.92));
    }

    .stTextInput label,
    .stSelectbox label {
        color: var(--muted) !important;
        font-size: 0.82rem;
        margin-bottom: 0.32rem;
    }

    .stTextInput input,
    .stSelectbox div[data-baseweb="select"] > div,
    .stButton button {
        background: rgba(255, 255, 255, 0.04) !important;
        color: var(--text) !important;
        border-color: rgba(148, 163, 184, 0.18) !important;
        border-radius: 16px !important;
    }

    .stButton button {
        font-weight: 700;
        padding: 0.7rem 1rem;
    }

    .stButton button:hover {
        border-color: rgba(87, 216, 255, 0.44) !important;
        transform: translateY(-1px);
    }

    div[data-testid="stVerticalBlockBorderWrapper"] {
        border: 1px solid rgba(148, 163, 184, 0.12) !important;
        border-radius: 24px !important;
        background: rgba(11, 18, 32, 0.76) !important;
        box-shadow: 0 18px 46px rgba(0, 0, 0, 0.22) !important;
        padding: 0.25rem 0.1rem !important;
        margin-bottom: 0.85rem;
    }

    @media (max-width: 1200px) {
        .deal-list-header {
            display: none;
        }

        .page-header {
            flex-direction: column;
        }

        .page-actions {
            width: 100%;
            justify-content: flex-start;
        }
    }

    @media (max-width: 760px) {
        .main .block-container {
            padding-top: 0.75rem;
        }

        .page-header,
        .deals-toolbar__header,
        .selected-deal-card,
        .empty-state {
            padding: 18px;
        }

        .kpi-value {
            font-size: 1.55rem;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.session_state.setdefault("dashboard_sidebar_collapsed", False)
st.session_state.setdefault("dashboard_active_item", "Deals")
st.session_state.setdefault("deals_selected_deal", None)
st.session_state.setdefault("deals_search", "")
st.session_state.setdefault("deals_stage_filter", "All stages")
st.session_state.setdefault("deals_risk_filter", "All risk")
st.session_state.setdefault("deals_rep_filter", "All reps")
st.session_state.setdefault("deals_size_filter", "All sizes")
st.session_state.setdefault("deals_close_filter", "All close dates")
st.session_state.setdefault("deals_sort_filter", "Deal Value")

render_sidebar(collapsed=st.session_state.dashboard_sidebar_collapsed, active_item="Deals")

with st.container(border=True):
    header_left, header_right = st.columns([3.4, 1.4], vertical_alignment="center")
    with header_left:
        st.markdown(
            """
            <div class='page-eyebrow'>Pipeline intelligence</div>
            <h1 style='margin: 6px 0 8px;'>Deals</h1>
            <p>Track pipeline health, deal momentum, and opportunities that need attention.</p>
            """,
            unsafe_allow_html=True,
        )
    with header_right:
        action_one, action_two = st.columns(2)
        with action_one:
            if st.button("Add Deal", use_container_width=True, key="deals_add_deal"):
                st.toast("Add Deal is UI-only for this page.", icon="＋")
        with action_two:
            if st.button("Export", use_container_width=True, key="deals_export"):
                st.toast("Export will be connected later.", icon="▤")

visible_deals = _get_filtered_deals(DEALS)
open_deals = [deal for deal in visible_deals if deal["stage"] not in {"Closed Won", "Closed Lost"}]
at_risk_deals = [deal for deal in visible_deals if deal["risk_level"] == "High"]
pipeline_total = sum(deal["amount"] for deal in visible_deals)
average_deal_value = int(pipeline_total / len(visible_deals)) if visible_deals else 0

_render_summary(pipeline_total, len(open_deals), len(at_risk_deals), average_deal_value)

st.markdown("<div style='height: 0.35rem;'></div>", unsafe_allow_html=True)

toolbar_options = {
    "stages": ["All stages", "Discovery", "Qualification", "Proposal", "Negotiation", "Contract", "Closed Won", "Closed Lost"],
    "risks": ["All risk", "Low", "Medium", "High"],
    "reps": _selected_rep_options(DEALS),
    "sizes": ["All sizes", "Under $100K", "$100K - $250K", "$250K - $500K", "$500K+"],
    "close_dates": ["All close dates", "Past due", "Due in 7 days", "Due in 30 days", "This quarter"],
}

_render_toolbar(toolbar_options)

if st.session_state.get("deals_selected_deal"):
    selected = st.session_state.deals_selected_deal
    with st.container(border=True):
        st.markdown(
            f"""
            <div class='selected-deal-card'>
                <div class='section-eyebrow'>Selection ready</div>
                <h3>{selected['company']} · {selected['deal_name']}</h3>
                <p>This deal has been stored in Streamlit session_state and is ready for a future deal details route.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown(
    f"""
    <div style='display:flex; justify-content:space-between; gap:12px; align-items:center; margin: 8px 2px 12px;'>
        <div class='section-eyebrow'>Deal list</div>
        <div style='color: var(--muted); font-size: 0.88rem;'>{len(visible_deals)} deals visible</div>
    </div>
    """,
    unsafe_allow_html=True,
)

if visible_deals:
    st.markdown(
        """
        <div class='deal-list-header'>
            <div>Company / Deal</div>
            <div>Value</div>
            <div>Stage</div>
            <div>Risk</div>
            <div>Sales Rep</div>
            <div>Last Activity</div>
            <div>Expected Close</div>
            <div>Action</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    for deal in visible_deals:
        _render_deal_row(deal)
else:
    _render_empty_state()
