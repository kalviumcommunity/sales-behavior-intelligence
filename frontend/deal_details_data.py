"""
Mock data for Deal Details page.
Contains all data for a single deal including behavioral signals, stakeholders, timeline, and coaching recommendations.
"""

from datetime import date, datetime, timedelta


def get_deal_details(deal_id):
    """Fetch detailed deal information by deal_id."""
    # For MVP, return mock deal details for deal_201
    if deal_id != "deal_201":
        deal_id = "deal_201"

    return {
        "id": "deal_201",
        "company": "Acme Corporation",
        "deal_name": "Enterprise Platform Expansion",
        "deal_value": 245000,
        "stage": "Proposal",
        "risk_level": "High",
        "risk_score": 68,
        "assigned_rep": "Sarah Johnson",
        "expected_close": date(2026, 8, 28),
        "created_date": date(2026, 6, 28),
        "days_open": 47,
        "days_in_stage": 8,
        "stakeholders_count": 3,
        "interactions_count": 18,
        "last_activity": datetime(2026, 8, 10, 14, 30),
        "last_activity_label": "2 hours ago",
        "next_step": "Executive review (not confirmed)",
    }


def get_deal_health_metrics(deal_id):
    """Get deal health overview metrics."""
    return {
        "health_score": 68,
        "health_max": 100,
        "risk_level": "High",
        "deal_velocity": "Below Team Average",
        "velocity_trend": "↓ -12%",
        "engagement": "Moderate",
        "engagement_trend": "→ Flat",
        "next_step_confirmed": False,
    }


def get_ai_summary(deal_id):
    """Get AI-generated deal summary."""
    return {
        "summary": (
            "This opportunity has progressed steadily through qualification and reached the proposal stage, "
            "but momentum has weakened over the last 8 days. The customer has engaged with the proposal, "
            "but executive stakeholder coverage remains limited. The next meeting does not yet have a confirmed decision-maker."
        ),
        "key_signals": [
            "Proposal follow-up delayed",
            "Single-threaded opportunity",
            "Strong product engagement",
            "No confirmed executive meeting",
        ],
        "confidence": 92,
    }


def get_behavioral_signals(deal_id):
    """Get behavioral intelligence signals."""
    return [
        {
            "signal_name": "Follow-up Timing",
            "score": 62,
            "max_score": 100,
            "insight": "Average follow-up time increased after proposal delivery. Last contact was 48 hours ago, above your team average of 24 hours.",
            "severity": "medium",
        },
        {
            "signal_name": "Stakeholder Coverage",
            "score": 48,
            "max_score": 100,
            "insight": "Only one active stakeholder is engaged in the opportunity. Economic buyer and executive sponsor have not participated in recent interactions.",
            "severity": "high",
        },
        {
            "signal_name": "Next-Step Clarity",
            "score": 55,
            "max_score": 100,
            "insight": "Recent interactions ended without a confirmed customer commitment. The next scheduled meeting has no clear agenda or decision-making authority confirmed.",
            "severity": "high",
        },
        {
            "signal_name": "Engagement Momentum",
            "score": 74,
            "max_score": 100,
            "insight": "Customer engagement remains healthy despite slower follow-up. Proposal views and email opens show sustained interest over the past week.",
            "severity": "low",
        },
    ]


def get_stakeholders(deal_id):
    """Get stakeholder information for the deal."""
    return [
        {
            "name": "John Carter",
            "job_title": "VP Engineering",
            "company": "Acme Corporation",
            "engagement_level": "High",
            "last_interaction": "2 days ago",
            "role": "Technical Champion",
            "influence": "high",
            "thread_status": "primary",
        },
        {
            "name": "Lisa Park",
            "job_title": "Director of Operations",
            "company": "Acme Corporation",
            "engagement_level": "Medium",
            "last_interaction": "5 days ago",
            "role": "Operational Stakeholder",
            "influence": "medium",
            "thread_status": "secondary",
        },
        {
            "name": "Michael Chen",
            "job_title": "CFO",
            "company": "Acme Corporation",
            "engagement_level": "Low",
            "last_interaction": "Never contacted",
            "role": "Economic Buyer",
            "influence": "high",
            "thread_status": "not_engaged",
        },
        {
            "name": "Jennifer Martinez",
            "job_title": "VP Sales Operations",
            "company": "Acme Corporation",
            "engagement_level": "Medium",
            "last_interaction": "3 days ago",
            "role": "Process Owner",
            "influence": "medium",
            "thread_status": "secondary",
        },
    ]


