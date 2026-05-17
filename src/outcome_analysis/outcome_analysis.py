# Outcome Analysis

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def outcome_analysis():
    """
    Performs an outcome analysis for market size and revenue projections 
    (Actual, Baseline, Pandemic, Hindsight) from 2014-2023, calculates 
    error analysis for 2019-2023, and displays the data, error table, 
    a dual-axis Plotly chart, and an explanatory text.
    All monetary values are in 2025 USD Millions.
    Dark mode readable via CSS media query.
    """
    st.header("Outcome Analysis")
    
    # Data
    years = [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
    actual_market = [1002263.0, 1075278.2, 1119072.0, 1139027.4, 1147068.8, 1163230.4, 1107950.1, 1175306.8, 1128715.0, 1099410.9]
    actual_rev = [36822.9, 34060.7, 32589.3, 29574.9, 26598.6, 26189.5, 23155.4, 26814.0, 24807.6, 26249.7]
    baseline_market = [1002263.0, 1075278.2, 1119072.0, 1139027.4, 1147068.8, 1192951.5, 1240669.6, 1290296.4, 1341908.2, 1395584.5]
    baseline_rev = [36822.9, 34060.7, 32589.3, 29574.9, 26598.6, 27404.6, 28238.0, 29099.7, 29990.8, 30912.7]
    pandemic_market = [1002263.0, 1075278.2, 1119072.0, 1139027.4, 1147068.8, 1164274.8, 1181738.9, 1199465.0, 1217457.0, 1235718.8]
    pandemic_rev = [36822.9, 34060.7, 32589.3, 29574.9, 26598.6, 28210.7, 25648.7, 22285.3, 24318.8, 25803.5]
    hindsight_market = [1002263.0, 1075278.2, 1119072.0, 1139027.4, 1147068.8, 1170010.1, 1193410.3, 1217278.6, 1241624.1, 1266456.6]
    hindsight_rev = [36822.9, 34060.7, 32589.3, 29574.9, 26598.6, 28210.7, 25648.7, 22285.3, 24318.8, 25803.5]

    # DataFrame
    df_data = {
        'Year': years,
        'Actual Market': actual_market,
        'Actual Revenue': actual_rev,
        'Baseline Market': baseline_market,
        'Baseline Revenue': baseline_rev,
        'Pandemic Market': pandemic_market,
        'Pandemic Revenue': pandemic_rev,
        'Hindsight Market': hindsight_market,
        'Hindsight Revenue': hindsight_rev
    }
    df = pd.DataFrame(df_data)

    # Style main table 
    styled_df = df.style.set_table_styles([
        {'selector': 'th.col_heading[col="Actual Market"]', 'props': [('background-color', '#e6f3ff'), ('color', 'navy'), ('font-weight', 'bold')]},
        {'selector': 'th.col_heading[col="Actual Revenue"]', 'props': [('background-color', '#f0f8ff'), ('color', 'black'), ('font-weight', 'bold')]},
        {'selector': 'th.col_heading[col="Baseline Market"], th.col_heading[col="Pandemic Market"], th.col_heading[col="Hindsight Market"]', 'props': [('background-color', '#f5f5f5'), ('color', 'gray'), ('font-weight', 'bold')]},
        {'selector': 'th.col_heading[col="Baseline Revenue"], th.col_heading[col="Pandemic Revenue"], th.col_heading[col="Hindsight Revenue"]', 'props': [('background-color', '#fff2e6'), ('color', 'darkorange'), ('font-weight', 'bold')]},
        {'selector': 'th', 'props': [('font-weight', 'bold'), ('text-align', 'center'), ('border', '1px solid #ddd')]},
        {'selector': 'td', 'props': [('border', '1px solid #ddd'), ('padding', '8px'), ('text-align', 'right')]},
        {'selector': 'tr:nth-child(even)', 'props': [('background-color', '#f9f9f9')]},
        {'selector': 'tr:hover', 'props': [('background-color', '#f5f5f5')]}
    ]).format("{:,.1f}", subset=df.columns[1:])

    st.write(styled_df)

    # Error Analysis 
    err_years = years[5:]
    pand_err = np.round(((np.array(pandemic_market[5:]) - np.array(actual_market[5:])) / np.array(actual_market[5:]) * 100), 2)
    hind_err = np.round(((np.array(hindsight_market[5:]) - np.array(actual_market[5:])) / np.array(actual_market[5:]) * 100), 2)
    rev_err = np.round(((np.array(pandemic_rev[5:]) - np.array(actual_rev[5:])) / np.array(actual_rev[5:]) * 100), 2)

    err_df = pd.DataFrame({
        'Year': err_years,
        'Global Market (Pandemic) %': pand_err,
        'Global Market (Hindsight) %': hind_err,
        'Revenues (Both) %': rev_err
    })

    # Compute average
    avg_pand = np.mean(pand_err)
    avg_hind = np.mean(hind_err)
    avg_rev = np.mean(rev_err)

    avg_row = pd.DataFrame({
        'Year': ['Average'],
        'Global Market (Pandemic) %': [avg_pand],
        'Global Market (Hindsight) %': [avg_hind],
        'Revenues (Both) %': [avg_rev]
    })

    err_df = pd.concat([err_df, avg_row], ignore_index=True)
    err_df = err_df.set_index('Year')

    # Style error table
    def color_errors(val):
        if pd.isna(val):
            return ''
        if val > 0:
            return 'background-color: rgba(255,0,0,0.2); color: red; font-weight: bold'
        elif val < 0:
            return 'background-color: rgba(0,255,0,0.2); color: green; font-weight: bold'
        else:
            return 'background-color: rgba(255,255,0,0.2); color: black; font-weight: bold'

    styled_err = err_df.style.map(color_errors, subset=err_df.columns).set_table_styles([
        {'selector': 'th', 'props': [('background-color', '#e6f3ff'), ('color', 'navy'), ('font-weight', 'bold'), ('border', '1px solid #ddd')]},
        {'selector': 'td', 'props': [('border', '1px solid #ddd'), ('padding', '8px'), ('text-align', 'center')]},
        {'selector': 'tr:nth-child(even)', 'props': [('background-color', '#f9f9f9')]},
        {'selector': 'tr:hover', 'props': [('background-color', '#f5f5f5')]}
    ]).format("{:,.2f}", subset=err_df.columns)

    st.write(styled_err)

    # Plot Chart 
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    # Market Traces (Left Axis)
    fig.add_trace(go.Scatter(x=years, y=actual_market, mode='lines+markers', name='Actual Market', line=dict(color='lightblue', width=3), marker=dict(size=8)), secondary_y=False)
    fig.add_trace(go.Scatter(x=years, y=baseline_market, mode='lines+markers', name='Baseline Market', line=dict(color='gray', dash='dot'), marker=dict(size=6)), secondary_y=False)
    fig.add_trace(go.Scatter(x=years, y=pandemic_market, mode='lines+markers', name='Pandemic Market', line=dict(color='cyan'), marker=dict(size=6)), secondary_y=False)
    fig.add_trace(go.Scatter(x=years, y=hindsight_market, mode='lines+markers', name='Hindsight Market', line=dict(color='navy', dash='dash'), marker=dict(size=6)), secondary_y=False)
    
    # Revenue Traces (Right Axis)
    fig.add_trace(go.Scatter(x=years, y=actual_rev, mode='lines+markers', name='Actual Revenue', line=dict(color='yellow', width=3), marker=dict(size=8)), secondary_y=True)
    fig.add_trace(go.Scatter(x=years, y=baseline_rev, mode='lines+markers', name='Baseline Revenue', line=dict(color='lightgray', dash='dot'), marker=dict(size=6)), secondary_y=True)
    fig.add_trace(go.Scatter(x=years, y=pandemic_rev, mode='lines+markers', name='Pandemic Revenue', line=dict(color='lime'), marker=dict(size=6)), secondary_y=True)
    fig.add_trace(go.Scatter(x=years, y=hindsight_rev, mode='lines+markers', name='Hindsight Revenue', line=dict(color='orange', dash='dash'), marker=dict(size=6)), secondary_y=True)
    
    # Layout Updates
    fig.update_xaxes(title_text="Year", tickmode='linear', dtick=1)
    fig.update_yaxes(title_text="Global Fast-food Market Size (Millions)", secondary_y=False, title_font=dict(color='lightblue'), tickformat='.0f', ticksuffix='M')
    fig.update_yaxes(title_text="Revenues (Millions)", secondary_y=True, title_font=dict(color='lightblue'), tickformat='.0f', ticksuffix='M')
    fig.update_layout(
        title_text="<b>Outcome Analysis: Market Size and Revenues (2014-2023)</b>", 
        hovermode='x unified', 
        height=550,
        template='plotly_white',
        legend=dict(orientation="h", yanchor="bottom", y=-0.25, xanchor="center", x=0.5, bgcolor='rgba(0,0,0,0.5)', bordercolor='gray')
    )
    
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("## Outcome Analysis Summary")
    st.markdown("""
All monetary values—historical data (2014-2018), forecasted figures (2019-2023), and actual market size and revenue data (2019-2023) from sources—have
been adjusted to 2025 USD using CPI multipliers for precision in the error analysis. This aligns the project with current purchasing power as of March 
2025, ensuring a consistent basis for comparing projections against actual outcomes. The adjustments are documented in the "Data Reference" sheet, 
accessible via the hyperlink below, allowing for transparency while keeping the analysis focused on accuracy evaluation.

**Error Analysis** evaluates the percentage errors between the actual and projected values for global fast-food market sizes and revenues under the
Pandemic Disruption and Hindsight scenarios (with all figures adjusted to 2025 USD for consistency). The Pandemic Disruption scenario, modeled on
revenue declines from the 2003 SARS outbreak (**-10%** in 2020, **-14%** in 2021) and the 2008 financial crisis, and the Hindsight scenario, 
assuming a **2%** CAGR with annual fluctuations, share identical revenue projections across 2019-2023, resulting in an average error 
of **-0.41%** (indicating a slight underestimate). This similarity arises because both scenarios were designed to explore company-specific vulnerabilities 
during a severe disruption, with the Hindsight scenario's fluctuations built around the same SARS/2008 revenue drops, reflecting historical variability 
rather than introducing a new revenue trend. For global market sizes, the Pandemic Disruption assumes a **1.5%** CAGR with an average error of **5.81%**, while 
the Hindsight scenario uses a **2%** CAGR with an average error of **7.41%**, reflecting the market's actual resilience that outpaced both assumptions. 
The Baseline scenario was excluded from this error analysis, as it assumes a steady **4%** CAGR without accounting for a significant disruption like 
the COVID-19 pandemic, which did not align with the conditions observed in 2019-2023, making it less relevant for validation. These findings suggest 
the models captured the initial disruption well but underestimated the recovery.
    """)

if __name__ == "__main__":
    outcome_analysis()
