# Sales Behavior Intelligence - Quick Reference

## 🚀 Quick Start

### Run Locally
```bash
streamlit run app.py
```

### Login (Any credentials work)
- Email: anything@example.com
- Password: anything

---

## 📊 Pages Overview

| Page | Route | Purpose | Key Features |
|------|-------|---------|--------------|
| **Landing** | `/app.py` | Marketing site | Hero, features, pricing, testimonials |
| **Auth** | `/Authentication` | User login | Email/password, session state |
| **Dashboard** | `/dashboard` | Executive view | 8 KPIs, 5 charts, activities, coaching |
| **Deals** | `/2_Deals` | Pipeline list | Filters, search, sort, 20+ deals |
| **Deal Details** | `/3_Deal_Details` | Deal deep dive | Health, timeline, signals, risk, coaching |

---

## 🎨 Design System

**Colors:**
- Cyan: `#5EE7FF` (primary accent)
- Violet: `#8B7CFF` (secondary)
- Green: `#4ADE80` (success)
- Red: `#FB7185` (danger)
- BG Dark: `#070A12`

**Spacing:** 4px, 8px, 12px, 16px, 20px, 24px, 32px...

**Font:** Inter (or system sans-serif)

**Radius:** 8px (small), 12px (cards), 22px (sections)

---

## 📁 Key Files

```
frontend/
├── design_system.py          ← All design tokens & CSS
├── landing_page.py           ← Landing page
├── components/               ← 20+ reusable components
│   ├── app_shell.py         ← NEW: App wrapper
│   ├── metric_card.py       ← NEW: KPI display
│   └── badge.py             ← NEW: Status badges
└── *_data.py                ← Mock data for each page

pages/
├── 1_Authentication.py       ← Login page
├── 2_Deals.py               ← Pipeline view
├── 3_Deal_Details.py        ← Deal analysis
└── dashboard.py             ← Executive dashboard
```

---

## 🔄 Session State

```python
# Authentication
st.session_state.authenticated  # True/False

# Navigation
st.session_state.current_page   # "dashboard", "deals", etc.

# Deal Selection
st.session_state.deals_selected_deal  # Current deal dict

# Filters (Deals page)
st.session_state.deals_search
st.session_state.deals_stage_filter
st.session_state.deals_risk_filter
st.session_state.deals_rep_filter
st.session_state.deals_size_filter
st.session_state.deals_close_filter
st.session_state.deals_sort_filter
```

---

## 📊 Mock Data

**Location:** `frontend/*_data.py`

**Includes:**
- 8 KPI metrics
- 100+ chart data points
- 20 deals with full details
- 3 testimonials
- 7 FAQs
- 6 features
- 4-step process

---

## 🎯 Component Usage

### Import & Use
```python
from frontend.components.metric_card import render_metric
from frontend.design_system import get_global_css

# Apply design system
st.markdown(get_global_css(), unsafe_allow_html=True)

# Render metric
render_metric(
    label="Total Pipeline",
    value="$1.84M",
    trend="+12.4%",
    trend_direction="up"
)
```

---

## 🌐 Responsive Breakpoints

| Breakpoint | Width | Changes |
|------------|-------|---------|
| Desktop | 1920px+ | Full layout, all features |
| Large Tablet | 1440px | Slightly compressed |
| Tablet | 1024px | 2-column grids |
| Mobile | 768px | Sidebar → drawer, 1 column |
| Small Mobile | 480px | Large fonts, stacked layout |

---

## 📍 How It Works

### Deal Health Score
- 0-100 scale
- Green (70+), Yellow (50-70), Red (<50)
- Calculated from signals, activity, timeline

### Behavioral Signals
1. Follow-up timing
2. Stakeholder coverage
3. Next-step clarity
4. Engagement frequency

### Risk Levels
- **Low** - On track, no concerns
- **Medium** - Monitor, may need attention
- **High** - Requires immediate action

---

## 🛠️ Development

### Add New Page
1. Create `pages/N_PageName.py`
2. Check authentication at top
3. Import components & mock data
4. Build layout using Streamlit
5. Add sidebar navigation link

### Add New Component
1. Create `frontend/components/component_name.py`
2. Define function with parameters
3. Use design system CSS
4. Return st.markdown() with HTML
5. Export function

### Update Design
1. Edit `frontend/design_system.py`
2. Change DESIGN_TOKENS dict
3. Update CSS in get_global_css()
4. Changes apply globally

---

## 🎬 Common Tasks

### Search & Filter
```python
# All on Deals page
search_query = st.text_input("Search")
stage = st.selectbox("Stage", stages)
risk = st.selectbox("Risk", risks)

# Apply filters
filtered = [d for d in deals if search_query.lower() in d["company"].lower()]
```

### Navigate Between Pages
```python
# To go to another page
if st.button("View Deal"):
    st.session_state.deals_selected_deal = deal
    st.switch_page("pages/3_Deal_Details.py")
```

### Display a Card
```python
# Using design system CSS
st.markdown("""
    <div style="padding: 16px; background: rgba(255,255,255,0.02); 
                border: 1px solid rgba(255,255,255,0.08); border-radius: 12px;">
        <div style="font-weight: 700;">Card Title</div>
        <p style="color: #A7B0C0;">Card description</p>
    </div>
""", unsafe_allow_html=True)
```

---

## 🚨 Troubleshooting

| Issue | Solution |
|-------|----------|
| Can't login | Any credentials work (mock) |
| Page not loading | Check `st.session_state.authenticated` |
| Charts not showing | Check data structure in `*_data.py` |
| Layout broken | Verify column widths sum properly |
| Colors wrong | Check `design_system.py` for hex values |

---

## 📚 Documentation

- **`WEBSITE_OVERVIEW.md`** - Comprehensive project docs
- **`COMPLETION_SUMMARY.md`** - What was done & how to use
- **`QUICK_REFERENCE.md`** - This file
- **`README.md`** - Project overview

---

## 🔗 Git Commands

```bash
# Current branch
git branch -v

# View commits
git log --oneline -10

# Check status
git status

# Create new branch
git branch feature/new-feature
git checkout feature/new-feature

# Commit changes
git add .
git commit -m "feat: description"

# Push to remote
git push origin feature/new-feature
```

---

## 📞 Quick Help

**Q: How do I change the color scheme?**
A: Edit `DESIGN_TOKENS` in `frontend/design_system.py`

**Q: How do I add a new filter to Deals?**
A: Add selectbox in `pages/2_Deals.py`, add to state dict, filter in `_get_filtered_deals()`

**Q: How do I connect to a real backend?**
A: Replace mock data in `frontend/*_data.py` with API calls

**Q: How do I test responsiveness?**
A: Open browser DevTools, use device emulation at breakpoints

**Q: How do I add a new page?**
A: Create file in `pages/`, add to sidebar navigation

---

## ✅ Checklist for Next Development

- [ ] Review `WEBSITE_OVERVIEW.md`
- [ ] Study design system in `design_system.py`
- [ ] Explore each page locally
- [ ] Plan next feature
- [ ] Create feature branch
- [ ] Reference docs when coding
- [ ] Test responsive design
- [ ] Commit with clear messages

---

Generated: August 13, 2026
Version: 1.0