def get_deal_timeline(deal_id):
    """Get chronological timeline of deal activities."""
    return [
        {
            "date": "June 28",
            "event_type": "stage_change",
            "icon": "📌",
            "title": "Opportunity Created",
            "description": "Deal record created and qualification began with initial discovery notes.",
            "related_person": None,
        },
        {
            "date": "July 2",
            "event_type": "meeting",
            "icon": "📞",
            "title": "Discovery Call Completed",
            "description": "John Carter (Technical Champion) participated. Pain points identified around integration challenges.",
            "related_person": "John Carter",
        },
        {
            "date": "July 7",
            "event_type": "meeting",
            "icon": "👥",
            "title": "Technical Demo Completed",
            "description": "Demo presented to John Carter and team. Strong positive feedback on feature set.",
            "related_person": "John Carter, Lisa Park",
        },
        {
            "date": "July 12",
            "event_type": "meeting",
            "icon": "💵",
            "title": "Pricing Discussion",
            "description": "Commercial terms discussed. Customer expressed interest in annual commitment.",
            "related_person": "John Carter",
        },
        {
            "date": "July 18",
            "event_type": "stage_change",
            "icon": "📧",
            "title": "Proposal Sent",
            "description": "Formal proposal document delivered to John Carter via email.",
            "related_person": "John Carter",
        },
        {
            "date": "July 20",
            "event_type": "email",
            "icon": "📨",
            "title": "Customer Opened Proposal",
            "description": "Proposal opened 3 times; viewed 12 pages total.",
            "related_person": None,
        },
        {
            "date": "July 22",
            "event_type": "email",
            "icon": "✉️",
            "title": "Follow-up Email Sent",
            "description": "Follow-up email sent to John Carter asking for initial feedback.",
            "related_person": "John Carter",
        },
        {
            "date": "July 25",
            "event_type": "signal",
            "icon": "⚠️",
            "title": "No Response Detected",
            "description": "No response to follow-up email after 72 hours. Follow-up cadence delayed.",
            "related_person": None,
        },
        {
            "date": "July 28",
            "event_type": "signal",
            "icon": "🚩",
            "title": "Risk Signal Generated",
            "description": "Behavioral AI detected single-threaded opportunity risk. Recommend stakeholder expansion.",
            "related_person": None,
        },
        {
            "date": "Aug 2",
            "event_type": "meeting",
            "icon": "📞",
            "title": "Recovery Call",
            "description": "Call with John Carter to discuss proposal feedback. Scheduled executive review meeting.",
            "related_person": "John Carter",
        },
        {
            "date": "Aug 10",
            "event_type": "email",
            "icon": "📧",
            "title": "Executive Meeting Prep",
            "description": "Email sent sharing executive briefing materials. No confirmation of CFO participation yet.",
            "related_person": "John Carter",
        },
    ]


