from datetime import date

import os
import requests
from frontend.mock_data import MOCK_COACHING_CARDS, MOCK_DEALS as _MOCK_DEALS, MOCK_REPS as _MOCK_REPS, MOCK_TIMELINES

API_BASE = os.getenv("API_URL", "http://localhost:8000/api")

def _fetch_api(endpoint, default_data):
    try:
        res = requests.get(f"{API_BASE}/{endpoint}", timeout=2)
        if res.ok: return res.json()
    except Exception: pass
    return default_data

MOCK_DEALS = _fetch_api("deals", _MOCK_DEALS)
MOCK_REPS = _fetch_api("reps", _MOCK_REPS)


def money(value):
    return f"${value:,.0f}"


CURRENT_USER = {
    "name": "Sarah Johnson",
    "role": "Sales Manager",
    "team": "Enterprise Growth",
    "email": "sarah.johnson@salesbehaviour.ai",
    "avatar": "SJ",
}

DASHBOARD_NAV_ITEMS = [
    {"label": "Dashboard", "icon": "◼"},
    {"label": "Deals", "icon": "◆"},
    {"label": "Sales Reps", "icon": "◉"},
    {"label": "AI Coaching", "icon": "✦"},
    {"label": "Analytics", "icon": "▣"},
    {"label": "Settings", "icon": "⚙"},
    {"label": "Logout", "icon": "↪"},
]

CURRENT_DATE = date(2026, 8, 6).strftime("%A, %b %d, %Y")
BREADCRUMB = "Home / Manager Dashboard"

TOTAL_PIPELINE = sum(deal["amount"] for deal in MOCK_DEALS)
OPEN_DEALS = len(MOCK_DEALS)
WIN_RATE = 68
REVENUE = 1845000
AVG_RISK_SCORE = round(sum(deal["risk_score"] for deal in MOCK_DEALS) / len(MOCK_DEALS))
ACTIVE_REPS = len(MOCK_REPS)
COACHING_ALERTS = sum(len(cards) for cards in MOCK_COACHING_CARDS.values())
DEALS_CLOSING_THIS_WEEK = 2

KPI_METRICS = [
    {"label": "Total Pipeline", "value": money(TOTAL_PIPELINE), "detail": f"{OPEN_DEALS} open deals", "accent": "cyan"},
    {"label": "Open Deals", "value": str(OPEN_DEALS), "detail": "Active opportunities in play", "accent": "blue"},
    {"label": "Win Rate", "value": f"{WIN_RATE}%", "detail": "Trailing 90 days", "accent": "green"},
    {"label": "Revenue", "value": money(REVENUE), "detail": "Closed won this year", "accent": "violet"},
    {"label": "Average Risk Score", "value": f"{AVG_RISK_SCORE}/100", "detail": "Behavioral health across book", "accent": "orange"},
    {"label": "Active Reps", "value": str(ACTIVE_REPS), "detail": "Selling with the team", "accent": "teal"},
    {"label": "Coaching Alerts", "value": str(COACHING_ALERTS), "detail": "Actions waiting on managers", "accent": "rose"},
    {"label": "Deals Closing This Week", "value": str(DEALS_CLOSING_THIS_WEEK), "detail": "Expected to land soon", "accent": "gold"},
]

REVENUE_TREND = [
    {"month": "Jan", "revenue": 240000},
    {"month": "Feb", "revenue": 275000},
    {"month": "Mar", "revenue": 298000},
    {"month": "Apr", "revenue": 318000},
    {"month": "May", "revenue": 351000},
    {"month": "Jun", "revenue": 375000},
]

PIPELINE_BY_STAGE = [
    {"stage": "Discovery", "count": 1},
    {"stage": "Demo Completed", "count": 1},
    {"stage": "Proposal Sent", "count": 1},
    {"stage": "Solution Validation", "count": 1},
    {"stage": "Negotiation", "count": 1},
]

WIN_LOSS_RATIO = [
    {"outcome": "Won", "value": 12},
    {"outcome": "Lost", "value": 5},
]

RISK_DISTRIBUTION = [
    {"bucket": "Low", "value": 2},
    {"bucket": "Medium", "value": 2},
    {"bucket": "High", "value": 1},
]

