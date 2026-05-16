# Market Research

import pandas as pd
import numpy as np
import streamlit as st

def format_percentage(val):
    if pd.notnull(val):
        return f"({abs(val) * 100:.2f}%)" if val < 0 else f"{val * 100:.2f}%"
    return "-"

def compute_metrics(df, revenue_col='McDonald\'s Total Revenue ($M)'):
    """Compute market share, RG, and avg RG. Returns (df, avg_rg)."""
    df = df.copy()  
    df['McDonald\'s Market Share'] = (df[revenue_col] / df['Global Fast Food Market ($M)']).round(6)
    rg_list = [None] + [(df[revenue_col].iloc[i] / df[revenue_col].iloc[i-1] - 1).round(6) for i in range(1, len(df))]
    df.loc[:, 'Revenue Growth (RG)'] = rg_list  
    avg_rg = df['Revenue Growth (RG)'].mean(skipna=True).round(6)
    return df, avg_rg

def market_research():
    """
    Replicates the 'Market Research' worksheet from the McDonald's financial model.
    Hardcodes adjusted global fast food market sizes and adjusted revenues (2018 USD) for full metrics table.
    Second table: Unadjusted market sizes only (nominal).
    Computes McDonald's market share (adj rev / adj market), revenue growth (YoY % change on adj rev), average RG.
    Displays tables with cycle phase hardcoded as 'Expansion'.
    No graphs produced.
    All values in $M.
    """
    markdown_text = """
<div style="text-align: center;">

# Market Research (2014-2018)

</div>
"""
    st.markdown(markdown_text)

    years = ['2014', '2015', '2016', '2017', '2018']
    cycle_phase = ['Expansion'] * 5

    # Adjusted data 
    adj_markets = [792251.8, 849967.1, 884585.0, 900356.9, 906714.2]
    adj_revs = [29107.117291413226, 26923.732015003145, 25760.62966205152, 23377.78305646214, 21025.2]

    # Adjusted DataFrame with full metrics
    adj_data_base = pd.DataFrame({
        'Year': years,
        'Global Fast Food Market ($M)': adj_markets,
        'McDonald\'s Total Revenue ($M)': adj_revs,
        'Cycle Phase': cycle_phase
    }).round(2)

    # Compute metrics for adjusted
    adj_data, avg_rg_adj = compute_metrics(adj_data_base)

    # Unadjusted markets for second table
    unadj_markets = [746910.8, 802274.1, 845482.6, 878890.2, 906714.2]

    # Build minimal unadjusted market size table
    unadj_market_df = pd.DataFrame({
        'Year': years,
        'Global Fast Food Market ($M) (Unadjusted)': unadj_markets
    }).round(2)

    # Add seasonality and volatility to adjusted table (from Quarterly)
    seasonality = [1.000, 1.000, 1.000, 1.000, 1.000]
    volatility = [round(x, 4) for x in [0.0402, 0.0450, 0.0379, 0.0511, 0.0232]]

    adj_data['Seasonality Factor'] = seasonality
    adj_data['Volatility'] = volatility

    # Reorder columns for adjusted table: Cycle Phase at end
    col_order = ['Year', 'Global Fast Food Market ($M)', 'McDonald\'s Total Revenue ($M)', 
                 'Revenue Growth (RG)', 'McDonald\'s Market Share', 'Seasonality Factor', 
                 'Volatility', 'Cycle Phase']
    adj_data = adj_data[col_order]

    # Styling function for tables
    def style_table(df, title, adjustment='', caption=''):
        fmt_dict = {
            'Global Fast Food Market ($M)': '{:,.1f}', 
            'McDonald\'s Total Revenue ($M)': '{:,.1f}', 
            'McDonald\'s Market Share': '{:.2%}', 
            'Seasonality Factor': '{:.3f}',
            'Volatility': '{:.2%}',
            'Global Fast Food Market ($M) (Unadjusted)': '{:,.1f}'
        }
        # Custom format
        if 'Revenue Growth (RG)' in df.columns:
            styled = df.style.format({**fmt_dict, 'Revenue Growth (RG)': format_percentage}).set_caption(f"{title} {adjustment}<br><small>{caption}</small>")
        else:
            styled = df.style.format(fmt_dict).set_caption(f"{title} {adjustment}<br><small>{caption}</small>")
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
    st.write((style_table(adj_data, "Market Research", "(Adjusted to 2018 USD)")))
    st.write((style_table(unadj_market_df, "Unadjusted Market Sizes", "(Nominal)", "All in $M")))

    # Footer with reference
    footer_md = f"""
<p style='font-family:Arial;font-size:12px;text-align:center;'>Adjusted to 2018 USD via BLS CPI-U multipliers. Average RG (Adjusted): {avg_rg_adj:.2%}. Cycle Phase: All Expansion.</p>
<p style='font-family:Arial;font-size:21px;'>Market Size Source: <a href="https://www.ibisworld.com/global/market-size/global-fast-food-restaurants/1480/">IBISWorld Global Fast Food Restaurants</a></p>
"""
    st.markdown(footer_md)

# Run the function
if __name__ == "__main__":
    market_research()