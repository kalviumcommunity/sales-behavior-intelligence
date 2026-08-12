import streamlit as st


def render_meeting_table(meetings):
    rows = "".join(
        f"""
        <tr>
            <td>{meeting['time']}</td>
            <td>{meeting['company']}</td>
            <td>{meeting['rep']}</td>
            <td>{meeting['stage']}</td>
        </tr>
        """
        for meeting in meetings
    )

    st.markdown(
        f"""
        <div class="meeting-table-wrap">
            <table class="meeting-table">
                <thead>
                    <tr>
                        <th>Time</th>
                        <th>Company</th>
                        <th>Rep</th>
                        <th>Stage</th>
                    </tr>
                </thead>
                <tbody>
                    {rows or '<tr><td colspan="4">No upcoming meetings match the current search.</td></tr>'}
                </tbody>
            </table>
        </div>
        """,
        unsafe_allow_html=True,
    )
