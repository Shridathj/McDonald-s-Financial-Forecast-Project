# McDonald’s Financial Forecast Project

**Summary & Technical Report**  
Developed by Pranav  
Excel Version: March 2025 | Python Version: October 2025  
April 2026

## Abstract

This project analyses McDonald’s historical performance (2014–2018) and generates 5-year forward projections (2019–2023) under three scenarios: **Baseline Growth**, **Pandemic Disruption**, and **Hindsight**. The model was first developed as a comprehensive Excel financial model (March 2025) and later fully replicated in Python with interactive Plotly visualisations (October 2025). Using pre-COVID data only, the exercise served as a forward-looking case study of a severe global crisis. All monetary values are CPI-adjusted to 2018 USD (later validated to 2025 USD). Post-hoc validation against actual 2019–2023 results shows the model captured the initial disruption directionally well while modestly underestimating McDonald’s resilience through delivery and digital channels.

## Executive Summary

The project demonstrates rigorous scenario-based financial modelling and post-event validation. Historical data (2014–2018) from 10-K and 10-Q filings were used to project 2019–2023 performance under three scenarios:

- **Baseline Growth**: Steady 4 % market CAGR and 2 % annual revenue growth.  
- **Pandemic Disruption**: Severe shock modelled on 2003 SARS and 2008–2009 crisis patterns (market CAGR 1.5 %, explicit revenue declines of -10 % in 2020 and -14 % in 2021).  
- **Hindsight**: Optimistic relative to the Pandemic scenario (market CAGR 2 %) but still realistic, sharing the same revenue shock assumptions.

**Outcome analysis** (Part 2) compared projections with actual 2019–2023 data (all adjusted to 2025 USD). Average errors were modest: +5.81 % (Pandemic market), +7.41 % (Hindsight market), and -0.41 % (revenues in both disruption scenarios). The project highlights the value of dynamic scenario modelling for stress-testing resilience in the quick-service restaurant sector.

## Project Overview & Data

- **Data Period**: Historical 2014–2018 (model calibration); actual outcomes 2019–2023 (validation).  
- **Sources**: McDonald’s 10-K and 10-Q filings (SEC EDGAR), IBISWorld Global Fast Food Market data, BLS CPI-U.  
- **Adjustments**: All monetary figures CPI-adjusted to 2018 USD; common stock left unadjusted (share count only). Later validated to 2025 USD.  
- **Implementation**: Complete Excel financial dashboard (transposed tables, ratio analysis, segment breakdowns, quarterly seasonality/volatility, market research, growth assumptions, forecasts, and outcome validation). Fully replicated in Python (pandas + Plotly) with interactive visualisations.

## Detailed Methodology

The model follows a structured, layered approach:

1. **Historical Financial Statements** (Income Statement, Balance Sheet, Cash Flow) – Transposed format with CPI adjustment and CAGR calculations.  
2. **Ratio Analysis** – Profitability, leverage, liquidity, cash-flow quality, return ratios, dividend sustainability, and market performance.  
3. **Segment & Quarterly Analysis** – Geographic segments (U.S., International Lead Markets, High Growth Markets, Foundational Markets & Corporate) and quarterly revenue with seasonality and volatility metrics.  
4. **Market Research & Assumed Growth** – Global fast-food market sizing, McDonald’s market share, and scenario-specific growth assumptions derived from historical crises.  
5. **Forecasting** – 5-year projections (2019–2023) of market size, revenues, and market share under all scenarios.  
6. **Outcome Analysis & Validation** – Direct comparison of projected vs. actual results with percentage error calculations.

## Outcome Analysis Results

All figures adjusted to 2025 USD.

| Metric                          | Pandemic Disruption | Hindsight     | Revenues (both scenarios) |
|---------------------------------|---------------------|---------------|---------------------------|
| Average Error (2019–2023)       | +5.81 %            | +7.41 %      | -0.41 %                  |
| Interpretation                  | Modest underestimate of market resilience | Modest underestimate of market resilience | Slight underestimate of revenue recovery |

The model captured the initial disruption directionally well but modestly underestimated the speed of McDonald’s recovery, largely due to unmodelled strength in delivery and digital channels.

## Business & Strategic Impact

- Demonstrates effective pre-crisis stress-testing of a major QSR operator against a severe global health disruption.  
- Quantifies downside risk and recovery potential through scenario planning.  
- Highlights McDonald’s greater resilience than the broader market.  
- Framework is directly transferable to other retailers or QSR chains for capital allocation and risk management.

## Repository Contents

- `Excel/` – Complete Excel financial model (March 2025)  
- `Python/` – Replicated Python implementation with interactive Plotly dashboards (October 2025)  
- `data/` – Cleaned historical and actual datasets (CPI-adjusted)  
- `reports/` – Full technical report and validation outputs  

## Technologies

- **Excel**: Advanced financial modelling, scenario manager, dynamic dashboards  
- **Python**: pandas, Plotly, NumPy, SciPy  
- Data sources: SEC EDGAR, IBISWorld, BLS CPI-U  

## References

All assumptions grounded in McDonald’s official 10-K/10-Q filings (2014–2023), IBISWorld Global Fast Food Restaurants market data, BLS CPI-U indices, and historical crisis benchmarks (2003 SARS, 2008–2009 financial crisis). Full references with direct SEC links are included in the project files.

---

**License**: Apache2.0 
**Author**: Pranav  
**Last Updated**: April 2026
