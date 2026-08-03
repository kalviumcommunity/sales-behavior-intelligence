"""
Deal Event Timeline Component.
Renders chronological events (calls, emails, CRM updates) with behavioral risk tags.
"""
import streamlit as st

def render_deal_timeline(timeline_events):
    """Renders visual timeline list of deal activities."""
    if not timeline_events:
        st.info("No timeline events logged for this deal yet.")
        return

    st.subheader("🗓️ Chronological Activity & Behavior Timeline")
    st.caption("Combines CRM updates, email timestamps, and call transcript signals.")

    for event in timeline_events:
        flag_html = ""
        if event.get("flag"):
            if "Slow" in event["flag"] or "Thin" in event["flag"] or "Single" in event["flag"] or "Weak" in event["flag"]:
                flag_color = "#ef4444" # red
                bg_color = "#fee2e2"
            else:
                flag_color = "#10b981" # green
                bg_color = "#d1fae5"
            flag_html = f"<span style='background-color: {bg_color}; color: {flag_color}; padding: 2px 8px; border-radius: 12px; font-size: 0.8rem; font-weight: 600;'>🚩 {event['flag']}</span>"

        with st.container():
            st.markdown(
                f"""
                <div style="border-left: 3px solid #3b82f6; padding-left: 14px; margin-bottom: 16px;">
                    <div style="font-size: 0.85rem; color: #6b7280; font-weight: 500;">
                        {event['icon']} <strong>{event['date']}</strong> • <em>{event['type']}</em> {flag_html}
                    </div>
                    <div style="font-size: 1.05rem; font-weight: 600; margin-top: 4px; color: #1f2937;">
                        {event['title']}
                    </div>
                    <div style="font-size: 0.92rem; color: #4b5563; margin-top: 2px;">
                        {event['details']}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
