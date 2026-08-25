"""Behavioral Intelligence Signals Component"""

import streamlit as st


def render_behavioral_signals(signals):
    """Render behavioral intelligence signals with scores."""

    st.html("<div class='section-heading'>💡 Behavioral Intelligence</div>")

    for signal in signals:
        score_pct = (signal["score"] / signal["max_score"]) * 100

        # Determine color based on severity
        if signal["severity"] == "high":
            color = "#ff8ea7"
            icon = "⚠️"
        elif signal["severity"] == "medium":
            color = "#ffb76a"
            icon = "→"
        else:
            color = "#5fd6a0"
            icon = "✓"

        st.html(f"""
            <div class='behavioral-signal-card'>
                <div class='behavioral-signal__header'>
                    <div class='behavioral-signal__name'>{icon} {signal["signal_name"]}</div>
                    <div class='behavioral-signal__score'>
                        <span class='behavioral-signal__number' style='color: {color};'>
                            {signal["score"]} / {signal["max_score"]}
                        </span>
                    </div>
                </div>
                <div class='behavioral-signal__bar'>
                    <div class='behavioral-signal__progress' style='width: {score_pct}%; background-color: {color};'></div>
                </div>
                <div class='behavioral-signal__insight'>
                    {signal["insight"]}
                </div>
            </div>
            """)

        st.markdown("<div style='height: 0.5rem;'></div>")