MONTHLY_PERFORMANCE = [
    {"month": "Jan", "pipeline": 82, "win_rate": 61, "coaching_completion": 48},
    {"month": "Feb", "pipeline": 84, "win_rate": 62, "coaching_completion": 53},
    {"month": "Mar", "pipeline": 89, "win_rate": 64, "coaching_completion": 57},
    {"month": "Apr", "pipeline": 92, "win_rate": 66, "coaching_completion": 61},
    {"month": "May", "pipeline": 95, "win_rate": 67, "coaching_completion": 66},
    {"month": "Jun", "pipeline": 98, "win_rate": 68, "coaching_completion": 70},
]

RECENT_ACTIVITIES = [
    {"time": "10:30 AM", "title": "John updated ACME Deal", "detail": "Stage changed to Proposal Sent and risk score updated to 78.", "icon": "◌"},
    {"time": "10:15 AM", "title": "Meeting Completed", "detail": "Sarah Johnson finished a deal review with Maya Lin and sales ops.", "icon": "◌"},
    {"time": "09:45 AM", "title": "Proposal Sent", "detail": "Apex Logistics received the final proposal with finance attached.", "icon": "◌"},
    {"time": "09:20 AM", "title": "New Lead Added", "detail": "Inbound enterprise opportunity routed into the manager queue.", "icon": "◌"},
]

HIGH_RISK_DEALS = [
    {
        "company": deal["company"],
        "deal_value": money(deal["amount"]),
        "risk_score": f"{deal['risk_score']}/100",
        "stage": deal["stage"],
        "assigned_rep": deal["rep_name"],
        "recommended_action": "Book a live review with finance and procurement before momentum decays.",
    }
    for deal in MOCK_DEALS
    if deal["risk_level"] == "High"
]

COACHING_SUGGESTIONS = [
    {
        "rep": "Maya Lin",
        "problem": "Slow post-demo follow-up",
        "suggestion": "Pre-book the proposal review meeting while the demo is still live.",
        "confidence": 96,
    },
    {
        "rep": "Jordan Smith",
        "problem": "Thin discovery",
        "suggestion": "Use a structured question map to confirm pain, budget, and decision process.",
        "confidence": 91,
    },
    {
        "rep": "Alex Rivera",
        "problem": "Stakeholder mapping not complete",
        "suggestion": "Add an executive sponsor before the contract reaches legal.",
        "confidence": 88,
    },
]

TOP_REPS = [
    {"rank": 1, "avatar": "AR", "name": "Alex Rivera", "pipeline": money(595000), "win_rate": "94%", "behavior_score": 96},
    {"rank": 2, "avatar": "ML", "name": "Maya Lin", "pipeline": money(410000), "win_rate": "82%", "behavior_score": 77},
    {"rank": 3, "avatar": "JS", "name": "Jordan Smith", "pipeline": money(285000), "win_rate": "68%", "behavior_score": 71},
]

UPCOMING_MEETINGS = [
    {"time": "11:00 AM", "company": "Starlight Media", "rep": "Alex Rivera", "stage": "Negotiation / Legal"},
    {"time": "01:30 PM", "company": "Acme Corp", "rep": "Maya Lin", "stage": "Proposal Sent"},
    {"time": "03:00 PM", "company": "Vortex Systems", "rep": "Alex Rivera", "stage": "Solution Validation"},
    {"time": "04:15 PM", "company": "Nexus Technologies", "rep": "Jordan Smith", "stage": "Demo Completed"},
]

QUICK_ACTIONS = [
    {"label": "Add Deal", "description": "Capture a new opportunity before follow-up slips.", "icon": "＋"},
    {"label": "Add Rep", "description": "Create a seller profile and attach coaching goals.", "icon": "◉"},
    {"label": "Schedule Meeting", "description": "Book the next checkpoint for active deals.", "icon": "🗓"},
    {"label": "View Reports", "description": "Open analytics and forecast views for leadership.", "icon": "▤"},
    {"label": "AI Analysis", "description": "Run coaching suggestions across the current pipeline.", "icon": "✦"},
]

DEAL_TIMELINE_LOOKUP = MOCK_TIMELINES
COACHING_LOOKUP = MOCK_COACHING_CARDS
