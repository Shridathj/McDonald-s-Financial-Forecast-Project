import streamlit as st
import pandas as pd

def home():
    st.markdown("""
    <div style="text-align:center; margin-bottom:2rem;">
        <h1 style="color:#DA291C;">McDonald's Financial Forecast Project</h1>
        <p style="color:#555;">Comprehensive Financial Analysis & 5-Year Forecast • 2014–2023</p>
    </div>
    """, unsafe_allow_html=True)

    st.info("**Prepared by:** Pranav J  |  **Date:** 11 March 2025")

    st.subheader("📋 Section Index")

    data = {
        "Section": ["Overview", "Balance Sheet", "Cash Flow", "Ratios", "Segment Analysis",
                    "Quarterly Analysis", "Market Research", "Assumed Growth", "Forecast",
                    "References", "Summary", "Outcome Analysis", "Conclusion"],
        "Description": [
            "Historical income data summary", "Assets, Liabilities and Equity",
            "Cash inflows and outflows", "Profitability and leverage ratios",
            "Segment-wise revenue breakdown", "Quarterly revenues, seasonality & cycles",
            "Market research for industry and markets", "Assumed growth of markets and segments",
            "5-year forecast of company performance", "Data sources & references",
            "Executive summary", "Comparing forecast with actual data", "Final conclusions"
        ]
    }
    st.dataframe(pd.DataFrame(data), use_container_width=True, hide_index=True)

    st.markdown("---")
    st.subheader("⚡ Quick Navigation")

    cols = st.columns(4)
    sections = list(data["Section"])
    for i, sec in enumerate(sections):
        with cols[i % 4]:
            if st.button(sec, key=f"btn_{i}", use_container_width=True):
                st.session_state.page = sec
                st.rerun()