def get_activity_sections(deal_id):
    """Get activity by type (emails, calls, meetings, notes)."""
    return {
        "emails": [
            {
                "sender": "Sarah Johnson",
                "subject": "RE: Enterprise Platform Expansion Proposal - Next Steps",
                "time": "Today, 9:45 AM",
                "response_status": "Awaiting response",
            },
            {
                "sender": "John Carter",
                "subject": "RE: Technical deep-dive - Available next Thursday",
                "time": "Yesterday, 3:22 PM",
                "response_status": "Responded",
            },
            {
                "sender": "Sarah Johnson",
                "subject": "Follow-up on Proposal - Your Thoughts?",
                "time": "July 22, 2:15 PM",
                "response_status": "Opened but not responded",
            },
            {
                "sender": "John Carter",
                "subject": "RE: Proposal sent - Team is reviewing",
                "time": "July 20, 11:08 AM",
                "response_status": "Responded",
            },
        ],
        "calls": [
            {
                "title": "Recovery Discussion with John Carter",
                "duration": "24 minutes",
                "participants": ["Sarah Johnson", "John Carter"],
                "summary": "Discussed proposal feedback. John expressed strong technical alignment. Scheduled executive briefing for next week.",
                "date": "Aug 2, 2:00 PM",
            },
            {
                "title": "Pricing & Commercial Terms",
                "duration": "18 minutes",
                "participants": ["Sarah Johnson", "John Carter"],
                "summary": "Went through pricing tiers and volume discounts. Customer interested in annual commitment.",
                "date": "July 12, 10:30 AM",
            },
        ],
        "meetings": [
            {
                "name": "Technical Demo",
                "date": "July 7, 2:00 PM",
                "participants": ["Sarah Johnson", "John Carter", "Lisa Park"],
                "outcome": "Strong positive feedback. Customization requests noted.",
            },
            {
                "name": "Discovery Call",
                "date": "July 2, 1:30 PM",
                "participants": ["Sarah Johnson", "John Carter"],
                "outcome": "Pain points identified. Product fit confirmed.",
            },
        ],
        "notes": [
            {
                "date": "Aug 8",
                "author": "Sarah Johnson",
                "content": "Need to get Lisa Park and Michael Chen (CFO) on the executive review call. Single-threaded risk is real.",
            },
            {
                "date": "Aug 2",
                "author": "Sarah Johnson",
                "content": "John mentioned budget was approved by CFO but CFO hasn't participated directly. Push for executive involvement.",
            },
        ],
    }


def get_risk_factors(deal_id):
    """Get risk analysis for the deal."""
    return [
        {
            "severity": "HIGH",
            "reason": "No executive stakeholder",
            "description": "Deal is dependent on one technical stakeholder (John Carter). CFO and executive sponsor have not been directly engaged.",
            "recommended_action": "Schedule executive-level conversation within 48 hours. Leverage technical champion to facilitate introduction.",
            "impact": "Deal could be delayed or lost if technical champion changes priorities.",
        },
        {
            "severity": "MEDIUM",
            "reason": "Proposal follow-up delayed",
            "description": "Follow-up cadence has slowed since proposal was sent. Last contact was 48 hours ago.",
            "recommended_action": "Send value-add email or schedule check-in call within 24 hours. Share customer success stories.",
            "impact": "Extended timeline could allow competing solutions to enter the conversation.",
        },
        {
            "severity": "MEDIUM",
            "reason": "No confirmed next meeting",
            "description": "Executive review meeting is proposed but not yet confirmed on calendar.",
            "recommended_action": "Confirm meeting time, participants, and agenda with John Carter immediately.",
            "impact": "Deal momentum could stall if next step is ambiguous.",
        },
        {
            "severity": "LOW",
            "reason": "Customer engagement declining",
            "description": "Email open rates have decreased week-over-week. Customer hasn't opened last two emails.",
            "recommended_action": "Personalize next outreach. Consider phone call to reconnect.",
            "impact": "May indicate shifting priorities at customer but too early to escalate.",
        },
    ]


def get_coaching_recommendation(deal_id):
    """Get coaching recommendation for the sales rep."""
    return {
        "title": "Coach Sarah to multi-thread the opportunity before the next proposal discussion",
        "why": "The deal currently depends heavily on one technical stakeholder (John Carter). Executive and financial decision-makers have not been directly involved in the sales process.",
        "recommended_action": "Ask the technical champion to introduce the economic buyer (CFO Michael Chen) and executive sponsor before the next meeting. Frame it as 'need to align on implementation timeline and budget authority.'",
        "expected_impact": "Increase stakeholder coverage from single-threaded to multi-threaded. Reduce deal slippage risk and accelerate decision-making.",
        "confidence": 94,
    }


def get_next_best_action(deal_id):
    """Get the next best action to move the deal forward."""
    return {
        "action": "Schedule an executive-level conversation within the next 48 hours.",
        "priority": "High",
        "expected_impact": "High",
        "suggested_owner": "Sarah Johnson",
        "deadline_hours": 48,
        "details": "Use technical champion (John Carter) to facilitate. Focus on implementation timeline and resource alignment with CFO and VP Operations.",
    }


def get_deal_stages():
    """Get deal stage progression."""
    return [
        {"name": "Discovery", "completed": True},
        {"name": "Qualification", "completed": True},
        {"name": "Proposal", "completed": False, "current": True},
        {"name": "Negotiation", "completed": False},
        {"name": "Contract", "completed": False},
        {"name": "Closed Won", "completed": False},
    ]
