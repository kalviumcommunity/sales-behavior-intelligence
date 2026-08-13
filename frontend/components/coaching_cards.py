"""
Evidence-Backed Coaching Cards Component.
Displays detected seller behaviors, concrete proof/evidence, deal impact, and recommended coaching action.
"""
import streamlit as st

def render_coaching_cards(coaching_cards):
    """Renders evidence-backed coaching cards for managers."""
    if not coaching_cards:
        st.success("✅ No behavioral risk flags detected on this deal. Great execution!")
        return

    st.subheader("💡 Evidence-Backed Coaching Recommendations")
    st.caption("Auto-generated behavior analysis connecting rep activity to deal outcomes.")

    for card in coaching_cards:
        badge_color = "#dc2626" if card["severity"] == "High Risk" else "#d97706"

        with st.expander(f"⚠️ {card['flag_title']} ({card['severity']})", expanded=True):
            st.markdown(
                f"""
                <div style="background-color: #f9fafb; padding: 12px; border-radius: 8px; border: 1px solid #e5e7eb; margin-bottom: 8px;">
                    <div style="font-weight: 600; color: #111827; margin-bottom: 4px;">
                        📌 <strong>Concrete Evidence:</strong>
                    </div>
                    <div style="color: #374151; font-size: 0.95rem; margin-bottom: 10px;">
                        {card['evidence']}
                    </div>
                    <div style="font-weight: 600; color: #991b1b; margin-bottom: 4px;">
                        📉 <strong>Deal Impact:</strong>
                    </div>
                    <div style="color: #4b5563; font-size: 0.95rem; margin-bottom: 10px;">
                        {card['impact']}
                    </div>
                    <div style="font-weight: 600; color: #065f46; margin-bottom: 4px;">
                        🎯 <strong>Recommended Manager Coaching Action:</strong>
                    </div>
                    <div style="color: #047857; font-size: 0.95rem; font-weight: 500;">
                        {card['action']}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            col1, col2, col3 = st.columns([2, 2, 4])
            with col1:
                if st.button(f"Mark Coached", key=f"btn_coached_{card['id']}", type="primary", use_container_width=True):
                    st.toast(f"Marked '{card['flag_title']}' as coached with rep!", icon="✅")
            with col2:
                if st.button(f"Send to Slack/Email", key=f"btn_share_{card['id']}", use_container_width=True):
                    st.toast("Coaching recommendation shared with rep.", icon="📩")
