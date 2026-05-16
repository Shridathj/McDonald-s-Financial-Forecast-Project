import sys
import importlib
import types
from pathlib import Path
from dataclasses import dataclass
from typing import Optional, Dict, Any, List, Tuple

import streamlit as st
import pandas as pd

# ══════════════════════════════════════════════════════════════
# 0. PROJECT CONFIGURATION
# ══════════════════════════════════════════════════════════════

PROJECT_ROOT = Path(__file__).parent.resolve()
sys.path.insert(0, str(PROJECT_ROOT))

# McDonald's Brand Colors (official palette)
MCD_RED: str = "#DA291C"
MCD_YELLOW: str = "#FFC72C"
MCD_DARK: str = "#1A1A1A"
MCD_MID: str = "#27251F"
MCD_LIGHT: str = "#F5F5F5"

PAGE_TITLE: str = "McDonald's Financial Forecast"
PAGE_ICON: str = "🍔"

@dataclass(frozen=True)
class PageConfig:
    """Immutable configuration for each dashboard page."""
    icon: str
    description: str
    module_path: Optional[str] = None
    function_name: Optional[str] = None

PAGES: Dict[str, PageConfig] = {
    "Home":            PageConfig("🏠", "Project Overview & Navigation"),
    "Overview":        PageConfig("📊", "Income Statement Overview",          "src.overview.overview",          "overview"),
    "Balance Sheet":   PageConfig("💰", "Assets, Liabilities & Equity",       "src.balance_sheet.balance_sheet", "balance_sheet"),
    "Cash Flow":       PageConfig("💵", "Cash Inflows & Outflows",            "src.cash_flow.cash_flow",        "cash_flow_statement"),
    "Ratios":          PageConfig("📈", "Financial Ratios Analysis",          "src.ratios.ratios",              "ratio_analysis"),
    "Segment Analysis":PageConfig("🎯", "Segment-wise Revenue",               "src.segment_analysis.segment_analysis", "segment_analysis"),
    "Quarterly Analysis": PageConfig("📅", "Quarterly Performance & Seasonality", "src.quarterly_analysis.quarterly_analysis", "quarterly_analysis"),
    "Market Analysis": PageConfig("🌍", "Market Research",                    "src.market_analysis.market_analysis",   "market_research"),
    "Assumed Growth":  PageConfig("📉", "Growth Assumptions",                 "src.assumed_growth.assumed_growth",     "assumed_growth"),
    "Forecast":        PageConfig("🔮", "5-Year Forecast",                    "src.forecast.forecast",          "forecast"),
    "Outcome Analysis":PageConfig("✅", "Forecast vs Actual",                 "src.outcome_analysis.outcome_analysis", "outcome_analysis"),
    "Summary":         PageConfig("📝", "Executive Summary",                  "src.summary.summary",            "summary"),
    "Conclusion":      PageConfig("🎓", "Final Conclusions",                  "src.conclusion.conclusion",      "conclusion"),
    "References":      PageConfig("📚", "Data Sources & References",          "src.references.references",      "references"),
}

# Single source of truth for home-page section index and quick-nav
SECTIONS: List[Tuple[str, str, str]] = [
    ("📊", "Overview",          "Historical income data summary"),
    ("💰", "Balance Sheet",     "Assets, Liabilities and Equity"),
    ("💵", "Cash Flow",         "Cash inflows and outflows"),
    ("📈", "Ratios",            "Profitability and leverage ratios"),
    ("🎯", "Segment Analysis",  "Segment-wise revenue breakdown"),
    ("📅", "Quarterly Analysis","Quarterly revenues, seasonality & cycles"),
    ("🌍", "Market Analysis",   "Market research for industry and markets"),
    ("📉", "Assumed Growth",    "Assumed growth of markets and segments"),
    ("🔮", "Forecast",          "5-year forecast of company performance"),
    ("✅", "Outcome Analysis",  "Comparing forecast with actual data"),
    ("📝", "Summary",           "Executive summary"),
    ("🎓", "Conclusion",        "Final conclusions"),
    ("📚", "References",        "Data sources & references"),
]

# ══════════════════════════════════════════════════════════════
# 1. PAGE CONFIGURATION (must be the very first Streamlit call)
# ══════════════════════════════════════════════════════════════

st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
    layout="wide",
    initial_sidebar_state="expanded",
)

# ══════════════════════════════════════════════════════════════
# 2. GLOBAL STYLES (clean, DRY, brand-aligned)
# ══════════════════════════════════════════════════════════════

CUSTOM_CSS = f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

