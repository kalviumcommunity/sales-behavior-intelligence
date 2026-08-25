"""Activity Tabs Component"""

import streamlit as st


def render_activity_tabs(activity_data):
    """Render tabbed activity view (emails, calls, meetings, notes)."""

    st.html("<div class='section-heading'>📬 Activity</div>")

    tabs = st.tabs(["Emails", "Calls", "Meetings", "Notes"])

    # Emails tab
    with tabs[0]:
        st.html(
            "<div class='activity-count'>Total: {} emails</div>".format(
                len(activity_data["emails"])
            )
        )
        for email in activity_data["emails"]:
            response_color = (
                "#5fd6a0" if email["response_status"] == "Responded" else "#ffb76a"
            )
            st.html(f"""
                <div class='activity-card activity-card--email'>
                    <div class='activity-card__header'>
                        <div class='activity-card__sender'>{email["sender"]}</div>
                        <div class='activity-card__status' style='color: {response_color};'>{email["response_status"]}</div>
                    </div>
                    <div class='activity-card__subject'>{email["subject"]}</div>
                    <div class='activity-card__time'>{email["time"]}</div>
                </div>
                """)

    # Calls tab
    with tabs[1]:
        st.markdown(
            "<div class='activity-count'>Total: {} calls</div>".format(
                len(activity_data["calls"])
            )
        )
        for call in activity_data["calls"]:
            participants = ", ".join(call["participants"])
            st.html(f"""
                <div class='activity-card activity-card--call'>
                    <div class='activity-card__header'>
                        <div class='activity-card__title'>{call["title"]}</div>
                        <div class='activity-card__meta'>{call["duration"]}</div>
                    </div>
                    <div class='activity-card__participants'>👥 {participants}</div>
                    <div class='activity-card__summary'>{call["summary"]}</div>
                    <div class='activity-card__time'>{call["date"]}</div>
                </div>
                """)

    # Meetings tab
    with tabs[2]:
        st.markdown(
            "<div class='activity-count'>Total: {} meetings</div>".format(
                len(activity_data["meetings"])
            )
        )
        for meeting in activity_data["meetings"]:
            participants = ", ".join(meeting["participants"])
            st.html(f"""
                <div class='activity-card activity-card--meeting'>
                    <div class='activity-card__header'>
                        <div class='activity-card__title'>{meeting["name"]}</div>
                    </div>
                    <div class='activity-card__date'>{meeting["date"]}</div>
                    <div class='activity-card__participants'>👥 {participants}</div>
                    <div class='activity-card__outcome'>
                        <strong>Outcome:</strong> {meeting["outcome"]}
                    </div>
                </div>
                """)

    # Notes tab
    with tabs[3]:
        st.markdown(
            "<div class='activity-count'>Total: {} notes</div>".format(
                len(activity_data["notes"])
            )
        )
        for note in activity_data["notes"]:
            st.markdown(f"""
                <div class='activity-card activity-card--note'>
                    <div class='activity-card__header'>
                        <div class='activity-card__author'>{note["author"]}</div>
                        <div class='activity-card__date'>{note["date"]}</div>
                    </div>
                    <div class='activity-card__content'>
                        {note["content"]}
                    </div>
                </div>
                """)
