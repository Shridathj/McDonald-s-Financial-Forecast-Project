import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="streamlit")
warnings.filterwarnings("ignore", message=".*ScriptRunContext.*")
warnings.filterwarnings("ignore", message=".*missing ScriptRunContext.*")
warnings.filterwarnings("ignore", message=".*Session state does not function.*")

import os
import sys
import importlib
import types
from pathlib import Path
from dataclasses import dataclass
from typing import Optional, Dict, Any, List

import streamlit as st
import pandas as pd

# CONFIG
PROJECT_ROOT = Path(__file__).parent.resolve()
sys.path.insert(0, str(PROJECT_ROOT))

MCD_RED = "#DA291C"
MCD_YELLOW = "#FFC72C"
MCD_DARK = "#1A1A1A"

PAGE_TITLE = "McDonald's Financial Forecast"

@dataclass(frozen=True)
class PageConfig:
    description: str
    module_path: str
    function_name: str

PAGES = {
    "Home":            PageConfig("Project Overview & Navigation", "src.home.home", "home"),
    "Overview":        PageConfig("Income Statement Overview", "src.overview.overview", "overview"),
    "Balance Sheet":   PageConfig("Assets, Liabilities & Equity", "src.balance_sheet.balance_sheet", "balance_sheet"),
    "Cash Flow":       PageConfig("Cash Inflows & Outflows", "src.cash_flow.cash_flow", "cash_flow_statement"),
    "Ratios":          PageConfig("Financial Ratios Analysis", "src.ratios.ratios", "ratio_analysis"),
    "Segment Analysis":PageConfig("Segment-wise Revenue", "src.segment_analysis.segment_analysis", "segment_analysis"),
    "Quarterly Analysis": PageConfig("Quarterly Performance & Seasonality", "src.quarterly_analysis.quarterly_analysis", "quarterly_analysis"),
    "Market Research": PageConfig("Market Research", "src.market_analysis.market_analysis", "market_research"),
    "Assumed Growth":  PageConfig("Growth Assumptions", "src.assumed_growth.assumed_growth", "assumed_growth"),
    "Forecast":        PageConfig("5-Year Forecast", "src.forecast.forecast", "forecast"),
    "References":      PageConfig("Data Sources & References", "src.references.references", "references"),
    "Summary":         PageConfig("Executive Summary", "src.summary.summary", "summary"),
    "Outcome Analysis":PageConfig("Forecast vs Actual", "src.outcome_analysis.outcome_analysis", "outcome_analysis"),
    "Conclusion":      PageConfig("Final Conclusions", "src.conclusion.conclusion", "conclusion"),
}

# PAGE CONFIG
st.set_page_config(page_title=PAGE_TITLE, layout="wide", initial_sidebar_state="expanded")

# STYLES
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');
html, body, [class*="css"] {{ font-family: 'Inter', sans-serif; }}

[data-testid="stSidebar"] {{ background: linear-gradient(180deg, {MCD_DARK} 0%, #2d2b28 100%); border-right: 3px solid {MCD_RED}; }}
[data-testid="stSidebar"] * {{ color: white !important; }}

.stButton > button {{ background: {MCD_RED}; color: white; border-radius: 6px; font-weight: 600; }}
.stButton > button:hover {{ background: {MCD_YELLOW}; color: {MCD_DARK}; }}

.page-banner {{ background: linear-gradient(135deg, {MCD_RED} 0%, #8B0000 100%); padding: 1.6rem 2rem; border-radius: 12px; color: white; margin-bottom: 1.5rem; }}
</style>
""", unsafe_allow_html=True)

# SIDEBAR
with st.sidebar:
    st.markdown(f"""
    <div style="text-align:center; padding: 1.5rem 0 1rem;">
        <h2 style="color: {MCD_YELLOW}; margin:0;">McDonald's</h2>
        <p style="color:#aaa; margin:0.3rem 0 0;">Financial Forecast Dashboard</p>
    </div>
    """, unsafe_allow_html=True)
    
    selected = st.radio(
        "Navigation",
        list(PAGES.keys()),
        index=list(PAGES.keys()).index(st.session_state.get("page", "Home")),
        label_visibility="collapsed"
    )
    
    if selected != st.session_state.get("page", "Home"):
        st.session_state.page = selected
        st.rerun()

    st.markdown("---")
    st.caption("Prepared by Pranav J • 11 March 2025")

# MAIN LOGIC
def main():
    page = st.session_state.get("page", "Home")
    cfg = PAGES[page]

    if page == "Home":
        try:
            mod = importlib.import_module(cfg.module_path)
            getattr(mod, cfg.function_name)()
        except Exception as e:
            st.error(f"Error loading Home: {e}")
            st.code(str(e))
    else:
        st.markdown(f'<div class="page-banner"><h1>{page}</h1><p>{cfg.description}</p></div>', unsafe_allow_html=True)
        
        try:
            mod = importlib.import_module(cfg.module_path)
            getattr(mod, cfg.function_name)()
        except Exception as e:
            st.error(f"Error in {page}")
            st.code(str(e))

        if st.button("← Back to Home"):
            st.session_state.page = "Home"
            st.rerun()

if __name__ == "__main__":
    if "page" not in st.session_state:
        st.session_state.page = "Home"
    main()