:root {{
    --red:    {MCD_RED};
    --yellow: {MCD_YELLOW};
    --dark:   {MCD_DARK};
    --mid:    {MCD_MID};
    --light:  {MCD_LIGHT};
    --card-shadow: 0 4px 20px rgba(0,0,0,.12);
}}

html, body, [class*="css"] {{ font-family: 'Inter', sans-serif; }}

/* ── Sidebar ── */
[data-testid="stSidebar"] {{
    background: linear-gradient(180deg, {MCD_DARK} 0%, #2d2b28 100%);
    border-right: 2px solid var(--red);
}}
[data-testid="stSidebar"] * {{ color: #fff !important; }}

/* Sidebar radio navigation */
[data-testid="stSidebar"] .stRadio label {{
    color: #ccc !important;
    padding: .4rem .85rem !important;
    border-radius: 8px;
    transition: background .2s, color .2s;
    margin: 2px 0;
    font-weight: 500;
}}
[data-testid="stSidebar"] .stRadio label:hover {{
    background: rgba(218,41,28,.22);
    color: var(--yellow) !important;
}}

/* ── Main content area ── */
.main .block-container {{ padding: 2rem 2.5rem; }}

/* Page header banner */
.page-banner {{
    background: linear-gradient(135deg, {MCD_RED} 0%, #8B0000 100%);
    padding: 1.8rem 2.5rem;
    border-radius: 14px;
    margin-bottom: 2rem;
    box-shadow: var(--card-shadow);
    color: #fff;
}}
.page-banner h1 {{ color: #fff; margin: 0; font-size: 2rem; font-weight: 700; }}
.page-banner p  {{ color: #FFD580; margin: .4rem 0 0; font-size: 1rem; }}

/* Tables (custom header) */
table {{ border-collapse: collapse; width: 100%; font-size: .88rem; }}
thead th {{
    background: var(--red) !important;
    color: #fff !important;
    padding: .7rem 1rem !important;
    text-align: center !important;
}}
tbody td {{ padding: .55rem .9rem !important; border-bottom: 1px solid #e0e0e0 !important; }}
tbody tr:hover {{ background: #FFF8E1 !important; }}

/* Primary buttons */
.stButton > button {{
    background: var(--red);
    color: #fff;
    border-radius: 8px;
    border: none;
    font-weight: 600;
    padding: .45rem 1.2rem;
    transition: background .2s, transform .15s;
}}
.stButton > button:hover {{
    background: var(--yellow);
    color: var(--dark);
    transform: translateY(-1px);
}}

/* Site footer */
.site-footer {{
    margin-top: 3rem;
    border-top: 2px solid var(--red);
    padding: 1rem 0;
    text-align: center;
    color: #888;
    font-size: .82rem;
}}
</style>
"""

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# 3. COMPATIBILITY LAYER (IPython + Plotly shim)
#    Required for legacy modules that call display(), HTML(), or fig.show()
#    Recommendation: Migrate src/ modules to native Streamlit calls for long-term maintainability.
# ══════════════════════════════════════════════════════════════

def _st_display(obj: Any) -> None:
    """Streamlit-compatible replacement for IPython.display()."""
    if hasattr(obj, "to_html"):
        st.markdown(obj.to_html(), unsafe_allow_html=True)
    elif hasattr(obj, "data") and isinstance(getattr(obj, "data", None), str):
        st.markdown(obj.data, unsafe_allow_html=True)
    elif hasattr(obj, "_repr_markdown_"):
        st.markdown(str(obj), unsafe_allow_html=True)
    else:
        st.write(obj)

def _make_html(value: str) -> Any:
    class _HTML:
        def __init__(self, v: str): self.data = v
        def to_html(self) -> str: return self.data
    return _HTML(value)

def _make_markdown(value: str) -> Any:
    class _Markdown:
        def __init__(self, v: str): self.data = v
        def to_html(self) -> str: return self.data
    return _Markdown(value)

def _build_ipy_shim() -> types.ModuleType:
    shim = types.ModuleType("IPython.display")
    shim.HTML = _make_html
    shim.Markdown = _make_markdown
    shim.display = _st_display
    return shim

def _inject_shim_into(module: types.ModuleType) -> None:
    """Inject display/HTML/Markdown shims and patch Plotly globally."""
    module.display = _st_display
    module.HTML = _make_html
    module.Markdown = _make_markdown

    # Global IPython shim
    ipy_shim = _build_ipy_shim()
    sys.modules.setdefault("IPython", types.ModuleType("IPython"))
    sys.modules["IPython.display"] = ipy_shim

    # One-time Plotly Figure.show patch
    try:
        import plotly.graph_objects as go
        if not getattr(go.Figure, "_st_patched", False):
            def _st_plotly_show(self, *args, **kwargs):
                st.plotly_chart(self, use_container_width=True)
            go.Figure.show = _st_plotly_show
            go.Figure._st_patched = True
    except ImportError:
        pass

# Install shims before any src/ imports
_ipy_shim = _build_ipy_shim()
sys.modules.setdefault("IPython", types.ModuleType("IPython"))
sys.modules["IPython.display"] = _ipy_shim

# ══════════════════════════════════════════════════════════════
# 4. SAFE DYNAMIC MODULE LOADER
# ══════════════════════════════════════════════════════════════

def load_page_module(dotted_path: str) -> Optional[types.ModuleType]:
    """
    Import module, inject compatibility shims, and return it.
    Errors are stored in session_state for display.
    """
    errors: Dict[str, str] = st.session_state.setdefault("load_errors", {})
    try:
        mod = importlib.import_module(dotted_path)
        _inject_shim_into(mod)
        return mod
    except Exception as exc:
        errors[dotted_path] = str(exc)
        return None

# ══════════════════════════════════════════════════════════════
# 5. SESSION STATE
# ══════════════════════════════════════════════════════════════

if "page" not in st.session_state:
    st.session_state.page = "Home"
if "load_errors" not in st.session_state:
    st.session_state.load_errors = {}

# ══════════════════════════════════════════════════════════════
# 6. SIDEBAR NAVIGATION (Upgraded)
# ══════════════════════════════════════════════════════════════

with st.sidebar:
    st.markdown(f"""
    <div style='text-align:center; padding:1.2rem 0 .8rem;'>
        <div style='font-size:2.8rem;'>🍔</div>
        <h2 style='color:{MCD_YELLOW}; margin:.3rem 0 0; font-size:1.15rem; font-weight:700;'>McDonald's</h2>
        <p style='color:#aaa; margin:0; font-size:.78rem;'>Financial Forecast Dashboard</p>
    </div>
    <hr style='border-color:#444; margin:.5rem 0 1rem;'>
    """, unsafe_allow_html=True)

    page_names: List[str] = list(PAGES.keys())
    current: str = st.session_state.page

    selected: str = st.radio(
        label="Navigation",
        options=page_names,
        index=page_names.index(current) if current in page_names else 0,
        format_func=lambda name: f"{PAGES[name].icon}  {name}",
        label_visibility="collapsed",
        key="nav_radio"
    )

    if selected != current:
        st.session_state.page = selected
        st.rerun()

    st.markdown(f"""
    <hr style='border-color:#444; margin:1rem 0;'>
    <div style='text-align:center; padding-bottom:1rem;'>
        <p style='color:#aaa; font-size:.75rem; margin:0;'>Prepared by <strong style='color:{MCD_YELLOW};'>Pranav J</strong></p>
        <p style='color:#666; font-size:.72rem; margin:.2rem 0 0;'>11 March 2025 · Financial Analysis</p>
    </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# 7. RENDER HELPERS
# ══════════════════════════════════════════════════════════════

def render_page_banner(title: str, subtitle: str = "") -> None:
    """Render branded page header."""
    subtitle_html = f"<p>{subtitle}</p>" if subtitle else ""
    st.markdown(f"""
    <div class="page-banner">
        <h1>{title}</h1>
        {subtitle_html}
    </div>
    """, unsafe_allow_html=True)

def render_footer() -> None:
    """Render consistent site footer."""
    st.markdown("""
    <div class="site-footer">
        McDonald's Financial Forecast Project © 2025
        &nbsp;·&nbsp; Professional Financial Analysis &amp; Forecasting
        &nbsp;·&nbsp; Prepared by Pranav J
    </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# 8. HOME PAGE (Cleaned & Modernized)
# ══════════════════════════════════════════════════════════════

def render_home() -> None:
    render_page_banner(
        "🍔 McDonald's Financial Forecast Project",
        "Comprehensive Financial Analysis & 5-Year Forecast · 2014–2023"
    )

    # Project introduction
    col_intro, col_stats = st.columns([2.1, 1])

    with col_intro:
        st.markdown(f"""
        <div style='background:#fff; border-radius:12px; padding:1.5rem 1.9rem;
                    box-shadow:0 2px 12px rgba(0,0,0,.08); border-left:5px solid {MCD_RED};
                    margin-bottom:1.5rem;'>
            <p style='margin:0 0 .65rem; color:#333; font-size:.95rem;'>
                <strong>Prepared by:</strong> Pranav J &nbsp;|&nbsp;
                <strong>Date:</strong> 11 March 2025 &nbsp;|&nbsp;
                <strong>Purpose:</strong> Financial Analysis & Forecasting
            </p>
            <p style='margin:0; color:#555; font-size:.88rem; line-height:1.65;'>
                Deep-dive into McDonald's financial performance (2014–2018) with two forecast
                scenarios through 2023: <em>Baseline Growth</em> and <em>Pandemic Disruption</em>.
                All values adjusted to 2018 USD using BLS CPI-U multipliers.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col_stats:
        st.markdown(f"""
        <div style='background:linear-gradient(135deg,{MCD_RED},#8B0000); border-radius:12px;
                    padding:1.55rem; color:#fff; box-shadow:0 4px 16px rgba(218,41,28,.3);
                    text-align:center;'>
            <div style='font-size:2.3rem;'>📁</div>
            <p style='margin:.45rem 0 0; font-size:.9rem; color:#FFD580; font-weight:600;'>14 Sections</p>
            <p style='margin:.12rem 0 0; font-size:.78rem; color:#ffcfcf;'>5 Years Historical Data</p>
            <p style='margin:.08rem 0 0; font-size:.78rem; color:#ffcfcf;'>5 Years Forecast</p>
        </div>
        """, unsafe_allow_html=True)

    # Section Index Table
    st.markdown(f"<h3 style='color:{MCD_RED}; margin:1.9rem 0 .6rem;'>📋 Section Index</h3>", unsafe_allow_html=True)

    rows_html = "".join(
        f"""<tr>
              <td style='text-align:center; width:48px;'>{icon}</td>
              <td><strong style='color:{MCD_RED};'>{name}</strong></td>
              <td style='color:#555;'>{desc}</td>
           </tr>"""
        for icon, name, desc in SECTIONS
    )

    st.markdown(f"""
    <table style='border-collapse:collapse; width:100%; background:#fff;
                  border-radius:10px; overflow:hidden; box-shadow:0 2px 12px rgba(0,0,0,.08);'>
        <thead>
            <tr style='background:{MCD_RED};'>
                <th style='color:#fff; padding:.7rem; text-align:center;'>#</th>
                <th style='color:#fff; padding:.7rem; text-align:left;'>Section</th>
                <th style='color:#fff; padding:.7rem; text-align:left;'>Description</th>
            </tr>
        </thead>
        <tbody>{rows_html}</tbody>
    </table>
    <p style='color:#888; font-size:.78rem; margin-top:.55rem;'>
        ⓘ All financial data is adjusted to 2018 USD unless stated otherwise (BLS CPI-U multipliers).
    </p>
    """, unsafe_allow_html=True)

    # Quick Navigation
    st.markdown(f"<h3 style='color:{MCD_RED}; margin:2.1rem 0 .6rem;'>⚡ Quick Navigation</h3>", unsafe_allow_html=True)

    nav_cols = st.columns(4)
    for idx, (icon, name, desc) in enumerate(SECTIONS):
        with nav_cols[idx % 4]:
            if st.button(f"{icon} {name}", key=f"quick_{name}", use_container_width=True, help=desc):
                st.session_state.page = name
                st.rerun()

# ══════════════════════════════════════════════════════════════
# 9. MAIN APPLICATION LOGIC
# ══════════════════════════════════════════════════════════════

def main() -> None:
    """Primary application controller."""
    current_page: str = st.session_state.page
    page_cfg: PageConfig = PAGES[current_page]

    if current_page == "Home":
        render_home()
    else:
        render_page_banner(f"{page_cfg.icon}  {current_page}", page_cfg.description)

        mod_path = page_cfg.module_path
        fn_name = page_cfg.function_name

        if mod_path is None:
            st.warning("No module configured for this page.")
        else:
            module = load_page_module(mod_path)
            if module is None:
                err = st.session_state["load_errors"].get(mod_path, "Unknown error")
                st.error(f"⚠️ Failed to load **{mod_path}**")
                with st.expander("Error details"):
                    st.code(err)
                st.info("Ensure the `src/` package exists and all dependencies are installed.")
            else:
                target_function = getattr(module, fn_name, None)
                if target_function is None:
                    st.error(f"Function `{fn_name}` not found in `{mod_path}`.")
                else:
                    try:
                        target_function()
                    except Exception as exc:
                        import traceback
                        st.error(f"Error rendering **{current_page}**.")
                        with st.expander("🔍 Full traceback (developers only)"):
                            st.code(traceback.format_exc())

        # Consistent back navigation
        st.divider()
        if st.button("⬅️  Return to Home", key="back_home"):
            st.session_state.page = "Home"
            st.rerun()

    render_footer()

if __name__ == "__main__":
    main()