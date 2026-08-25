"""Next Best Action Component"""

import streamlit as st


def render_next_best_action(nba_data):
    """Render the Next Best Action panel."""

    st.html(f"""
        <div class='nba-card'>
            <div class='nba-card__label'>NEXT BEST ACTION</div>
            <div class='nba-card__title'>{nba_data["action"]}</div>
            
            <div class='nba-card__grid'>
                <div class='nba-card__field'>
                    <span class='nba-card__field-label'>Priority</span>
                    <span class='nba-card__field-value' style='color: #ff8ea7;'>{nba_data["priority"]}</span>
                </div>
                <div class='nba-card__field'>
                    <span class='nba-card__field-label'>Expected Impact</span>
                    <span class='nba-card__field-value' style='color: #5fd6a0;'>{nba_data["expected_impact"]}</span>
                </div>
                <div class='nba-card__field'>
                    <span class='nba-card__field-label'>Owner</span>
                    <span class='nba-card__field-value'>{nba_data["suggested_owner"]}</span>
                </div>
                <div class='nba-card__field'>
                    <span class='nba-card__field-label'>Deadline</span>
                    <span class='nba-card__field-value'>{nba_data["deadline_hours"]} hours</span>
                </div>
            </div>
            
            <div class='nba-card__details'>
                {nba_data["details"]}
            </div>
        </div>
        """)

    st.markdown("<div style='height: 1rem;'></div>")

    col1, col2, col3 = st.columns([2, 1, 1])
    with col3:
        if st.button("→ Take Action", use_container_width=True, key="nba_take_action"):
            st.toast("Action captured! Add to your task list.", icon="→")
