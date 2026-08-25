"""
Rep Performance & Coaching Insights View (Tab 3).
Aggregates seller behavior patterns for 1:1 coaching sessions.
"""
import streamlit as st


def render_rep_coaching(reps, deals):
    """Renders representative level behavior analytics and coaching summary."""
    st.markdown("### 👤 Sales Rep Behavior Benchmarking & 1:1 Coaching")
    st.caption("Identify individual seller habits, strengths, and repeatable coaching playbooks.")

    selected_rep_name = st.selectbox("Select Sales Representative", [r["name"] for r in reps])
    selected_rep = next(r for r in reps if r["name"] == selected_rep_name)

    rep_deals = [d for d in deals if d["rep_name"] == selected_rep_name]
    high_risk_rep_deals = [d for d in rep_deals if d["risk_level"] == "High"]

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Assigned Active Deals", len(rep_deals))
    with col2:
        st.metric("Quota Attainment", f"{selected_rep['quota_attainment']}%")
        st.progress(min(selected_rep['quota_attainment'] / 100.0, 1.0))
    with col3:
        st.metric("High Risk Deals", len(high_risk_rep_deals), delta="Needs Coaching" if high_risk_rep_deals else "On Track", delta_color="inverse")

    st.markdown("#### 🎯 Coaching Snapshot for " + selected_rep_name)

    if selected_rep_name == "Maya Lin":
        st.info("💡 **Key Behavioral Insight for Maya**: Maya excels at initial technical discovery and building rapport with technical champions. However, data reveals a pattern of **post-demo proposal follow-up lag** (>48 hours) and **single-threading** on enterprise accounts.")
        st.markdown(
            """
            * **Top Strengths**: Deep technical understanding, high customer engagement on discovery calls.
            * **Primary Coaching Focus**: Booking follow-up proposal review meetings live during demo calls rather than sending quotes asynchronously over email.
            * **Suggested Playbook**: *Multi-Threading Framework & Executive Sponsor Introductions*.
            """
        )
    else:
        st.success(f"💡 **Key Behavioral Insight for {selected_rep_name}**: Maintains strong follow-up cadence and consistent next-step scheduling across deals.")
