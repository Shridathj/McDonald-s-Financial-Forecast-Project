# Data Source

import streamlit as st
import pandas as pd
import numpy as np

def  data_source():
    """
    Displays global fast-food market size and revenues across Nominal Data, Baseline, Pandemic Disruption, and Hindsight scenarios (2014-2023).
    All values adjusted to 2018 USD except Nominal Data. Includes CPI table and references.
    Features styled tables.
    """
    st.header("Data Source (2014-2023)")
    st.markdown("**All values in millions, adjusted to 2018 USD except Nominal Data.**")

    # Main Projections Data
    years = [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
    nominal_market = [746910.8, 802274.1, 845482.6, 878890.2, 906714.2, 936152.4, 902663.0, 1002523.3, 1039830.5, 1054525.7]
    nominal_rev = [27441.3, 25413.0, 24621.9, 22820.4, 21025.2, 21077.0, 18865.0, 22872.0, 22854.0, 25178.0]
    baseline_market = [792251.8, 849967.1, 884585.0, 900356.9, 906714.2, 942982.8, 980702.1, 1019930.2, 1060727.4, 1103156.5]
    baseline_rev = [29107.1, 26923.7, 25760.6, 23377.8, 21025.2, 21662.3, 22321.0, 23002.2, 23706.6, 24435.3]
    pandemic_market = [792251.8, 849967.1, 884585.0, 900356.9, 906714.2, 920314.9, 934119.6, 948131.4, 962353.4, 976788.7]
    pandemic_rev = [29107.1, 26923.7, 25760.6, 23377.8, 21025.2, 22299.5, 20274.3, 17615.6, 19223.1, 20396.7]
    hindsight_market = [792251.8, 849967.1, 884585.0, 900356.9, 906714.2, 924848.5, 943345.5, 962212.4, 981456.6, 1001085.7]
    hindsight_rev = [29107.1, 26923.7, 25760.6, 23377.8, 21025.2, 22299.5, 20274.3, 17615.6, 19223.1, 20396.7]

    # DataFrame for main table
    df_data = {
        'Year': years,
        'Nominal: Global Fast-food market size': nominal_market,
        'Nominal: Revenues': nominal_rev,
        'Baseline: Global Fast-food market size': baseline_market,
        'Baseline: Revenues': baseline_rev,
        'Pandemic: Global Fast-food market size': pandemic_market,
        'Pandemic: Revenues': pandemic_rev,
        'Hindsight: Global Fast-food market size': hindsight_market,
        'Hindsight: Revenues': hindsight_rev
    }
    df = pd.DataFrame(df_data)

    # Style
    dark_css = """
    <style>
    @media (prefers-color-scheme: dark) {
        table { background-color: #1e1e1e; color: #fff; }
        th { background-color: #2d2d2d; color: #fff; border-color: #444; }
        td { background-color: #1e1e1e; color: #fff; border-color: #444; }
        tr:nth-child(even) { background-color: #2d2d2d; }
        tr:hover { background-color: #333; }
    }
    </style>
    """

    # Style main table 
    styled_df = df.style.set_table_styles([
        {'selector': 'th.col_heading[col="Year"]', 'props': [('background-color', '#e6f3ff'), ('color', 'navy'), ('font-weight', 'bold')]},
        {'selector': 'th.col_heading[col="Nominal: Global Fast-food market size"], th.col_heading[col="Nominal: Revenues"]', 'props': [('background-color', '#f0f8ff'), ('color', 'black'), ('font-weight', 'bold')]},
        {'selector': 'th.col_heading[col="Baseline: Global Fast-food market size"], th.col_heading[col="Pandemic: Global Fast-food market size"], th.col_heading[col="Hindsight: Global Fast-food market size"]', 'props': [('background-color', '#f5f5f5'), ('color', 'gray'), ('font-weight', 'bold')]},
        {'selector': 'th.col_heading[col="Baseline: Revenues"], th.col_heading[col="Pandemic: Revenues"], th.col_heading[col="Hindsight: Revenues"]', 'props': [('background-color', '#fff2e6'), ('color', 'darkorange'), ('font-weight', 'bold')]},
        {'selector': 'th', 'props': [('font-weight', 'bold'), ('text-align', 'center'), ('border', '1px solid #ddd')]},
        {'selector': 'td', 'props': [('border', '1px solid #ddd'), ('padding', '8px'), ('text-align', 'right')]},
        {'selector': 'tr:nth-child(even)', 'props': [('background-color', '#f9f9f9')]},
        {'selector': 'tr:hover', 'props': [('background-color', '#f5f5f5')]}
    ]).format("{:,.1f}", subset=df.columns[1:])

    st.write(styled_df)

    # CPI Data
    cpi_years = [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2025]
    cpi_values = [236.736, 237.017, 240.007, 245.120, 251.107, 255.657, 258.811, 270.970, 292.655, 304.702, 317.671]
    multiplier_values = [1.342, 1.340, 1.324, 1.296, 1.265, 1.243, 1.227, 1.172, 1.085, 1.043, 1.000]

    df_cpi = pd.DataFrame({
        'Year': cpi_years,
        'CPI': cpi_values,
        'Multiplier': multiplier_values
    })

    # Style CPI table
    styled_cpi = df_cpi.style.set_table_styles([
        {'selector': 'th', 'props': [('background-color', '#e6f3ff'), ('color', 'navy'), ('font-weight', 'bold'), ('border', '1px solid #ddd')]},
        {'selector': 'td', 'props': [('border', '1px solid #ddd'), ('padding', '8px'), ('text-align', 'right')]},
        {'selector': 'tr:nth-child(even)', 'props': [('background-color', '#f9f9f9')]},
        {'selector': 'tr:hover', 'props': [('background-color', '#f5f5f5')]}
    ]).format("{:,.3f}", subset=['CPI', 'Multiplier'])

    st.write(styled_cpi)

    # References Markdown
    markdown_refs = """
## References

- **2019**: [SEC 10-K](https://www.sec.gov/ix?doc=/Archives/edgar/data/0000063908/000006390820000022/mcd-12312019x10k.htm)
- **2020**: [SEC 10-K](https://www.sec.gov/ix?doc=/Archives/edgar/data/0000063908/000006390821000013/mcd-20201231.htm)
- **2021**: [SEC 10-K](https://www.sec.gov/ix?doc=/Archives/edgar/data/0000063908/0000₀639₀8/₀₀₀₀₀₆₃₉₀₈/₀₀₀₀₀₆₃₉₀₈₂₂₀₀₀₀₁₁/mcd-2０２１１２３１.htm)
- **2022**: [SEC 10-K](https://www.sec.gov/ix?doc=/Archives/edgar/data/０００００６３９０８/０００００６３９０８２３００００１２/mcd-２０２２１２３１.htm)
- **2023**: [SEC 10-K](https://www.sec.gov/ix?doc=/Archives/edgar/data/０００００６３９０８/０００００６３９０８２４０００Ｏ７２/mcd-２Ｏ２３１２３１.htm)
- **Global Market Size**: [IBISWorld](https://www.ibisworld.com/global/market-size/global-fast-food-restaurants/1480/)
- **CPI**: [BLS](https://www.bls.gov/regions/mid-atlantic/data/consumerpriceindexhistorical_us_table.htm)

"""
    st.markdown(markdown_refs)

if __name__== "__main__":
    data_source()