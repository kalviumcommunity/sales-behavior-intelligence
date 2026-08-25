"""
Pipeline Overview View (Tab 1) — Manager Dashboard.
Provides high-level pipeline health, risk filters, and deal table.
"""

import streamlit as st


def render_pipeline_overview(deals):
    """Renders the pipeline overview table and risk breakdown."""
    st.html("### 📊 Active Pipeline Risk Matrix")
    st.caption("Identify deals requiring immediate behavioral coaching intervention.")

    st.markdown("""
        <style>
        .deal-card {
            background-color: #ffffff; 
            border: 1px solid #e5e7eb; 
            padding: 14px 18px; 
            border-radius: 10px; 
            margin-bottom: 12px; 
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }
        .deal-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1), 0 2px 4px -1px rgba(0,0,0,0.06);
        }
        </style>
    """)

    # Filter Bar
    col1, col2, col3 = st.columns([3, 3, 3])
    with col1:
        rep_filter = st.selectbox(
            "Filter by Sales Rep",
            ["All Reps", "Maya Lin", "Alex Rivera", "Jordan Smith"],
        )
    with col2:
        risk_filter = st.selectbox(
            "Filter by Risk Level", ["All Risk Levels", "High", "Medium", "Low"]
        )
    with col3:
        search_query = st.text_input("Search Deal / Company", "")

    # Apply filters
    filtered_deals = deals
    if rep_filter != "All Reps":
        filtered_deals = [d for d in filtered_deals if d["rep_name"] == rep_filter]
    if risk_filter != "All Risk Levels":
        filtered_deals = [d for d in filtered_deals if d["risk_level"] == risk_filter]
    if search_query:
        filtered_deals = [
            d
            for d in filtered_deals
            if search_query.lower() in d["name"].lower()
            or search_query.lower() in d["company"].lower()
        ]

    st.write(f"Showing **{len(filtered_deals)}** of **{len(deals)}** deals")

    # Table view styling using markdown table / container loop
    for deal in filtered_deals:
        risk_badge = (
            "🔴 High Risk"
            if deal["risk_level"] == "High"
            else ("🟡 Medium Risk" if deal["risk_level"] == "Medium" else "🟢 Healthy")
        )

        with st.container():
            st.markdown(f"""
                <div class="deal-card">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <span style="font-size: 1.1rem; font-weight: 700; color: #111827;">{deal['name']}</span>
                        <span style="font-weight: 600; font-size: 0.9rem;">{risk_badge} (Score: {deal['risk_score']}/100)</span>
                    </div>
                    <div style="font-size: 0.9rem; color: #4b5563; margin-top: 6px;">
                        💰 <strong>Value:</strong> ${deal['amount']:,.0f} &nbsp;|&nbsp; 
                        👤 <strong>Rep:</strong> {deal['rep_name']} &nbsp;|&nbsp; 
                        📌 <strong>Stage:</strong> {deal['stage']} ({deal['days_in_stage']} days in stage)
                    </div>
                    <div style="font-size: 0.88rem; color: #dc2626; margin-top: 6px; font-weight: 500;">
                        🚩 <strong>Top Flag:</strong> {deal['top_flag']} &nbsp;•&nbsp; <em>Last activity: {deal['last_activity']}</em>
                    </div>
                </div>
                """)
