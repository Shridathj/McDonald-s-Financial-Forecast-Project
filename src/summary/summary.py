# Summary

import streamlit as st


def summary():
    """
    Replicates the 'Summary' worksheet from the McDonald's financial model.
    Uses Markdown for formatted text.

    """
    markdown_text = """

# Summary
    
Developed as a detailed financial forecasting model, this McDonald’s project projects performance from 2019 to 2023, utilizing 2014-2018 data extracted 
from 10-K and 10-Q filings, which is organized across multiple Excel worksheets. The model features two scenarios: a Baseline Growth and a 
Pandemic Disruption (which also includes Hindsight scenario), alongside assumptions drawn from historical crisis performance (e.g., SARS, 2008-2009). 
Despite challenges with online resource access due to paywalls and partial data, effective utilization of publicly available industry trends facilitated
market growth estimates (e.g., 4% CAGR). Critical business acumen informs realistic projections through analysis of strategies and market dynamics from 
financial literature. This project delivers actionable insights into resilience under varying economic conditions, serving as a key resume highlight.

Moving forward, next part of this project will extend the analysis by comparing the 2019-2023 projections with actual financial data from 
McDonald's 10-K reports and global fast-food market sizes. This comparison aims to evaluate the accuracy of the initial assumptions, examine how well 
the scenarios captured real-world impacts, completing the learning cycle of this forecast exercise.

"""
    st.markdown(markdown_text)


# Run the function
if __name__ == "__main__":
    summary()
