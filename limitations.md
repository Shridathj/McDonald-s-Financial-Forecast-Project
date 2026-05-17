# Limitations of the McDonald’s Financial Forecast Project

This document outlines the key limitations of the analysis presented in this repository. Users should consider these factors when interpreting the results.

## 1. Proprietary Data Sources

- **IBISWorld Global Fast Food Restaurants Market Data**: 
  The global fast-food market size figures used throughout the model (e.g., 2014–2023 projections under different scenarios) are derived from IBISWorld’s proprietary industry reports. Full access to IBISWorld data requires a paid subscription. The values incorporated here are based on publicly referenced summaries and historical excerpts available at the time of model development (March–October 2025). These figures may differ from the most current or detailed data available through a full IBISWorld license.

- **McDonald’s Financial Data**: All company-specific financials (income statement, balance sheet, cash flow, segment data, and ratios) are sourced exclusively from publicly available McDonald’s Corporation 10-K and 10-Q filings filed with the U.S. Securities and Exchange Commission (SEC EDGAR). These are accurate and complete as of the filing dates.

## 2. Model Assumptions and Forward-Looking Nature

- Growth assumptions (Baseline CAGR 4%, Pandemic CAGR 1.5%, Hindsight CAGR 2%) and revenue shock parameters (-10% in 2020 and -14% in 2021) are calibrated from historical crisis benchmarks (2003 SARS outbreak and 2008–2009 global financial crisis). These are simplified representations and do not capture the full complexity of the COVID-19 pandemic’s impact on consumer behavior, supply chains, or government interventions.

- The model does not explicitly incorporate post-2020 structural changes at McDonald’s, including the rapid expansion of delivery partnerships (Uber Eats, DoorDash, etc.), digital ordering platforms, and the MyMcDonald’s Rewards loyalty program. These factors contributed to stronger real-world recovery than projected in the disruption scenarios.

- All monetary values are adjusted using U.S. Bureau of Labor Statistics (BLS) CPI-U indices to constant 2018 USD (later validated to 2025 USD). While this provides consistency for trend analysis, it introduces minor distortions when comparing with nominal reported figures.

## 3. Technical and Implementation Limitations

- The Python implementation uses hardcoded data tables embedded within the source modules for full reproducibility and to avoid external dependencies. This means the model is static; updating with new quarterly results requires manual edits to the relevant Python files.

- The original comprehensive Excel model (March 2025) containing dynamic formulas, scenario manager, and linked worksheets has been archived in `archive/McD.xlsx`. The current Streamlit dashboard replicates the core analytical outputs but does not include all interactive Excel features (e.g., live what-if analysis).

- No real-time data pipeline or database connection is implemented. The project is designed as a self-contained analytical case study.

## 4. Scope and Generalizability

- This analysis focuses exclusively on McDonald’s Corporation. Results and resilience insights may not be directly transferable to other quick-service restaurant (QSR) operators without adjustment for differences in geographic exposure, menu mix, franchising model, and digital maturity.

- Outcome validation (comparison of 2019–2023 projections vs. actual results) demonstrates directional accuracy but should be viewed as illustrative rather than precise predictive validation. Average percentage errors are reported; individual year deviations can be larger.

## 5. Recommendations for Users

- For the most current market size data, consult the latest IBISWorld Global Fast Food Restaurants report directly.

- Cross-reference all projections with the most recent McDonald’s 10-K/10-Q filings and earnings releases.

- The Kaggle notebook version (https://www.kaggle.com/code/prnavjoshi/mcdonald-s-financial-forecast-project) provides an alternative interactive environment that may include additional visualizations or updates.

This project is intended as an educational and methodological demonstration of scenario-based financial stress testing rather than a definitive forecast.

**Last Updated**: May 2026
