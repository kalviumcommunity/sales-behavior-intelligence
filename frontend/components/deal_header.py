"""Deal Details Header Component"""

import streamlit as st


def render_deal_header(deal):
    """Render the deal header with key information and actions."""

    def format_currency(value):
        if value >= 1_000_000:
            return f"${value / 1_000_000:.2f}M"
        if value >= 1_000:
            return f"${value / 1_000:.0f}K"
        return f"${value:,.0f}"

    # Back button and header info
    header_cols = st.columns([0.8, 3.2, 1.8], vertical_alignment="center")

    with header_cols[0]:
        if st.button("← Back", use_container_width=True, key="deal_back_button"):
            st.session_state.pop("deal_details_id", None)
            st.switch_page("pages/2_Deals.py")

    with header_cols[1]:
        st.markdown(f"""
            <div class='deal-header-info'>
                <div class='deal-header__company'>{deal['company']}</div>
                <div class='deal-header__name'>{deal['deal_name']}</div>
            </div>
            """)

    with header_cols[2]:
        action_col1, action_col2 = st.columns(2)
        with action_col1:
            if st.button(
                "✎ Edit Deal", use_container_width=True, key="deal_edit_button"
            ):
                st.toast("Edit Deal is UI-only for this MVP.", icon="✎")
        with action_col2:
            if st.button("⋯ More", use_container_width=True, key="deal_more_button"):
                st.toast("More actions coming soon.", icon="⋯")

    # Deal key info grid
    info_cols = st.columns(5)

    info_items = [
        ("Value", format_currency(deal["deal_value"])),
        ("Stage", deal["stage"]),
        ("Risk", deal["risk_level"]),
        ("Rep", deal["assigned_rep"]),
        ("Close", deal["expected_close"].strftime("%b %d, %Y")),
    ]

    for col, (label, value) in zip(info_cols, info_items):
        with col:
            st.markdown(f"""
                <div class='deal-key-info'>
                    <div class='deal-key-info__label'>{label}</div>
                    <div class='deal-key-info__value'>{value}</div>
                </div>
                """)
