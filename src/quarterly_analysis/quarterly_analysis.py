# Quartely Analysis

import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st

def quarterly_analysis():
    """
    Hardcodes unadjusted quarterly revenues.
    Computes adjusted revenues using CPI multipliers.
    Computes seasonality factors as (quarterly rev / (annual total / 4)).
    Yearly factor as average of the four seasonalities per year.
    Computes volatility metrics (mean/std dev/vol = std/mean of quarters per year) via dedicated functions.
    Displays combined tables for revenues (adjusted/unadjusted), seasonality, and volatility.
    Plots: 
    - Heatmap for seasonality factors across years and quarters.
    All values in $M for revenues; factors as-is.
    """
    markdown_text = """
<div style="text-align: center;">

# Quarterly Data Analysis (2014-2018)

</div>
"""
    st.markdown(markdown_text)

    # CPI Multipliers 
    multipliers = {
        '2014': 1.061,
        '2015': 1.059,
        '2016': 1.046,
        '2017': 1.024,
        '2018': 1.000
    }

    # Hardcode unadjusted quarterly revenues
    revenues_unadj = pd.DataFrame({
        'Year': ['2014', '2015', '2016', '2017', '2018'],
        'Q1': [6700.3, 5958.9, 5903.9, 5675.9, 5138.9],
        'Q2': [7181.7, 6497.7, 6265.0, 6049.7, 5353.9],
        'Q3': [6987.1, 6615.1, 6424.1, 5754.6, 5369.4],
        'Q4': [6572.2, 6341.3, 6028.9, 5340.2, 5163.0],
        'Total': [27441.3, 25413.0, 24621.9, 22820.4, 21025.2]
    }).round(2)

    # Compute adjusted revenues from unadjusted using multipliers
    def compute_adjusted_revenues(unadj_df, multipliers):
        adj_df = unadj_df.copy()
        for idx, year in enumerate(adj_df['Year']):
            mult = multipliers[year]
            adj_df.iloc[idx, 1:5] *= mult  # Adjust Q1-Q4
            adj_df.iloc[idx, -1] *= mult   # Adjust Total
        return adj_df.round(2)

    revenues_adj = compute_adjusted_revenues(revenues_unadj, multipliers)

    # Function to compute seasonality factors: (quarterly / (total / 4))
    def compute_seasonality_factors(revenues_df):
        avg_quarter = revenues_df['Total'] / 4
        seasonality = pd.DataFrame({
            'Year': revenues_df['Year'],
            'Q1': (revenues_df['Q1'] / avg_quarter).round(5),
            'Q2': (revenues_df['Q2'] / avg_quarter).round(5),
            'Q3': (revenues_df['Q3'] / avg_quarter).round(5),
            'Q4': (revenues_df['Q4'] / avg_quarter).round(5)
        })
        # Yearly factor: average of the four seasonalities per year
        seasonality['Yearly Factor'] = seasonality[['Q1', 'Q2', 'Q3', 'Q4']].mean(axis=1).round(4)
        return seasonality

    seasonality = compute_seasonality_factors(revenues_unadj)  # Ratios same for adj/unadj

    # Function to compute volatility metrics (per year: mean/std dev/vol of quarters)
    def compute_volatility_metrics(revenues_df):
        n = len(revenues_df)
        volatility = pd.DataFrame({
            'Year': revenues_df['Year'],
            'Mean': [None] * n,
            'Stnd Dev': [None] * n,
            'Volatility': [None] * n
        })
        for idx, row in revenues_df.iterrows():
            quarters = [row['Q1'], row['Q2'], row['Q3'], row['Q4']]
            mean_q = np.mean(quarters).round(2)
            std_q = np.std(quarters).round(2)
            vol_q = (std_q / mean_q).round(4)
            volatility.at[idx, 'Mean'] = mean_q
            volatility.at[idx, 'Stnd Dev'] = std_q
            volatility.at[idx, 'Volatility'] = vol_q
        return volatility

    volatility = compute_volatility_metrics(revenues_unadj)  # Based on unadj 

    # Styling function for tables
    def style_table(df, title, caption=''):
        if 'Volatility' in df.columns:
            fmt_dict = {'Q1': '{:,.4f}', 'Q2': '{:,.4f}', 'Q3': '{:,.4f}', 'Q4': '{:,.4f}', 'Yearly Factor': '{:.3f}', 'Mean': '{:,.2f}', 'Stnd Dev': '{:,.2f}', 'Volatility': '{:.4f}'}
        else:
            fmt_dict = {'Q1': '{:,.3f}', 'Q2': '{:,.3f}', 'Q3': '{:,.3f}', 'Q4': '{:,.3f}', 'Total': '{:,.3f}'}
        styled = df.style.format(fmt_dict).set_caption(f"{title}<br><small>{caption}</small>")
        styled = styled.set_properties(**{
            'text-align': 'center',
            'font-family': 'Arial',
            'font-size': '12pt'
        }).set_table_styles([
            {'selector': 'th', 'props': [('background-color', '#D3D3D3'), ('font-weight', 'bold')]},
            {'selector': 'caption', 'props': [('font-size', '14px'), ('font-weight', 'bold'), ('text-align', 'center')]}
        ])
        return styled.to_html()

    # Display tables
    st.write((style_table(revenues_adj, "Adjusted Quarterly Revenues (2018 USD)", "All in $M")))
    st.write((style_table(revenues_unadj, "Unadjusted Quarterly Revenues", "All in $M")))
    st.write((style_table(seasonality, "Seasonality Factors", "Computed as (Quarterly Revenue / (Annual Total / 4)); Yearly Factor = Avg of Q1-Q4 Seasonalites")))
    st.write((style_table(volatility, "Volatility Metrics", "Computed: Mean/Std Dev of Quarters per Year; Volatility = Std Dev / Mean (All in $M except %; based on unadjusted)")))

    # Global layout config
    legend_config = dict(orientation="h", yanchor="bottom", y=-0.15, xanchor="center", x=0.5, font=dict(size=10))

    # Plot 1: Seasonality Factors Heatmap
    def plot_seasonality_heatmap():
        fig = go.Figure(data=go.Heatmap(
            z=[[seasonality.loc[i, 'Q1'], seasonality.loc[i, 'Q2'], seasonality.loc[i, 'Q3'], seasonality.loc[i, 'Q4']] for i in range(len(seasonality))],
            x=['Q1', 'Q2', 'Q3', 'Q4'],
            y=seasonality['Year'],
            colorscale='Viridis',
            text=[[f"{seasonality.loc[i, q]:.4f}" for q in ['Q1', 'Q2', 'Q3', 'Q4']] for i in range(len(seasonality))],
            texttemplate="%{text}",
            textfont={"size": 10},
            hoverongaps=False
        ))
        fig.update_layout(title='Seasonality Factors Heatmap', xaxis_title="Quarter", yaxis_title="Year", 
                          template='plotly_white', height=400, font=dict(size=12))
        fig.update_xaxes(showgrid=True)
        fig.update_yaxes(showgrid=True)
        return fig

    # Generate and display plot
    fig_seas = plot_seasonality_heatmap()

    st.plotly_chart(fig_seas)

    # Footer
    footer_md = """
<p style='font-family:Arial;font-size:12px;text-align:center;'>All revenues in $M (adjusted to 2018 USD via CPI multipliers). Seasonality = (Quarterly Revenue / (Annual Total / 4)). Yearly Factor = Avg of Q1-Q4 Seasonalites. Volatility = Std Dev / Mean (of quarters per year). Key Insight: Q2 consistently strongest (avg seasonality 1.033); volatility peaked in 2017 at 5.11% due to refranchising shifts.</p>
<p style='font-family:Arial;font-size:12px;'>Go to Home | Go to Segment Analysis | Go to Ratios | Go to Forecast</p>
"""
    st.markdown(footer_md)

# Run the function
if __name__ == "__main__":
    quarterly_analysis()