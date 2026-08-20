"""Deal Timeline Visual Component"""
import streamlit as st


def render_deal_timeline(timeline_events):
    """Render chronological deal timeline."""
    
    st.html("<div class='section-heading'>📅 Deal Timeline</div>")
    
    for event in timeline_events:
        # Determine icon and color based on event type
        type_config = {
            "stage_change": {"icon": "📌", "color": "#57d8ff"},
            "meeting": {"icon": "👥", "color": "#9a86ff"},
            "email": {"icon": "✉️", "color": "#7ab8ff"},
            "call": {"icon": "☎️", "color": "#59d19b"},
            "signal": {"icon": "🚩", "color": "#ff8ea7"},
        }
        
        config = type_config.get(event["event_type"], {"icon": "◌", "color": "#93a4bd"})
        
        st.markdown(
            f"""
            <div class='timeline-event'>
                <div class='timeline-event__icon' style='background-color: {config["color"]}20; border-color: {config["color"]};'>
                    {config["icon"]}
                </div>
                <div class='timeline-event__content'>
                    <div class='timeline-event__date-type'>
                        <span class='timeline-event__date'>{event["date"]}</span>
                        <span class='timeline-event__type'>{event["event_type"].replace("_", " ").title()}</span>
                    </div>
                    <div class='timeline-event__title'>{event["title"]}</div>
                    <div class='timeline-event__description'>{event["description"]}</div>
                    {f'<div class="timeline-event__person">👤 {event["related_person"]}</div>' if event["related_person"] else ''}
                </div>
            </div>
            """
        )
