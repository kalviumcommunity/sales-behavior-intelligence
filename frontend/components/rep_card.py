import streamlit as st


def render_rep_card(rank, avatar, name, pipeline, win_rate, behavior_score):
    st.markdown(
        f"""
        <div class="rep-card">
            <div style="display:flex; align-items:center; gap:12px; margin-bottom:10px;">
                <div class="rep-card__avatar">{avatar}</div>
                <div>
                    <div class="rep-card__rank">#{rank}</div>
                    <div class="rep-card__name">{name}</div>
                </div>
            </div>
            <div class="rep-card__grid">
                <div><span>Pipeline</span><strong>{pipeline}</strong></div>
                <div><span>Win Rate</span><strong>{win_rate}</strong></div>
                <div><span>Behavior Score</span><strong>{behavior_score}</strong></div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
