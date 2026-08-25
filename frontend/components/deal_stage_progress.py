"""Deal Stage Progress Component"""

import streamlit as st


def render_deal_stage_progress(stages):
    """Render deal stage progression."""

    st.html("<div class='section-heading'>📈 Deal Progression</div>")

    # Calculate stage HTML
    stage_items = []
    for i, stage in enumerate(stages):
        if stage.get("current"):
            class_name = "stage-item stage-item--current"
            icon = "→"
        elif stage.get("completed"):
            class_name = "stage-item stage-item--completed"
            icon = "✓"
        else:
            class_name = "stage-item stage-item--upcoming"
            icon = "◌"

        stage_items.append(f"""
            <div class='{class_name}'>
                <div class='stage-item__icon'>{icon}</div>
                <div class='stage-item__name'>{stage["name"]}</div>
            </div>
            """)

        # Add arrow between stages
        if i < len(stages) - 1:
            stage_items.append('<div class="stage-item__arrow">↓</div>')

    st.markdown(f"""
        <div class='stage-progression'>
            {''.join(stage_items)}
        </div>
        """)
