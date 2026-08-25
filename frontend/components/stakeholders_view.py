"""Stakeholders Component"""

import streamlit as st


def render_stakeholders(stakeholders):
    """Render stakeholder information."""

    st.html("<div class='section-heading'>👥 Stakeholders</div>")

    # Check for single-threaded warning
    engaged_stakeholders = [s for s in stakeholders if s["engagement_level"] != "Low"]
    if len(engaged_stakeholders) <= 1:
        st.html("""
            <div class='warning-banner'>
                ⚠️ <strong>Single-Threaded Opportunity</strong><br/>
                This deal depends on one stakeholder. Expand stakeholder coverage to reduce risk.
            </div>
            """)
        st.markdown("<div style='height: 0.5rem;'></div>")

    for stakeholder in stakeholders:
        engagement_color = (
            "#5fd6a0"
            if stakeholder["engagement_level"] == "High"
            else "#ffb76a" if stakeholder["engagement_level"] == "Medium" else "#ff8ea7"
        )

        engagement_icon = (
            "🟢"
            if stakeholder["engagement_level"] == "High"
            else "🟡" if stakeholder["engagement_level"] == "Medium" else "🔴"
        )

        thread_badge = ""
        if stakeholder["thread_status"] == "primary":
            thread_badge = (
                "<span class='thread-badge thread-badge--primary'>Primary</span>"
            )
        elif stakeholder["thread_status"] == "secondary":
            thread_badge = (
                "<span class='thread-badge thread-badge--secondary'>Secondary</span>"
            )
        elif stakeholder["thread_status"] == "not_engaged":
            thread_badge = "<span class='thread-badge thread-badge--not-engaged'>Not Engaged</span>"

        st.markdown(f"""
            <div class='stakeholder-card'>
                <div class='stakeholder__header'>
                    <div class='stakeholder__info'>
                        <div class='stakeholder__name'>{stakeholder["name"]}</div>
                        <div class='stakeholder__title'>{stakeholder["job_title"]} · {stakeholder["company"]}</div>
                    </div>
                    {thread_badge}
                </div>
                <div class='stakeholder__grid'>
                    <div class='stakeholder__field'>
                        <span class='stakeholder__label'>Engagement</span>
                        <div class='stakeholder__value'>
                            {engagement_icon} {stakeholder["engagement_level"]}
                        </div>
                    </div>
                    <div class='stakeholder__field'>
                        <span class='stakeholder__label'>Role</span>
                        <div class='stakeholder__value'>{stakeholder["role"]}</div>
                    </div>
                    <div class='stakeholder__field'>
                        <span class='stakeholder__label'>Influence</span>
                        <div class='stakeholder__value'>{stakeholder["influence"].title()}</div>
                    </div>
                    <div class='stakeholder__field'>
                        <span class='stakeholder__label'>Last Interaction</span>
                        <div class='stakeholder__value'>{stakeholder["last_interaction"]}</div>
                    </div>
                </div>
            </div>
            """)
