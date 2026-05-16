# Generated from: McD_Py (2).ipynb
# Converted at: 2026-04-05T14:27:53.754Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

# Home

from IPython.display import display, HTML, Markdown
import pandas as pd

def home():
    markdown_text = """
<div style="text-align: center;">

# McDonald's Financial Forecast Project

</div>
## Home

**Prepared by**: Pranav J  
**Date**: 11th of March, 2025  
**Purpose**: Financial Analysis and Forecasting  

The table below lists the sections of the McDonald's Financial Forecast Project with their descriptions.
"""
    display(Markdown(markdown_text))
    
    # Data for the Home sheet table
    data = pd.DataFrame({
        'Sl. No.': range(1, 14),
        'Section': [
            'Overview', 'Balance Sheet', 'Cash Flow Statement', 'Ratio Analysis',
            'Segment Analysis', 'Quarterly Data', 'Market Research', 'Assumed Growth',
            'Forecast', 'References', 'Summary', 'Outcome Analysis', 'Conclusion'
        ],
        'Description': [
            'Historical Income data summary.',
            'Assets, Liabilities and Equity.',
            'Cash inflows and outflows.',
            'Profitability and leverage ratios.',
            'Segment-wise revenue.',
            'Quarterly revenues, seasonality, volatility, Cycles.',
            'Market research for industry and markets.',
            'Assumed growth of markets and segments.',
            '5 year forecast of company.',
            'References.',
            'Summary.',
            'Comparing forecast with actual data.',
            'Conclusion'
        ]
    })
    
    # Style for presentation
    styled_data = data.style.set_properties(**{
        'text-align': 'left',
        'border': '1px solid black',
        'font-size': '12pt',
        'padding': '5px'
    }).set_table_styles([
        {'selector': 'th', 
         'props': [('text-align', 'center'), 
                   ('background-color', '#d3d3d3'), 
                   ('border', '1px solid black'), 
                   ('font-weight', 'bold'),
                   ('padding', '5px')]
        }
    ])
    
    # Display the table
    display(styled_data)
    
    # Footnote
    display(HTML('<p style="font-size: 10pt;"><b>Note</b>: All financial data is adjusted to 2018 USD unless otherwise stated, using BLS CPI-U multipliers.</p>'))

# Call the function to display the Home sheet
home()

# Income overview

import pandas as pd
import plotly.express as px
import numpy as np
from IPython.display import HTML, Markdown

def overview():
    """
    Replicates the 'Overview' worksheet from a financial model with transposed tables (metrics in rows, years in columns).
    Adjusts unadjusted values to 2018 USD using CPI multipliers, formats monetary values in US format,
    ratios in percentages, and highlights negatives in light red. CAGR and ratio cells are highlighted in blue.
    Adds a table for key ratios and generates an interactive bar chart.
    """
    markdown_text2 = """
<div style="text-align: center;">

# Income Sheet Overview

</div>

"""
    display(Markdown(markdown_text2))

    # Data from Overview sheet (unadjusted nominal values)
    data_unadjusted = {
        'Metric': [
            'Sales by Company-operated restaurants',
            'Revenues from franchised restaurants',
            'Total Revenues',
            'Revenue Growth',
            'Company operated expenses',
            'Franchised expenses',
            'Selling, general & administrative expenses',
            'Other expenses',
            'Total operating costs and expenses',
            'Operating Income',
            'Operating Margin',
            'Interest Expense',
            'Nonoperating Expense',
            'Income before Income Taxes',
            'Income Tax',
            'Net Income',
            'Net Margin',
            'EPS (Diluted)',
            'EPS Growth'
        ],
        '2014': [18169.3, 9272.0, 27441.3, None, 15288.0, 1697.0, 2488.0, 19.0, 19492.0, 7949.2, 0.2897, 576.0, 1.0, 7372.0, 2614.0, 4758.0, 0.1734, 4.82, None],
        '2015': [16488.3, 8924.7, 25413.0, None, 13977.0, 1647.0, 2434.0, 209.0, 18267.0, 7146.0, 0.2812, 638.0, -48.0, 6556.0, 2027.0, 4529.0, 0.1782, 4.80, None],
        '2016': [15295.0, 9326.9, 24621.9, None, 12698.8, 1718.4, 2384.5, 75.7, 16877.4, 7744.5, 0.3145, 884.8, -6.3, 6866.0, 2179.5, 4686.5, 0.1903, 5.44, None],
        '2017': [12718.9, 10101.5, 22820.4, None, 10409.6, 1790.0, 2231.3, -1163.2, 13267.7, 9552.7, 0.4186, 921.3, 57.9, 8573.5, 3381.2, 5192.3, 0.2275, 6.37, None],
        '2018': [10012.7, 11012.5, 21025.2, None, 8266.0, 1973.0, 2200.0, -237.0, 12202.0, 8823.0, 0.4196, 981.0, 26.0, 7816.0, 1892.0, 5924.0, 0.2818, 7.54, None],
        'CAGR': [None] * 19
    }

    # Initial adjusted data (to be populated from unadjusted with CPI, initialized as float)
    data_adjusted = {
        'Metric': data_unadjusted['Metric'],
        '2014': [0.0] * 19,
        '2015': [0.0] * 19,
        '2016': [0.0] * 19,
        '2017': [0.0] * 19,
        '2018': [0.0] * 19,
        'CAGR': [None] * 19
    }

    # CPI data (transposed)
    cpi_data = {
        'Metric': ['CPI', 'Multiplier'],
        '2014': [236.736, 1.0607],
        '2015': [237.017, 1.0594],
        '2016': [240.007, 1.0462],
        '2017': [245.120, 1.0244],
        '2018': [251.107, 1.0000]
    }

    # Create DataFrames
    df_adjusted = pd.DataFrame(data_adjusted)
    df_unadjusted = pd.DataFrame(data_unadjusted)
    df_cpi = pd.DataFrame(cpi_data)

    # Adjust unadjusted values to 2018 USD using CPI multipliers
    ratio_metrics = ['Revenue Growth', 'Operating Margin', 'Net Margin', 'EPS Growth']
    for metric in df_unadjusted['Metric']:
        if metric not in ratio_metrics:  # Skip ratio metrics
            for year in ['2014', '2015', '2016', '2017', '2018']:
                unadjusted_value = df_unadjusted.loc[df_unadjusted['Metric'] == metric, year].iloc[0]
                multiplier = df_cpi.loc[df_cpi['Metric'] == 'Multiplier', year].iloc[0]
                adjusted_value = unadjusted_value * multiplier if pd.notna(unadjusted_value) else None
                df_adjusted.loc[df_adjusted['Metric'] == metric, year] = adjusted_value

    # Calculate ratios and CAGR
    def calculate_cagr(start_value, end_value, periods):
        if start_value is None or end_value is None or start_value == 0 or start_value < 0 or end_value < 0:
            return None
        return (end_value / start_value) ** (0.2) - 1 
        #CAGR formula = Formula: [{(Present year/ Start year)^(1/no.of years)} - 1]*100%
        #Here, "no.of years" = 5 ; (1/ 5) = 0.2, this result is directly used in the above code.

    ratio_metrics = ['Revenue Growth', 'Operating Margin', 'Net Margin', 'EPS Growth']
    non_ratio_metrics = [m for m in df_adjusted['Metric'] if m not in ratio_metrics]

    for df in [df_adjusted, df_unadjusted]:
        total_revenues = df.loc[df['Metric'] == 'Total Revenues', '2014':'2018']
        revenue_growth = total_revenues.pct_change(axis=1)
        df.loc[df['Metric'] == 'Revenue Growth', '2015':'2018'] = revenue_growth.iloc[:, 1:].values
        
        operating_income = df.loc[df['Metric'] == 'Operating Income', '2014':'2018'].iloc[0]
        operating_margin = operating_income / total_revenues.iloc[0]
        df.loc[df['Metric'] == 'Operating Margin', '2014':'2018'] = operating_margin.values

        net_income = df.loc[df['Metric'] == 'Net Income', '2014':'2018'].iloc[0]
        net_margin = net_income / total_revenues.iloc[0]
        df.loc[df['Metric'] == 'Net Margin', '2014':'2018'] = net_margin.values

        eps_diluted = df.loc[df['Metric'] == 'EPS (Diluted)', '2014':'2018']
        eps_growth = eps_diluted.pct_change(axis=1)
        df.loc[df['Metric'] == 'EPS Growth', '2015':'2018'] = eps_growth.iloc[:, 1:].values

        for metric in non_ratio_metrics:
            start = df.loc[df['Metric'] == metric, '2014'].iloc[0]
            end = df.loc[df['Metric'] == metric, '2018'].iloc[0]
            cagr = calculate_cagr(start, end, 4)
            df.loc[df['Metric'] == metric, 'CAGR'] = cagr

    # Styling functions
    def format_currency(val):
        if pd.notnull(val):
            return f"{val:,.2f}" if val >= 0 else f"({abs(val):,.2f})"
        return "-"

    def format_percentage(val):
        if pd.notnull(val):
            return f"({abs(val) * 100:.2f}%)" if val < 0 else f"{val * 100:.2f}%"
        return "-"
    
    def apply_styles(df):
        ratio_metrics = ['Revenue Growth', 'Operating Margin', 'Net Margin', 'EPS Growth']

        metrics_headers = ['Total Revenues','Revenue Growth','Total operating costs and expenses',
           'Operating Margin','Net Income','Net Margin','EPS (Diluted)','EPS Growth']

        submetrics_headers = ['Sales by Company-operated restaurants','Revenues from franchised restaurants','Company operated expenses',
            'Franchised expenses','Selling, general & administrative expenses','Other expenses','Operating Income',
            'Interest Expense','Nonoperating Expense','Income before Income Taxes','Income Tax']

        # Apply formatting and styling
        styled_df = df.style

        # Apply currency format to monetary metrics
        styled_df = styled_df.format(format_currency, subset=pd.IndexSlice[~df['Metric'].isin(ratio_metrics), df.columns[1:-1]])
        
        # Apply percentage format to ratio metrics and CAGR
        styled_df = styled_df.format(format_percentage, subset=pd.IndexSlice[df['Metric'].isin(ratio_metrics), df.columns[1:]])
        styled_df = styled_df.format(format_percentage, subset=pd.IndexSlice[:, 'CAGR'])

        # Apply bold and centered text to headers
        styled_df = styled_df.set_properties(**{
            'font-weight': 'bold',
            'text-align': 'center',
            'background-color': '#FFB6C1'
        }, subset=pd.IndexSlice[df['Metric'].isin(metrics_headers), :])

        # Apply normal and left-aligned text to subsection headers
        styled_df = styled_df.set_properties(**{
            'font-weight': 'normal',
            'text-align': 'left',
            'background-color': '#1A1A1A' # Light Gray
        }, subset=pd.IndexSlice[df['Metric'].isin(submetrics_headers), :])

        # Apply blue highlighting to ratio rows and CAGR column
        styled_df = styled_df.set_properties(**{'background-color': '#e0f2ff'}, subset=pd.IndexSlice[df['Metric'].isin(ratio_metrics), :])
        styled_df = styled_df.set_properties(**{'background-color': '#e0f2ff'}, subset=pd.IndexSlice[:, 'CAGR'])

        # Apply red highlighting to negative values
        def highlight_negatives(val):
            return 'background-color: #FF9999;' if isinstance(val, (int, float)) and val < 0 else ''
        
        styled_df = styled_df.map(highlight_negatives, subset=df.columns[1:])
        
        # Add general table styles
        styled_df = styled_df.set_properties(**{
            'text-align': 'center',
            'border': '1px solid black',
            'font-family': 'Arial',
            'font-size': '12pt',
            'padding': '5px'
        }).set_table_styles([
            {'selector': 'th', 'props': [('text-align', 'center'), ('background-color', '#d3d3d3'), ('border', '1px solid black'), ('font-weight', 'bold'), ('padding', '5px')]},
            {'selector': 'caption', 'props': [('font-size', '16px'), ('font-weight', 'bold'), ('text-align', 'center'), ('margin-bottom', '10px')]}
        ])

        return styled_df
        
    # Apply styling to tables
    styled_adjusted = apply_styles(df_adjusted).set_caption("Adjusted Financial Metrics (2018 USD)")
    styled_unadjusted = apply_styles(df_unadjusted).set_caption("Unadjusted Financial Metrics (Nominal)")
    styled_cpi = df_cpi.style.set_caption("CPI Data")\
        .format(na_rep="-")\
        .set_properties(**{
            'text-align': 'center',
            'border': '1px solid black',
            'font-family': 'Arial',
            'font-size': '12pt',
            'padding': '5px'
        })\
        .set_table_styles([
            {'selector': 'th', 'props': [('text-align', 'center'), ('background-color', '#d3d3d3'), ('border', '1px solid black'), ('font-weight', 'bold'), ('padding', '5px')]},
            {'selector': 'caption', 'props': [('font-size', '16px'), ('font-weight', 'bold'), ('text-align', 'center'), ('margin-bottom', '10px')]}
        ])
    
    # Create Key Ratios table with correct formatting
    key_ratios = df_adjusted[df_adjusted['Metric'].isin(['Revenue Growth', 'Operating Margin', 'Net Margin', 'EPS Growth'])].copy()
    styled_key_ratios = apply_styles(key_ratios).set_caption("Key Financial Ratios (2018 USD)")

    # Generate HTML output
    html_output = f"""
    <p style='font-family:Arial;font-size:12px;text-align:center;'>All values in 2018 USD (BLS CPI-U Adjusted)</p>
    <p style='font-family:Arial;font-size:12px;text-align:center;'>In millions, except share data (10-K)</p>
    {styled_adjusted.to_html()}
    {styled_unadjusted.to_html()}
    {styled_key_ratios.to_html()}
    {styled_cpi.to_html()}
    <p style='font-family:Arial;font-size:12px;'>Refer below link for CPI Data:<br><a href='https://www.bls.gov/regions/mid-atlantic/data/consumerpriceindexhistorical_us_table.htm'>BLS CPI Data</a></p>
    """

    # Display the tables in the output
    display(HTML(html_output))

    # Plot Key Ratios (Bar Chart)
    ratios_data = df_adjusted[df_adjusted['Metric'].isin(['Revenue Growth', 'EPS Growth', 'Operating Margin', 'Net Margin'])].copy()
    ratios_data = ratios_data.melt(id_vars=['Metric'], value_vars=['2014', '2015', '2016', '2017', '2018'], var_name='Year', value_name='Value')
    ratios_data = ratios_data.dropna(subset=['Value'])
    fig = px.bar(ratios_data, x='Year', y='Value', color='Metric', barmode='group',
                 title="McDonald's Key Ratios (2014-2018, 2018 USD)",
                 labels={'Value': 'Ratio (%)', 'Year': 'Year', 'Metric': 'Ratio'},
                 text_auto='.2%',
                 color_discrete_map={
                     'Revenue Growth': '#6A0DAD',
                     'EPS Growth': '#008080',
                     'Operating Margin': '#FF6347',
                     'Net Margin': '#FFD700'
                 })
    fig.update_traces(hovertemplate='<b>%{data.name}</b><br>Year: %{x}<br>Value: %{y:.2%}<extra></extra>')
    fig.update_layout(
        template='plotly_white',
        title_font_size=16,
        xaxis_title='Year',
        yaxis_title='Ratio (%)',
        legend_title='Ratio',
        font=dict(size=12, family='Arial'),
        xaxis=dict(tickmode='array', tickvals=['2014', '2015', '2016', '2017', '2018'], ticktext=['2014', '2015', '2016', '2017', '2018']),
        yaxis=dict(range=[-0.15, 0.50], tickformat='.2%'),
        showlegend=True
    )
    fig.show()

# Run the function
if __name__ == "__main__":
    overview()

# Balance sheet

import pandas as pd
import plotly.express as px
import numpy as np
from IPython.display import HTML, Markdown

def balance_sheet():
    """
    Replicates the 'Balance Sheet' worksheet from a financial model.
    Adjusts unadjusted values to 2018 USD using CPI multipliers, formats monetary values in US format,
    ratios in percentages, and highlights negatives in light red. Ratio cells are highlighted in blue.
    Adds a table for key ratios and generates an interactive bar chart for key balance sheet metrics.
    """
    markdown_text = """
<div style="text-align: center;">

# Balance Sheet Overview

</div>

"""
    display(Markdown(markdown_text))

    # Data from Balance Sheet sheet (unadjusted nominal values) with hierarchical structure
    data_unadjusted = {
        'Metrics': [
            'ASSETS',
            'Current Assets', 
            'Cash and Equivalents',
            'Accounts and Notes Receivable',
            'Inventories',
            'Prepaid Expenses and Other Current Assets',
            'Assets Held for Sale',
            'Total Current Assets',
            'Other Assets',
            'Investments in and Advances to Affiliates',
            'Goodwill', 'Miscellaneous',
            'Total Other Assets',
            'Property and Equipment',
            'Property and Equipment, at Cost',
            'Accumulated Depreciation and Amortization',
            'Net Property and Equipment',
            'Total Assets',
            'LIABILITIES AND SHAREHOLDER\'s EQUITY',
            'Current Liabilities',
            'Accounts Payable',
            'Income Taxes', 
            'Other Taxes',
            'Accrued Interest',
            'Accrued Payroll and Other Liabilities',
            'Current Maturities',
            'Liabilities Held for Sale',
            'Total Current Liabilities',
            'Long-term Liabilities',
            'Long-term Debt',
            'Long-term Income Taxes',
            'Deferred Revenues',
            'Other Long-term Liabilities',
            'Deferred Income Taxes',
            'Total Long-term Liabilities',
            'Shareholder\'s Equity',
            'Preferred Stock',
            'Common Stock',
            'Additional Paid-in Capital',
            'Retained Earnings',
            'Accumulated Other Comprehensive Income',
            'Common Stock in Treasury',
            'Total Shareholder\'s Equity (Deficit)',
            'Total LIABILITIES AND SHAREHOLDER\'s EQUITY',
            'Key Ratios', 
            'Return on Assets (ROA)',
            'Debt to Asset Ratio (D/A)',
            'Current Ratio'
        ],
        '2014': [0.0, 0.0, 2077.9, 1213.4, 110.0, 783.2, 0.0, 4184.5, 0.0, 1004.3, 2736.3, 1744.0, 5484.6, 0.0, 39126.1, -14568.6, 24557.5, 34227.4,
                 0.0, 0.0, 860.1, 166.8, 330.0, 233.7, 1157.3, 0.0, 0.0, 2747.9, 0.0, 14935.7, 0.0, 0.0, 2065.9, 1624.5, 17001.6,
                 0.0, 0.0, 16.6, 6239.1, 43294.5, -1519.7, -35177.1, 12853.4, 34227.4, 0.0, None, None, None],
        '2015': [0.0, 0.0, 7685.5, 1298.6, 100.0, 558.6, 0.0, 9642.7, 0.0, 792.3, 2515.9, 1868.8, 5176.9, 0.0, 37692.6, -14574.8, 23117.6, 37938.7,
                 0.0, 0.0, 874.7, 154.8, 309.0, 233.1, 1378.8, 0.0, 0.0, 2950.4, 0.0, 24122.1, 0.0, 0.0, 2074.0, 1704.3, 26196.1,
                 0.0, 0.0, 16.6, 6533.4, 44594.5, -2879.8, -41176.8, 7087.9, 37938.7, 0.0, None, None, None],
        '2016': [0.0, 0.0, 1223.4, 1473.7, 58.9, 564.9, 1526.9, 4847.8, 0.0, 725.7, 2336.2, 1854.8, 4916.7, 0.0, 34443.4, -13185.8, 21257.6, 31023.9,
                 0.0, 0.0, 756.0, 267.2, 266.3, 247.5, 1159.3, 77.2, 694.8, 3468.3, 0.0, 25878.5, 0.0, 0.0, 2064.3, 1817.1, 27942.8,
                 0.0, 0.0, 16.6, 6757.9, 46222.7, -3092.9, -52108.6, -2204.3, 31023.9, 0.0, None, None, None],
        '2017': [0.0, 0.0, 2463.8, 1975.6, 58.8, 828.4, 0.0, 5326.6, 0.0, 1085.6, 2378.3, 2562.1, 6025.9, 0.0, 36626.4, -14178.1, 22448.3, 33803.7,
                 0.0, 0.0, 924.8, 265.8, 275.4, 278.4, 1146.2, 0.0, 0.0, 2890.6, 0.0, 29536.4, 2370.9, 0.0, 1154.4, 1119.4, 30690.8,
                 0.0, 0.0, 16.6, 7072.4, 48325.8, -2178.4, -56504.4, -3268.0, 33803.7, 0.0, None, None, None],
        '2018': [0.0, 0.0, 866.0, 2441.5, 51.1, 694.6, 0.0, 4053.2, 0.0, 1202.8, 2331.5, 2381.0, 5915.3, 0.0, 37193.6, -14350.9, 22842.7, 32811.2,
                 0.0, 0.0, 1207.9, 228.3, 253.7, 297.0, 986.6, 0.0, 0.0, 2973.5, 0.0, 31075.3, 2081.2, 627.8, 1096.3, 1215.5, 32171.6,
                 0.0, 0.0, 16.6, 7376.0, 50487.0, -2609.5, -61528.5, -6258.4, 32811.2, 0.0, None, None, None]
    }

    # Initial adjusted data 
    data_adjusted = {
        'Metrics': data_unadjusted['Metrics'],
        '2014': [0.0] * len(data_unadjusted['Metrics']),
        '2015': [0.0] * len(data_unadjusted['Metrics']),
        '2016': [0.0] * len(data_unadjusted['Metrics']),
        '2017': [0.0] * len(data_unadjusted['Metrics']),
        '2018': [0.0] * len(data_unadjusted['Metrics'])
    }

    # CPI data 
    cpi_data = {
        'Metric': ['CPI', 'Multiplier'],
        '2014': [236.736, 1.061],
        '2015': [237.017, 1.059],
        '2016': [240.007, 1.046],
        '2017': [245.120, 1.024],
        '2018': [251.107, 1.000]
    }

    # Create DataFrames
    df_adjusted = pd.DataFrame(data_adjusted)
    df_unadjusted = pd.DataFrame(data_unadjusted)
    df_cpi = pd.DataFrame(cpi_data)

   # Adjust unadjusted values to 2018 USD using CPI multipliers
    ratio_metrics = ['Return on Assets (ROA)', 'Debt to Asset Ratio (D/A)', 'Current Ratio']
    for metric in df_unadjusted['Metrics']:
        if metric not in ratio_metrics and metric not in ['ASSETS', 'Current Assets', 'Other Assets', 'Property and Equipment', 
                                                         'LIABILITIES AND SHAREHOLDER\'s EQUITY', 'Current Liabilities', 
                                                         'Long-term Liabilities', 'Shareholder\'s Equity', 'Key Ratios']:
            for year in ['2014', '2015', '2016', '2017', '2018']:
                unadjusted_value = df_unadjusted.loc[df_unadjusted['Metrics'] == metric, year].iloc[0]
                multiplier = df_cpi.loc[df_cpi['Metric'] == 'Multiplier', year].iloc[0]
                if metric == 'Common Stock':
                    adjusted_value = unadjusted_value  # Common Stock is unchanged because it isn't a monetary value
                else:
                    adjusted_value = unadjusted_value * multiplier if pd.notna(unadjusted_value) else 0.0
                df_adjusted.loc[df_adjusted['Metrics'] == metric, year] = adjusted_value

    # Calculations
    for df in [df_adjusted, df_unadjusted]:
        # Total Current Assets
        current_assets = df.loc[df['Metrics'].isin(['Cash and Equivalents', 'Accounts and Notes Receivable', 'Inventories', 
                                                    'Prepaid Expenses and Other Current Assets', 'Assets Held for Sale']), '2014':'2018'].sum()
        df.loc[df['Metrics'] == 'Total Current Assets', '2014':'2018'] = current_assets.values

        # Total Other Assets
        other_assets = df.loc[df['Metrics'].isin(['Investments in and Advances to Affiliates', 'Goodwill', 'Miscellaneous']), '2014':'2018'].sum()
        df.loc[df['Metrics'] == 'Total Other Assets', '2014':'2018'] = other_assets.values

        # Net Property and Equipment
        net_property = df.loc[df['Metrics'].isin(['Property and Equipment, at Cost', 'Accumulated Depreciation and Amortization']), '2014':'2018'].sum()
        df.loc[df['Metrics'] == 'Net Property and Equipment', '2014':'2018'] = net_property.values

        # Total Assets
        total_assets = df.loc[df['Metrics'].isin(['Total Current Assets', 'Total Other Assets', 'Net Property and Equipment']), '2014':'2018'].sum()
        df.loc[df['Metrics'] == 'Total Assets', '2014':'2018'] = total_assets.values

        # Total Current Liabilities
        current_liabilities = df.loc[df['Metrics'].isin(['Accounts Payable', 'Income Taxes', 'Other Taxes', 'Accrued Interest', 
                                                         'Accrued Payroll and Other Liabilities', 'Current Maturities', 
                                                         'Liabilities Held for Sale']), '2014':'2018'].sum()
        df.loc[df['Metrics'] == 'Total Current Liabilities', '2014':'2018'] = current_liabilities.values

        # Total Long-term Liabilities
        long_term_liabilities = df.loc[df['Metrics'].isin(['Long-term Debt', 'Long-term Income Taxes', 'Deferred Revenues', 
                                                           'Other Long-term Liabilities', 'Deferred Income Taxes']), '2014':'2018'].sum()
        df.loc[df['Metrics'] == 'Total Long-term Liabilities', '2014':'2018'] = long_term_liabilities.values

        # Total Shareholder's Equity
        shareholder_equity = df.loc[df['Metrics'].isin(['Preferred Stock', 'Common Stock', 'Additional Paid-in Capital', 
                                                        'Retained Earnings', 'Accumulated Other Comprehensive Income', 
                                                        'Common Stock in Treasury']), '2014':'2018'].sum()
        df.loc[df['Metrics'] == 'Total Shareholder\'s Equity (Deficit)', '2014':'2018'] = shareholder_equity.values

        # Total Liabilities and Shareholder's Equity
        total_liab_equity = df.loc[df['Metrics'].isin(['Total Current Liabilities', 'Total Long-term Liabilities', 
                                                       'Total Shareholder\'s Equity (Deficit)']), '2014':'2018'].sum()
        df.loc[df['Metrics'] == 'Total LIABILITIES AND SHAREHOLDER\'s EQUITY', '2014':'2018'] = total_liab_equity.values

        # Calculate Return on Assets (ROA)
        net_income = [5046.8, 4798.2, 4903.2, 5319.1, 5924.3]  # From Overview sheet
        total_assets = df.loc[df['Metrics'] == 'Total Assets', '2014':'2018'].iloc[0]
        roa = net_income / total_assets
        df.loc[df['Metrics'] == 'Return on Assets (ROA)', '2014':'2018'] = roa.values

        # Calculate Debt to Asset Ratio (D/A)
        long_term_debt = df.loc[df['Metrics'] == 'Long-term Debt', '2014':'2018'].iloc[0]
        other_long_term_liabilities = df.loc[df['Metrics'] == 'Other Long-term Liabilities', '2014':'2018'].iloc[0]
        total_debt = long_term_debt + other_long_term_liabilities  # Formula excludes "Deferred income taxes"
        debt_to_asset = total_debt / total_assets
        df.loc[df['Metrics'] == 'Debt to Asset Ratio (D/A)', '2014':'2018'] = debt_to_asset.values

        # Calculate Current Ratio
        total_current_assets = df.loc[df['Metrics'] == 'Total Current Assets', '2014':'2018'].iloc[0]
        total_current_liabilities = df.loc[df['Metrics'] == 'Total Current Liabilities', '2014':'2018'].iloc[0]
        current_ratio = total_current_assets / total_current_liabilities
        df.loc[df['Metrics'] == 'Current Ratio', '2014':'2018'] = current_ratio.values

    # Styling functions
    def format_currency(val):
        if pd.notnull(val) and isinstance(val, (int, float)) and val != 0:
            return f"{val:,.1f}" if val >= 0 else f"({abs(val):,.1f})"
        return ""

    def format_percentage(val):
        if pd.notnull(val):
            return f"({abs(val) * 100:.2f}%)" if val < 0 else f"{val * 100:.2f}%"
        return ""
    
    def apply_styles(df):
        ratio_metrics = ['Return on Assets (ROA)', 'Debt to Asset Ratio (D/A)', 'Current Ratio']
        Metrics_headers1 = ['ASSETS', 'LIABILITIES AND SHAREHOLDER\'s EQUITY']

        Metrics_headers2 = ['Current Assets', 'Other Assets', 'Property and Equipment',  'Current Liabilities', 
                           'Long-term Liabilities', 'Shareholder\'s Equity', 'Key Ratios']
        
        subheaders = [ 'Cash and Equivalents','Accounts and Notes Receivable','Inventories','Prepaid Expenses and Other Current Assets',
            'Assets Held for Sale','Total Current Assets','Investments in and Advances to Affiliates','Goodwill', 'Miscellaneous',
            'Total Other Assets','Property and Equipment, at Cost','Accumulated Depreciation and Amortization','Net Property and Equipment',
            'Total Assets','Accounts Payable','Income Taxes', 'Other Taxes','Accrued Interest','Accrued Payroll and Other Liabilities',
            'Current Maturities','Liabilities Held for Sale','Total Current Liabilities', 'Long-term Debt','Long-term Income Taxes',
            'Deferred Revenues','Other Long-term Liabilities','Deferred Income Taxes','Total Long-term Liabilities','Preferred Stock',
            'Common Stock','Additional Paid-in Capital','Retained Earnings','Accumulated Other Comprehensive Income','Common Stock in Treasury',
            'Total Shareholder\'s Equity (Deficit)','Total LIABILITIES AND SHAREHOLDER\'s EQUITY']
        
        # Apply formatting and styling
        styled_df = df.style

        # Apply currency format to monetary metrics
        styled_df = styled_df.format(format_currency, subset=pd.IndexSlice[~df['Metrics'].isin(ratio_metrics), df.columns[1:]])
        
        # Apply percentage format to ratio metrics
        styled_df = styled_df.format(format_percentage, subset=pd.IndexSlice[df['Metrics'].isin(ratio_metrics), df.columns[1:]])

        # Apply bold and centered text to Metrics headers
        styled_df = styled_df.set_properties(**{
            'font-weight': 'bold', 
            'text-align': 'center', 
            'background-color': '#FFB6C1'
        }, subset=pd.IndexSlice[df['Metrics'].isin(Metrics_headers1), :])

        styled_df = styled_df.set_properties(**{
            'font-weight': 'bold', 
            'text-align': 'left', 
            'background-color': '#d3d3d3'
        }, subset=pd.IndexSlice[df['Metrics'].isin(Metrics_headers2), :])

        styled_df = styled_df.set_properties(**{
            'font-weight': 'normal', 
            'text-align': 'left', 
            'background-color': '#1A1A1A'
        }, subset=pd.IndexSlice[df['Metrics'].isin(subheaders), :])

        # Apply blue highlighting to ratio rows
        styled_df = styled_df.set_properties(**{'background-color': '#e0f2ff'}, subset=pd.IndexSlice[df['Metrics'].isin(ratio_metrics), :])

        # Apply red highlighting to negative values
        def highlight_negatives(val):
            return 'background-color: #FF9999;' if isinstance(val, (int, float)) and val < 0 else ''
        
        styled_df = styled_df.map(highlight_negatives, subset=pd.IndexSlice[~df['Metrics'].isin(Metrics_headers2), df.columns[1:]])
        
        # Add general table styles
        styled_df = styled_df.set_properties(**{
            'text-align': 'left',
            'border': '1px solid black',
            'font-family': 'Arial',
            'font-size': '12pt',
            'padding': '5px'
        }, subset=pd.IndexSlice[~df['Metrics'].isin(Metrics_headers1), df.columns[1:]]).set_table_styles([
            {'selector': 'th', 'props': [('text-align', 'center'), ('background-color', '#d3d3d3'), ('border', '1px solid black'), ('font-weight', 'bold'), ('padding', '5px')]},
            {'selector': 'caption', 'props': [('font-size', '16px'), ('font-weight', 'bold'), ('text-align', 'center'), ('margin-bottom', '10px')]}
        ])

        return styled_df
        
    # Apply styling to tables
    styled_adjusted = apply_styles(df_adjusted).set_caption("Adjusted Balance Sheet Metrics (2018 USD)")
    styled_unadjusted = apply_styles(df_unadjusted).set_caption("Unadjusted Balance Sheet Metrics (Nominal)")
    styled_cpi = df_cpi.style.set_caption("CPI Data")\
        .format(na_rep="")\
        .set_properties(**{
            'text-align': 'left',
            'border': '1px solid black',
            'font-family': 'Arial',
            'font-size': '12pt',
            'padding': '5px'
        })\
        .set_table_styles([
            {'selector': 'th', 'props': [('text-align', 'center'), ('background-color', '#d3d3d3'), ('border', '1px solid black'), ('font-weight', 'bold'), ('padding', '5px')]},
            {'selector': 'caption', 'props': [('font-size', '16px'), ('font-weight', 'bold'), ('text-align', 'center'), ('margin-bottom', '10px')]}
        ])
    
    # Create Key Ratios table with formatting
    key_ratios = df_adjusted[df_adjusted['Metrics'].isin(['Key Ratios', 'Return on Assets (ROA)', 'Debt to Asset Ratio (D/A)', 'Current Ratio'])].copy()
    styled_key_ratios = apply_styles(key_ratios).set_caption("Key Balance Sheet Ratios (2018 USD)")

    # HTML output
    html_output = f"""
    <p style='font-family:Arial;font-size:12px;text-align:center;'>All values in 2018 USD (BLS CPI-U Adjusted)</p>
    <p style='font-family:Arial;font-size:12px;text-align:center;'>In millions, except share data (10-K)</p>
    {styled_adjusted.to_html()}
    <p style='font-family:Arial;font-size:12px;'>CPI Adjustment Note: Monetary values have been CPI-adjusted to reflect real purchasing power, while common stock remains unadjusted as it represents share count, not monetary value. This may cause a minor variance in the balance sheet equation due to mixed adjustment methodologies.</p>
    {styled_unadjusted.to_html()}
    {styled_key_ratios.to_html()}
    {styled_cpi.to_html()}
    <p style='font-family:Arial;font-size:12px;'>Refer below link for CPI Data:<br><a href='https://www.bls.gov/regions/mid-atlantic/data/consumerpriceindexhistorical_us_table.htm'>BLS CPI Data</a></p>
    """

    # Display the tables in the output
    display(HTML(html_output))

    # Plot Key Ratios (Bar Chart)
    ratios_data = df_adjusted[df_adjusted['Metrics'].isin(['Return on Assets (ROA)', 'Debt to Asset Ratio (D/A)', 'Current Ratio'])].copy()
    ratios_data = ratios_data.melt(id_vars=['Metrics'], value_vars=['2014', '2015', '2016', '2017', '2018'], var_name='Year', value_name='Value')
    ratios_data = ratios_data.dropna(subset=['Value'])
    fig = px.bar(ratios_data, x='Year', y='Value', color='Metrics', barmode='group',
                 title="McDonald's Key Balance Sheet Ratios (2014-2018, 2018 USD)",
                 labels={'Value': 'Ratio', 'Year': 'Year', 'Metrics': 'Ratio'},
                 text_auto='.2%',
                 color_discrete_map={
                     'Return on Assets (ROA)': '#6A0DAD',
                     'Debt to Asset Ratio (D/A)': '#008080',
                     'Current Ratio': '#FF6347'
                 })
    fig.update_traces(hovertemplate='<b>%{data.name}</b><br>Year: %{x}<br>Value: %{y:.2%}<extra></extra>')
    fig.update_layout(
        template='plotly_white',
        title_font_size=16,
        xaxis_title='Year',
        yaxis_title='Ratio',
        legend_title='Ratio',
        font=dict(size=12, family='Arial'),
        xaxis=dict(tickmode='array', tickvals=['2014', '2015', '2016', '2017', '2018'], ticktext=['2014', '2015', '2016', '2017', '2018']),
        yaxis=dict(range=[0, ratios_data['Value'].max() * 1.1], tickformat='.2%'),
        showlegend=True
    )
    fig.show()

# Run the function
if __name__ == "__main__":
    balance_sheet()

# Cash Flow Statement

import pandas as pd
import numpy as np
import plotly.express as px
from IPython.display import HTML, Markdown, display

def cash_flow_statement():
    """
    Replicates the 'CF Statement' worksheet from a financial model.
    Adjusts unadjusted values to 2018 USD using CPI multipliers, formats monetary values in US format,
    ratios in percentages, and highlights negatives in light red. Ratio cells are highlighted in blue.
    Displays Adjusted, Unadjusted, Key Ratios, and CPI tables, with an interactive bar chart for key ratios.
    """
    markdown_text = """
<div style="text-align: center;">

# Cash Flow Statement Overview

</div>
"""
    display(Markdown(markdown_text))

    # Data from CF Statement sheet (unadjusted nominal values)
    data_unadjusted = {
        'Metrics': [
            'Operating Activities',
            'Net Income',
            'Charges and Credits',
            'Depreciation and Amortization',
            'Deferred Income Taxes',
            'Share-based Compensation',
            'Net Gain on Sale of Businesses',
            'Other (Operating Activities)',
            'Changes in Working Capital',
            'Accounts Receivable',
            'Inventories, Prepaid Expenses and Other Current Assets',
            'Accounts Payable',
            'Income Taxes',
            'Other Accrued Liabilities',
            'Total Cash by Operations (OCF)',
            'Investing Activities',
            'Capital Expenditures (CapEx)',
            'Purchases of Restaurant Businesses',
            'Sales of Restaurant Businesses',
            'Proceeds from Sale (China and Hong Kong)',
            'Sales of Property',
            'Other (Investing Activities)',
            'Total Cash by Investing Activities',
            'Financing Activities',
            'Net Short-term Borrowings',
            'Long-term Financing Issuances',
            'Long-term Financing Repayments',
            'Treasury Stock Purchases',
            'Common Stock Dividends',
            'Proceeds from Stock Option Exercises',
            'Excess Tax Benefit on Share-based Compensation',
            'Other (Financing Activities)',
            'Total Cash Provided by (Used for) Financing Activities',
            'Effect of Exchange Rates on Cash',
            'Cash and Equivalents Increase',
            'Cash in Cash Balances of Business for Sale',
            'Cash and Equivalents at Beginning of Year',
            'Cash and Equivalents at End of Year',
            'Interest Paid',
            'Income Tax Paid',
            'Key Ratios',
            'Cash Flow Performance',
            'OCF / Revenue',
            'OCF - CapEx',
            'Liquidity and Solvency',
            'OCF / Total Debt',
            'OCF / Interest Paid',
            'CapEx / OCF',
            'Quality of Earnings',
            'OCF / Net Income',
            'Return Ratios',
            'OCF / Total Assets',
            'OCF / Shareholder\'s Equity',
            'Dividend and Sustainability',
            '(OCF - Dividends)/Net Income',
            'OCF / Dividends Paid',
            'Net Income / Dividends Paid',
            'Market Performance',
            'OCF / Market Cap'
        ],
        '2014': [0.0, 4757.8, 0.0, 1644.5, -90.7, 112.8, 0.0, 369.5, 0.0, 27.0,
                 -4.9, -74.7, 3.3, -14.3, 6730.3, 0.0, -2583.4, -170.5, 489.9, 0.0,
                 0.0, -40.9, -2304.9, 0.0, 510.4, 1540.6, -548.1, -3198.6, -3216.1, 235.4,
                 70.9, -12.8, -4618.3, -527.9, -720.8, 0.0, 2798.7, 2077.9, 573.2, 2388.3,
                 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        '2015': [0.0, 4529.3, 0.0, 1555.7, -1.4, 110.0, 0.0, 177.6, 0.0, -180.6,
                 44.9, -15.0, -64.4, 383.0, 6539.1, 0.0, -1813.9, -140.6, 554.2, 0.0,
                 0.0, -19.7, -1420.0, 0.0, 589.7, 10220.0, -1054.5, -6099.2, -3230.3, 317.2,
                 51.1, -58.7, 735.3, -246.8, 5607.6, 0.0, 2077.9, 7685.5, 640.8, 1985.4,
                 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        '2016': [0.0, 4686.5, 0.0, 1516.5, -538.6, 131.3, -310.7, 407.6, 0.0, -159.0,
                 28.1, 89.8, 169.7, 38.4, 6059.6, 0.0, -1821.1, -109.5, 975.6, 1526.9,
                 82.9, -109.5, -981.6, 0.0, -286.2, 3779.5, -822.9, -11171.0, -3058.2, 299.4,
                 0.0, -3.0, -11262.4, -103.7, -6288.1, -174.0, 7685.5, 1223.4, 873.5, 2387.5,
                 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        '2017': [0.0, 5192.3, 0.0, 1363.4, -36.4, 117.5, -1155.8, 1050.7, 0.0, -340.7,
                 -37.3, -59.7, -396.4, -146.4, 5551.2, 0.0, -1853.7, -77.0, 974.8, 0.0,
                 166.8, -245.9, 562.0, 0.0, -1050.3, 4727.5, -1649.4, -4685.7, -3089.2, 456.8,
                 0.0, -20.5, -5310.8, 264.0, 1066.4, 174.0, 1223.4, 2463.8, 885.2, 2786.3,
                 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        '2018': [0.0, 5924.3, 0.0, 1482.0, 102.6, 125.1, -308.8, 114.2, 0.0, -479.4,
                 -1.9, 129.4, -33.4, -87.4, 6966.7, 0.0, -2741.7, -101.7, 530.8, 0.0,
                 160.4, -302.9, -2455.1, 0.0, 95.9, 3794.5, -1759.6, -5207.7, -3255.9, 403.2,
                 0.0, -20.0, -5949.6, -159.8, -1597.8, 0.0, 2463.8, 866.0, 959.6, 1734.4,
                 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    }

    # Validate data lengths
    metrics_length = len(data_unadjusted['Metrics'])
    for year in ['2014', '2015', '2016', '2017', '2018']:
        if len(data_unadjusted[year]) != metrics_length:
            raise ValueError(f"Column {year} has length {len(data_unadjusted[year])}, expected {metrics_length}")

    # Initial adjusted data
    data_adjusted = {
        'Metrics': data_unadjusted['Metrics'],
        '2014': [0.0] * metrics_length,
        '2015': [0.0] * metrics_length,
        '2016': [0.0] * metrics_length,
        '2017': [0.0] * metrics_length,
        '2018': [0.0] * metrics_length
    }

    # CPI data
    cpi_data = {
        'Metric': ['CPI', 'Multiplier'],
        '2014': [236.736, 1.061],
        '2015': [237.017, 1.059],
        '2016': [240.007, 1.046],
        '2017': [245.120, 1.024],
        '2018': [251.107, 1.000]
    }

    # Create DataFrames
    df_adjusted_full = pd.DataFrame(data_adjusted)
    df_unadjusted_full = pd.DataFrame(data_unadjusted)
    df_cpi = pd.DataFrame(cpi_data)

    # CPI-Adjustment logic
    ignore_metrics = ['Operating Activities', 'Charges and Credits', 'Changes in Working Capital',
                      'Investing Activities', 'Financing Activities', 'Total Cash Provided by (Used for) Financing Activities',
                      'Total Cash by Operations (OCF)', 'Total Cash by Investing Activities',
                      'Cash and Equivalents Increase', 'Cash and Equivalents at End of Year',
                      'Key Ratios', 'Cash Flow Performance', 'Liquidity and Solvency', 'Quality of Earnings',
                      'Return Ratios', 'Dividend and Sustainability', 'Market Performance'] 

    for metric in df_unadjusted_full['Metrics']:
        if metric not in ignore_metrics:
            for year in ['2014', '2015', '2016', '2017', '2018']: 
                unadjusted_value = df_unadjusted_full.loc[df_unadjusted_full['Metrics'] == metric, year].iloc[0]
                multiplier = df_cpi.loc[df_cpi['Metric'] == 'Multiplier', year].iloc[0]
                adjusted_value = unadjusted_value * multiplier if pd.notna(unadjusted_value) else 0.0
                df_adjusted_full.loc[df_adjusted_full['Metrics'] == metric, year] = adjusted_value

    # Calculations (run on full dataframes)
    for df in [df_adjusted_full, df_unadjusted_full]:
        # Total Cash by Operations (OCF)
        ocf_components = df.loc[df['Metrics'].isin(['Net Income','Depreciation and Amortization', 'Deferred Income Taxes',
                                                     'Share-based Compensation', 'Net Gain on Sale of Businesses', 'Other (Operating Activities)',
                                                     'Accounts Receivable', 'Inventories, Prepaid Expenses and Other Current Assets',
                                                     'Accounts Payable', 'Income Taxes', 'Other Accrued Liabilities']), '2014':'2018'].sum()
        df.loc[df['Metrics'] == 'Total Cash by Operations (OCF)', '2014':'2018'] = ocf_components.values

        # Total Cash by Investing Activities
        investing_components = df.loc[df['Metrics'].isin(['Capital Expenditures (CapEx)', 'Purchases of Restaurant Businesses',
                                                         'Sales of Restaurant Businesses', 'Proceeds from Sale (China and Hong Kong)',
                                                         'Sales of Property', 'Other (investing Activities)']), '2014':'2018'].sum()
        df.loc[df['Metrics'] == 'Total Cash by Investing Activities', '2014':'2018'] = investing_components.values

        # Total Cash Provided by (Used for) Financing Activities
        financing_components = df.loc[df['Metrics'].isin(['Net Short-term Borrowings', 'Long-term Financing Issuances',
                                                         'Long-term Financing Repayments', 'Treasury Stock Purchases',
                                                         'Common Stock Dividends', 'Proceeds from Stock Option Exercises',
                                                         'Excess Tax Benefit on Share-based Compensation', 'Other (Financing Activities)']), '2014':'2018'].sum()
        df.loc[df['Metrics'] == 'Total Cash Provided by (Used for) Financing Activities', '2014':'2018'] = financing_components.values

        # Cash and Equivalents Increase (Net Change in Cash)
        ocf = df.loc[df['Metrics'] == 'Total Cash by Operations (OCF)', '2014':'2018'].iloc[0]
        icf = df.loc[df['Metrics'] == 'Total Cash by Investing Activities', '2014':'2018'].iloc[0]
        fcf_val = df.loc[df['Metrics'] == 'Total Cash Provided by (Used for) Financing Activities', '2014':'2018'].iloc[0]
        exchange_effect = df.loc[df['Metrics'] == 'Effect of Exchange Rates on Cash', '2014':'2018'].iloc[0]
        cash_increase = ocf + icf + fcf_val + exchange_effect
        df.loc[df['Metrics'] == 'Cash and Equivalents Increase', '2014':'2018'] = cash_increase.values

        # Cash and Equivalents at End of Year
        cash_increase = df.loc[df['Metrics'] == 'Cash and Equivalents Increase', '2014':'2018'].iloc[0]
        cash_beginning = df.loc[df['Metrics'] == 'Cash and Equivalents at Beginning of Year', '2014':'2018'].iloc[0]
        cash_balances_sale = df.loc[df['Metrics'] == 'Cash in Cash Balances of Business for Sale', '2014':'2018'].iloc[0]
        cash_end = cash_increase + cash_beginning + cash_balances_sale
        df.loc[df['Metrics'] == 'Cash and Equivalents at End of Year', '2014':'2018'] = cash_end.values

        # Data for ratios (in millions)
        total_revenue = pd.Series([29107.1, 26923.7, 25760.6, 23377.8, 21025.2], index=['2014', '2015', '2016', '2017', '2018'])
        total_debt = pd.Series([18038.7, 27741.7, 29228.2, 31427.4, 32171.6], index=['2014', '2015', '2016', '2017', '2018'])
        net_income = pd.Series([5046.8, 4798.2, 4903.2, 5319.1, 5924.3], index=['2014', '2015', '2016', '2017', '2018'])
        total_assets = pd.Series([36315.3, 40177.1, 32451.0, 34615.0, 32811.2], index=['2014', '2015', '2016', '2017', '2018'])
        share_holderseq = pd.Series([13636.4, 7505.1, -2306.5, -3346.8, -6258.4], index=['2014', '2015', '2016', '2017', '2018'])
        market_cap = pd.Series([91190.0, 108480.0, 101080.0, 137210.0, 136890.0], index=['2014', '2015', '2016', '2017', '2018'])

        # Extracted metrics
        ocf = df.loc[df['Metrics'] == 'Total Cash by Operations (OCF)', '2014':'2018'].iloc[0]
        capex = df.loc[df['Metrics'] == 'Capital Expenditures (CapEx)', '2014':'2018'].iloc[0]
        interest_paid = df.loc[df['Metrics'] == 'Interest Paid', '2014':'2018'].iloc[0]
        stock_dividends = df.loc[df['Metrics'] == 'Common Stock Dividends', '2014':'2018'].iloc[0]

        # Operating Cash Flow (OCF) Margin
        ocf_margin = ocf / total_revenue
        df.loc[df['Metrics'] == 'OCF / Revenue', '2014':'2018'] = ocf_margin.values

        # Free Cash Flow (OCF - CapEx)
        fcf = ocf + capex  # CapEx is negative, so addition accounts for subtraction
        df.loc[df['Metrics'] == 'OCF - CapEx', '2014':'2018'] = fcf.values

        # Cash Flow to Debt Ratio
        cash_flow_to_debt = ocf / total_debt
        df.loc[df['Metrics'] == 'OCF / Total Debt', '2014':'2018'] = cash_flow_to_debt.values

        # Cash Flow Coverage Ratio
        cash_flow_coverage = ocf / interest_paid
        df.loc[df['Metrics'] == 'OCF / Interest Paid', '2014':'2018'] = cash_flow_coverage.values

        # CapEx to OCF Ratio
        capex_to_ocf = capex / ocf
        df.loc[df['Metrics'] == 'CapEx / OCF', '2014':'2018'] = capex_to_ocf.values

        # Quality of Earnings Ratio (OCF / Net Income)
        quality_of_earnings = ocf / net_income
        df.loc[df['Metrics'] == 'OCF / Net Income', '2014':'2018'] = quality_of_earnings.values

        # Cash Return on Assets (CROA)
        ocf_to_totalassets = ocf / total_assets
        df.loc[df['Metrics'] == 'OCF / Total Assets', '2014':'2018'] = ocf_to_totalassets.values

        # Cash Return on Equity (CROE)
        ocf_to_shareholderseq = ocf / share_holderseq
        df.loc[df['Metrics'] == 'OCF / Shareholder\'s Equity', '2014':'2018'] = ocf_to_shareholderseq.values

        # Sustained Cash Flow Index
        ocf_div_net_income = (ocf + stock_dividends) / net_income  # Dividends are negative
        df.loc[df['Metrics'] == '(OCF - Dividends)/Net Income', '2014':'2018'] = ocf_div_net_income.values

        # Dividend Coverage Ratio (OCF / Dividends Paid)
        ocf_div = ocf / (-stock_dividends)  # Negate dividends for absolute value
        df.loc[df['Metrics'] == 'OCF / Dividends Paid', '2014':'2018'] = ocf_div.values

        # Net Income to Dividends Ratio
        net_div = net_income / (-stock_dividends)  # Negate dividends for absolute value
        df.loc[df['Metrics'] == 'Net Income / Dividends Paid', '2014':'2018'] = net_div.values

        # Cash Flow Yield
        cash_yield = ocf / market_cap
        df.loc[df['Metrics'] == 'OCF / Market Cap', '2014':'2018'] = cash_yield.values

    # Filter out Key Ratios metrics for the main tables
    main_metrics = df_unadjusted_full['Metrics'][:40].tolist() # Metrics up to 'Income Tax Paid'
    
    df_adjusted = df_adjusted_full[df_adjusted_full['Metrics'].isin(main_metrics)].copy()
    df_unadjusted = df_unadjusted_full[df_unadjusted_full['Metrics'].isin(main_metrics)].copy()

    # Create Key Ratios table from the full adjusted data
    key_ratios_metrics = df_adjusted_full['Metrics'][40:].tolist()
    key_ratios = df_adjusted_full[df_adjusted_full['Metrics'].isin(key_ratios_metrics)].copy()


    # Styling functions
    def format_currency(val):
        if pd.notnull(val) and isinstance(val, (int, float)) and val != 0:
            return f"{val:,.1f}" if val >= 0 else f"({abs(val):,.1f})"
        return ""

    def format_percentage(val):
        if pd.notnull(val):
            # Ensure proper display for non-ratio values mistakenly passed
            if abs(val) > 100: # Heuristic check for non-ratio values
                 return f"{val:,.1f}" if val >= 0 else f"({abs(val):,.1f})"
            return f"({abs(val) * 100:.2f}%)" if val < 0 else f"{val * 100:.2f}%"
        return ""

    def format_blank(val):
        if pd.notnull(val) and isinstance(val, (int, float)):
            if val == 0:
                return ""
            return f"{val:,.1f}" if val > 0 else f"({abs(val):,.1f})"
        return ""

    def apply_styles(df):
 
        metrics_monetary = ['Net Income', 'Depreciation and Amortization', 'Deferred Income Taxes', 'Share-based Compensation',
                            'Net Gain on Sale of Businesses', 'Other (Operating Activities)', 'Accounts Receivable', 'Inventories, Prepaid Expenses and Other Current Assets',
                            'Accounts Payable', 'Income Taxes', 'Other Accrued Liabilities', 'Total Cash by Operations (OCF)', 'Capital Expenditures (CapEx)',
                            'Purchases of Restaurant Businesses', 'Sales of Restaurant Businesses', 'Proceeds from Sale (China and Hong Kong)', 'Sales of Property',
                            'Other (Investing Activities)', 'Total Cash by Investing Activities', 'Net Short-term Borrowings', 'Long-term Financing Issuances', 'Long-term Financing Repayments',
                            'Treasury Stock Purchases', 'Common Stock Dividends', 'Proceeds from Stock Option Exercises', 'Excess Tax Benefit on Share-based Compensation',
                            'Other (Financing Activities)', 'Total Cash Provided by (Used for) Financing Activities', 'Effect of Exchange Rates on Cash', 'Cash and Equivalents Increase',
                            'Cash in Cash Balances of Business for Sale', 'Cash and Equivalents at Beginning of Year', 'Cash and Equivalents at End of Year', 'Interest Paid', 'Income Tax Paid']
        
        ratio_metrics = ['OCF / Revenue', 'OCF / Total Debt', 'OCF / Interest Paid', 'CapEx / OCF',
                         'OCF / Net Income', 'OCF / Total Assets', 'OCF / Shareholder\'s Equity',
                         '(OCF - Dividends)/Net Income', 'OCF / Dividends Paid', 'Net Income / Dividends Paid', 'OCF / Market Cap']

        ocf_capex = ['OCF - CapEx']
        
        section_headers = ['Operating Activities', 'Charges and Credits', 'Changes in Working Capital','Investing Activities', 'Financing Activities', 'Key Ratios']
        
        subsection_headers = ['Cash Flow Performance','Liquidity and Solvency', 'Quality of Earnings', 'Return Ratios', 
                              'Dividend and Sustainability', 'Market Performance']
        
        styled_df = df.style

        # Apply currency format to monetary metrics and OCF - CapEx
        styled_df = styled_df.format(format_currency, subset=pd.IndexSlice[df['Metrics'].isin(metrics_monetary + ocf_capex), df.columns[1:]])
        
        # Apply blank
        styled_df = styled_df.format(format_blank, subset=pd.IndexSlice[df['Metrics'].isin(section_headers + subsection_headers), df.columns[1:]])

        # Apply percentage format to ratio metrics
        styled_df = styled_df.format(format_percentage, subset=pd.IndexSlice[df['Metrics'].isin(ratio_metrics), df.columns[1:]])

        # Apply bold and centered text to section headers
        styled_df = styled_df.set_properties(**{
            'font-weight': 'bold',
            'text-align': 'center',
            'background-color': '#FFB6C1' # Light Pink
        }, subset=pd.IndexSlice[df['Metrics'].isin(section_headers), :])

        # Apply normal and right-aligned text to subsection headers
        styled_df = styled_df.set_properties(**{
            'font-weight': 'normal',
            'text-align': 'center',
            'background-color': '#d3d3d3' # Light Gray
        }, subset=pd.IndexSlice[df['Metrics'].isin(subsection_headers), :])

        styled_df = styled_df.set_properties(**{
            'font-weight': 'normal',
            'text-align': 'right',
            'background-color': '#1A1A1A' 
        }, subset=pd.IndexSlice[df['Metrics'].isin(metrics_monetary + ratio_metrics), :])
        
        # Apply light blue highlighting to ratio rows
        styled_df = styled_df.set_properties(**{'background-color': '#ADD8E6'}, subset=pd.IndexSlice[df['Metrics'].isin(ratio_metrics + ocf_capex), df.columns[1:]])

        # Apply red highlighting to negative values
        def highlight_negatives(val):
            # Only apply to numeric columns (years)
            if isinstance(val, (int, float)) and val < 0:
                # Exclude Ratio-highlighted cells (they're already blue)
                is_ratio_metric = df.loc[df.index[df[df.columns[1:]].eq(val).any(axis=1)].tolist()[0], 'Metrics'] in ratio_metrics
                if not is_ratio_metric:
                    return 'background-color: #FF9999;' # Light Red
            return ''
        
        styled_df = styled_df.map(highlight_negatives, subset=pd.IndexSlice[~df['Metrics'].isin(subsection_headers + section_headers), df.columns[1:]])

        # Add general table styles
        styled_df = styled_df.set_properties(**{
            'text-align': 'left',
            'border': '1px solid black',
            'font-family': 'Arial',
            'font-size': '12pt',
            'padding': '5px',
            'font-weight': 'normal'
        }, subset=pd.IndexSlice[:, df.columns[0]]).set_properties(**{
            'text-align': 'right',
            'border': '1px solid black',
            'font-family': 'Arial',
            'font-size': '12pt',
            'padding': '5px',
            'font-weight': 'normal'
        }, subset=pd.IndexSlice[~df['Metrics'].isin(section_headers + subsection_headers), df.columns[1:]]).set_table_styles([
            {'selector': 'th', 'props': [('text-align', 'center'), ('background-color', '#d3d3d3'), ('border', '1px solid black'), ('font-weight', 'bold'), ('padding', '5px')]},
            {'selector': 'caption', 'props': [('font-size', '16px'), ('font-weight', 'bold'), ('text-align', 'center'), ('margin-bottom', '10px')]}
        ])

        return styled_df

    # Apply styling to tables
    styled_adjusted = apply_styles(df_adjusted).set_caption("Adjusted Cash Flow Statement Metrics (2018 USD)")
    styled_unadjusted = apply_styles(df_unadjusted).set_caption("Unadjusted Cash Flow Statement Metrics (Nominal)")
    styled_key_ratios = apply_styles(key_ratios).set_caption("Key Cash Flow Ratios (2018 USD)")
    
    styled_cpi = df_cpi.style.set_caption("CPI Data")\
        .format(na_rep="")\
        .set_properties(**{
            'text-align': 'right',
            'border': '1px solid black',
            'font-family': 'Arial',
            'font-size': '12pt',
            'padding': '5px'
        })\
        .set_table_styles([
            {'selector': 'th', 'props': [('text-align', 'center'), ('background-color', '#d3d3d3'), ('border', '1px solid black'), ('font-weight', 'bold'), ('padding', '5px')]},
            {'selector': 'caption', 'props': [('font-size', '16px'), ('font-weight', 'bold'), ('text-align', 'center'), ('margin-bottom', '10px')]}
        ])

    # HTML output for tables and chart
    html_output = f"""
    <p style='font-family:Arial;font-size:12px;text-align:center;'>All values in 2018 USD (BLS CPI-U Adjusted)</p>
    <p style='font-family:Arial;font-size:12px;text-align:center;'>In millions (10-K)</p>
    {styled_adjusted.to_html()}
    <p style='font-family:Arial;font-size:12px;'>CPI Adjustment Note: Monetary values have been CPI-adjusted to reflect real purchasing power. This ensures consistency in economic analysis across years. Minor rounding differences (0.03–0.04%) may occur due to CPI multiplier precision, as noted in the Excel file, but these have negligible impact.</p>
    {styled_unadjusted.to_html()}
    {styled_key_ratios.to_html()}
    {styled_cpi.to_html()}
    <p style='font-family:Arial;font-size:12px;'>Refer below link for CPI Data:<br><a href='https://www.bls.gov/regions/mid-atlantic/data/consumerpriceindexhistorical_us_table.htm'>BLS CPI Data</a></p>
    """

    # Display the tables
    display(HTML(html_output))

# Run the function
if __name__ == "__main__":
    cash_flow_statement()

# Ratios

import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from IPython.display import HTML, Markdown, display

def ratio_analysis():
    """
    Displays key ratios sequentially (one section at a time) with respective interactive plots.
    Formats ratios as percentages, highlights negatives in light red. Section headers in light pink.
    Individual plotting functions for easy customization per section.
    Dual y-axis for sections with mixed scales (e.g., Cash Flow Performance: left % for OCF/Revenue, right $M for OCF-CapEx).
    All values adjusted to 2018 USD where applicable (BLS CPI-U Adjusted).
    All graphs standardized to line plots with markers. Legend positioned below graph.
    """
    markdown_text = """
<div style="text-align: center;">

# Ratio Analysis Overview

</div>
"""
    display(Markdown(markdown_text))

    # Data for each section 
    sections = {
        'Income Statement Ratios': {
            'df': pd.DataFrame({
                'Metrics': ['Revenue growth', 'EPS growth', 'Operating margin', 'Net margin'],
                '2014': [np.nan, np.nan, 0.2897, 0.1734],
                '2015': [-0.0750, -0.0059, 0.2812, 0.1782],
                '2016': [-0.0432, 0.1201, 0.3145, 0.1903],
                '2017': [-0.0925, 0.1459, 0.4186, 0.2275],
                '2018': [-0.1006, 0.1564, 0.4196, 0.2818]
            })
        },
        'Balance Sheet Ratios': {
            'df': pd.DataFrame({
                'Metrics': ['Return on Assets (ROA)', 'Debt to Asset ratio (D/A)', 'Current Ratio'],
                '2014': [0.1631, 0.4967, 1.5232],
                '2015': [0.1475, 0.6905, 3.2684],
                '2016': [0.1826, 0.9007, 1.3980],
                '2017': [0.1711, 0.9079, 1.8429],
                '2018': [0.1805, 0.9805, 1.3631]
            })
        },
        'Cash Flow Performance': {
            'df': pd.DataFrame({
                'Metrics': ['OCF/Revenue', 'OCF-CapEx'],
                '2014': [0.2453, 4588.9],
                '2015': [0.2572, 5003.7],
                '2016': [0.2460, 4433.5],
                '2017': [0.2432, 3786.2],
                '2018': [0.3313, 4225.0]
            })
        },
        'Liquidity and Solvency': {
            'df': pd.DataFrame({
                'Metrics': ['OCF/Total debt', 'OCF/ Interest paid', 'Capex/OCF'],
                '2014': [0.4063, 12.0525, -0.3739],
                '2015': [0.2496, 10.2041, -0.2774],
                '2016': [0.2169, 6.9371, -0.3005],
                '2017': [0.1809, 6.2711, -0.3339],
                '2018': [0.2165, 7.2600, -0.3935]
            })
        },
        'Quality of Earnings': {
            'df': pd.DataFrame({
                'Metrics': ['OCF/Net Income'],
                '2014': [1.2373],
                '2015': [1.1688],
                '2016': [1.0699],
                '2017': [0.9595],
                '2018': [1.1760]
            })
        },
        'Return Ratios': {
            'df': pd.DataFrame({
                'Metrics': ['OCF/Total assets', 'OCF/Shareholder\'s equity'],
                '2014': [0.2018, 0.5375],
                '2015': [0.1724, 0.9227],
                '2016': [0.1953, -2.7481],
                '2017': [0.1642, -1.6985],
                '2018': [0.2123, -1.1132]
            })
        },
        'Dividend and Sustainability': {
            'df': pd.DataFrame({
                'Metrics': ['(OCF-Dividends)/Net income', 'OCF/Dividends paid', 'Net income/Dividends paid'],
                '2014': [0.6613, 2.1481, 1.7362],
                '2015': [0.5914, 2.0242, 1.7318],
                '2016': [0.5299, 1.9814, 1.8520],
                '2017': [0.4256, 1.7970, 1.8728],
                '2018': [0.6264, 2.1397, 1.8196]
            })
        },
        'Market Performance': {
            'df': pd.DataFrame({
                'Metrics': ['OCF/Market cap'],
                '2014': [0.0804],
                '2015': [0.0638],
                '2016': [0.0627],
                '2017': [0.0414],
                '2018': [0.0509]
            })
        }
    }

    # Global color palette
    global_colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f']

    # Global legend config
    legend_config = dict(
        orientation="h",
        yanchor="bottom",
        y=-0.15,
        xanchor="center",
        x=0.5,
        font=dict(size=10)
    )

    # Styling function for tables 
    def style_table(df, title):
        def format_percentage(val):
            if pd.isna(val):
                return ""
            return f"{val * 100:.2f}%" if val >= 0 else f"({abs(val) * 100:.2f}%)"

        def format_currency(val):
            if pd.isna(val):
                return ""
            return f"{val:,.1f}" if val >= 0 else f"({abs(val):,.1f})"

        styled = df.style
        currency_metrics = ['OCF-CapEx']
        if 'OCF-CapEx' in df['Metrics'].values:
            styled = styled.format(format_percentage, subset=pd.IndexSlice[df['Metrics'] != 'OCF-CapEx', df.columns[1:]])
            styled = styled.format(format_currency, subset=pd.IndexSlice[df['Metrics'] == 'OCF-CapEx', df.columns[1:]])
        else:
            styled = styled.format(format_percentage, subset=pd.IndexSlice[:, df.columns[1:]])

        # Highlight negatives
        def highlight_negatives(val):
            return 'background-color: #FF9999' if isinstance(val, (int, float)) and val < 0 else ''
        styled = styled.map(highlight_negatives, subset=pd.IndexSlice[:, df.columns[1:]])

        # General styles
        styled = styled.set_properties(**{
            'text-align': 'left',
            'border': '1px solid black',
            'font-family': 'Arial',
            'font-size': '12pt',
            'padding': '5px'
        }, subset=pd.IndexSlice[:, df.columns[0]]).set_properties(**{
            'text-align': 'right',
            'border': '1px solid black',
            'font-family': 'Arial',
            'font-size': '12pt',
            'padding': '5px'
        }, subset=pd.IndexSlice[:, df.columns[1:]]).set_table_styles([
            {'selector': 'th', 'props': [('text-align', 'center'), ('background-color', '#D3D3D3'), ('border', '1px solid black'), ('font-weight', 'bold'), ('padding', '5px')]},
            {'selector': 'caption', 'props': [('font-size', '14px'), ('font-weight', 'bold'), ('text-align', 'center'), ('margin-bottom', '10px')]}
        ]).set_caption(title)

        return styled.to_html()

    # Plotting functions 
    def plot_income_statement(df):
        """Line plot for Income Statement ratios (single y-axis, % scale)."""
        years = df.columns[1:].tolist()
        fig = go.Figure()
        for i, metric in enumerate(df['Metrics']):
            values = df.loc[df['Metrics'] == metric, years].values[0]
            y_values = [v * 100 if not pd.isna(v) else np.nan for v in values]
            fig.add_trace(go.Scatter(x=years, y=y_values, mode='lines+markers', name=metric, 
                                     line=dict(width=2, color=global_colors[i % len(global_colors)]), 
                                     marker=dict(size=6)))
        fig.update_layout(title="Income Statement Ratios", xaxis_title="Year", yaxis_title="Value (%)", 
                          template='plotly_white', height=400, showlegend=True, font=dict(size=12),
                          legend=legend_config, hovermode='x unified')
        fig.update_xaxes(showgrid=True)
        fig.update_yaxes(tickformat=",.1f")
        return fig.to_html(full_html=False, include_plotlyjs='cdn')

    def plot_balance_sheet(df):
        """Line plot for Balance Sheet ratios (single y-axis)."""
        years = df.columns[1:].tolist()
        fig = go.Figure()
        for i, metric in enumerate(df['Metrics']):
            values = df.loc[df['Metrics'] == metric, years].values[0]
            y_values = [v * 100 if not pd.isna(v) else np.nan for v in values]
            fig.add_trace(go.Scatter(x=years, y=y_values, mode='lines+markers', name=metric, 
                                     line=dict(width=2, color=global_colors[i % len(global_colors)]), 
                                     marker=dict(size=6)))
        fig.update_layout(title="Balance Sheet Ratios", xaxis_title="Year", yaxis_title="Value (%)", 
                          template='plotly_white', height=400, showlegend=True, font=dict(size=12),
                          legend=legend_config, hovermode='x unified')
        fig.update_xaxes(showgrid=True)
        fig.update_yaxes(tickformat=",.1f")
        return fig.to_html(full_html=False, include_plotlyjs='cdn')

    def plot_cash_flow_performance(df):
        """Line plot with dual y-axis: left % for OCF/Revenue, right $M for OCF-CapEx."""
        years = df.columns[1:].tolist()
        fig = make_subplots(specs=[[{"secondary_y": True}]])
        # OCF/Revenue (%)
        metric_left = 'OCF/Revenue'
        values_left = df.loc[df['Metrics'] == metric_left, years].values[0]
        y_left = [v * 100 if not pd.isna(v) else np.nan for v in values_left]
        fig.add_trace(go.Scatter(x=years, y=y_left, mode='lines+markers', name=metric_left, 
                                 line=dict(width=2, color=global_colors[0]), yaxis='y',
                                 marker=dict(size=6),
                                 hovertemplate='<b>OCF/Revenue</b><br>Year: %{x}<br>Value: %{y:.2f}%<extra></extra>'),
                      secondary_y=False)
        # OCF-CapEx ($M)
        metric_right = 'OCF-CapEx'
        values_right = df.loc[df['Metrics'] == metric_right, years].values[0]
        fig.add_trace(go.Scatter(x=years, y=values_right, mode='lines+markers', name=metric_right, 
                                 line=dict(width=2, color=global_colors[1]), yaxis='y2',
                                 marker=dict(size=6),
                                 hovertemplate='<b>OCF-CapEx</b><br>Year: %{x}<br>Value: $%{y:,.0f}M<extra></extra>'),
                      secondary_y=True)
        fig.update_yaxes(title_text="OCF/Revenue (%)", secondary_y=False, tickformat=",.1f")
        fig.update_yaxes(title_text="OCF-CapEx ($M)", secondary_y=True, tickformat=",.0f", side="right", range=[2000, 5000], dtick=1000)
        fig.update_layout(title="Cash Flow Performance", xaxis_title="Year", template='plotly_white', height=400, 
                          showlegend=True, font=dict(size=12), legend=legend_config, hovermode='x unified')
        fig.update_xaxes(showgrid=True)
        return fig.to_html(full_html=False, include_plotlyjs='cdn')

    def plot_liquidity_solvency(df):
        """Line plot with dual y-axis: explicit traces per metric (left % for debt/capex, right raw x for interest coverage)."""
        years = df.columns[1:].tolist()
        fig = make_subplots(specs=[[{"secondary_y": True}]])
    
        # OCF/Total debt
        debt_values = df.loc[df['Metrics'] == 'OCF/Total debt', years].values[0]
        y_debt = [v * 100 if not pd.isna(v) else np.nan for v in debt_values]
        fig.add_trace(go.Scatter(x=years, y=y_debt, mode='lines+markers', name='OCF/Total debt', 
                                 line=dict(width=2, color=global_colors[0]), 
                                 marker=dict(size=6), yaxis='y',
                                 hovertemplate='<b>OCF/Total debt</b><br>Year: %{x}<br>Value: %{y:.2f}%<extra></extra>'),
                      secondary_y=False)
    
        # OCF/ Interest paid
        metric_right = "OCF/ Interest paid"
        values_right = df.loc[df['Metrics'] == metric_right, years].values[0]
        y_right = [v * 100 if not pd.isna(v) else np.nan for v in values_right]
        fig.add_trace(go.Scatter(x=years, y=y_right, mode='lines+markers', name=metric_right, 
                                 line=dict(width=2, color=global_colors[1]), yaxis='y2',
                                 marker=dict(size=6),
                                 hovertemplate=f'<b>{metric_right}</b><br>Year: %{{x}}<br>Value: %{{y:.2f}}%<extra></extra>'),
                      secondary_y=True)
    
    # Capex/OCF
        capex_values = df.loc[df['Metrics'] == 'Capex/OCF', years].values[0]
        y_capex = [v * 100 if not pd.isna(v) else np.nan for v in capex_values]
        fig.add_trace(go.Scatter(x=years, y=y_capex, mode='lines+markers', name='Capex/OCF', 
                                 line=dict(width=2, color=global_colors[2]), 
                                 marker=dict(size=6), yaxis='y',
                                 hovertemplate='<b>Capex/OCF</b><br>Year: %{x}<br>Value: %{y:.2f}%<extra></extra>'),
                      secondary_y=False)
    
        fig.update_yaxes(title_text="Ratios (%)", secondary_y=False, tickformat=",.1f")
        fig.update_yaxes(title_text="Interest Coverage (%)", secondary_y=True, tickformat=",.1f", side="right", range=[500, 1500], dtick=200)
        fig.update_layout(title="Liquidity and Solvency", xaxis_title="Year", template='plotly_white', height=400, 
                          showlegend=True, font=dict(size=12), legend=legend_config, hovermode='x unified')
        fig.update_xaxes(showgrid=True)
        return fig.to_html(full_html=False, include_plotlyjs='cdn')

    def plot_quality_earnings(df):
        """Simple line plot for OCF/Net Income (%)."""
        years = df.columns[1:].tolist()
        metric = 'OCF/Net Income'
        values = df.loc[df['Metrics'] == metric, years].values[0]
        y_values = [v * 100 if not pd.isna(v) else np.nan for v in values]
        fig = go.Figure(go.Scatter(x=years, y=y_values, mode='lines+markers', name=metric, 
                                   line=dict(width=2, color=global_colors[0]),
                                   marker=dict(size=6),
                                   hovertemplate=f'<b>{metric}</b><br>Year: %{{x}}<br>Value: %{{y:.2f}}%<extra></extra>'))
        fig.update_layout(title="Quality of Earnings", xaxis_title="Year", yaxis_title="Value (%)", 
                          template='plotly_white', height=400, showlegend=True, font=dict(size=12),
                          legend=legend_config, hovermode='x unified')
        fig.update_xaxes(showgrid=True)
        fig.update_yaxes(tickformat=",.1f")
        return fig.to_html(full_html=False, include_plotlyjs='cdn')

    def plot_return_ratios(df):
        """Line plot with dual y-axis: left OCF/Total assets (%), right OCF/Shareholder's equity (%)."""
        years = df.columns[1:].tolist()
        fig = make_subplots(specs=[[{"secondary_y": True}]])
        # Left: OCF/Total assets (%)
        metric_left = 'OCF/Total assets'
        values_left = df.loc[df['Metrics'] == metric_left, years].values[0]
        y_left = [v * 100 if not pd.isna(v) else np.nan for v in values_left]
        fig.add_trace(go.Scatter(x=years, y=y_left, mode='lines+markers', name=metric_left, 
                                 line=dict(width=2, color=global_colors[0]), yaxis='y',
                                 marker=dict(size=6),
                                 hovertemplate=f'<b>{metric_left}</b><br>Year: %{{x}}<br>Value: %{{y:.2f}}%<extra></extra>'),
                      secondary_y=False)
        # Right: OCF/Shareholder's equity 
        metric_right = "OCF/Shareholder's equity"
        values_right = df.loc[df['Metrics'] == metric_right, years].values[0]
        y_right = [v * 100 if not pd.isna(v) else np.nan for v in values_right]
        fig.add_trace(go.Scatter(x=years, y=y_right, mode='lines+markers', name=metric_right, 
                                 line=dict(width=2, color=global_colors[1]), yaxis='y2',
                                 marker=dict(size=6),
                                 hovertemplate=f'<b>{metric_right}</b><br>Year: %{{x}}<br>Value: %{{y:.2f}}%<extra></extra>'),
                      secondary_y=True)
        fig.update_yaxes(title_text="OCF/Total assets (%)", secondary_y=False, tickformat=",.1f")
        fig.update_yaxes(title_text="OCF/Shareholder's equity (%)", secondary_y=True, side="right", tickformat=",.1f", range=[-300, 100])
        fig.update_layout(title="Return Ratios", xaxis_title="Year", template='plotly_white', height=400, 
                          showlegend=True, font=dict(size=12), legend=legend_config, hovermode='x unified')
        fig.update_xaxes(showgrid=True)
        return fig.to_html(full_html=False, include_plotlyjs='cdn')

    def plot_dividend_sustainability(df):
        """Line plot with dual y-axis: explicit traces (left % for OCF-Div/NI, right raw x for coverages)."""
        years = df.columns[1:].tolist()
        fig = make_subplots(specs=[[{"secondary_y": True}]])
    
        # (OCF-Dividends)/Net income
        retain_values = df.loc[df['Metrics'] == '(OCF-Dividends)/Net income', years].values[0]
        y_retain = [v * 100 if not pd.isna(v) else np.nan for v in retain_values]
        fig.add_trace(go.Scatter(x=years, y=y_retain, mode='lines+markers', name='(OCF-Dividends)/Net income', 
                                 line=dict(width=2, color=global_colors[0]), 
                                 marker=dict(size=6), yaxis='y',
                                 hovertemplate='<b>(OCF-Dividends)/Net income</b><br>Year: %{x}<br>Value: %{y:.2f}%<extra></extra>'),
                      secondary_y=False)
    
        # OCF/Dividends paid
        metric_right = "OCF/Dividends paid"
        values_right = df.loc[df['Metrics'] == metric_right, years].values[0]
        y_right = [v * 100 if not pd.isna(v) else np.nan for v in values_right]
        fig.add_trace(go.Scatter(x=years, y=y_right, mode='lines+markers', name=metric_right, 
                                 line=dict(width=2, color=global_colors[1]), yaxis='y2',
                                 marker=dict(size=6),
                                 hovertemplate=f'<b>{metric_right}</b><br>Year: %{{x}}<br>Value: %{{y:.2f}}%<extra></extra>'),
                      secondary_y=True)
        
        # Net income/Dividends 
        metric_right = "Net income/Dividends paid"
        values_right = df.loc[df['Metrics'] == metric_right, years].values[0]
        y_right = [v * 100 if not pd.isna(v) else np.nan for v in values_right]
        fig.add_trace(go.Scatter(x=years, y=y_right, mode='lines+markers', name=metric_right, 
                                 line=dict(width=2, color=global_colors[1]), yaxis='y2',
                                 marker=dict(size=6),
                                 hovertemplate=f'<b>{metric_right}</b><br>Year: %{{x}}<br>Value: %{{y:.2f}}%<extra></extra>'),
                      secondary_y=True)
        
        fig.update_yaxes(title_text="(OCF-Dividends)/Net income (%)", secondary_y=False, tickformat=",.1f")
        fig.update_yaxes(title_text="Coverage Ratios (x)", secondary_y=True, side="right", tickformat=",.1f")
        fig.update_layout(title="Dividend and Sustainability", xaxis_title="Year", template='plotly_white', height=400, 
                          showlegend=True, font=dict(size=12), legend=legend_config, hovermode='x unified')
        fig.update_xaxes(showgrid=True)
        return fig.to_html(full_html=False, include_plotlyjs='cdn')

    def plot_market_performance(df):
        """Simple line plot for OCF/Market cap (%)."""
        years = df.columns[1:].tolist()
        metric = 'OCF/Market cap'
        values = df.loc[df['Metrics'] == metric, years].values[0]
        y_values = [v * 100 if not pd.isna(v) else np.nan for v in values]
        fig = go.Figure(go.Scatter(x=years, y=y_values, mode='lines+markers', name=metric, 
                                   line=dict(width=2, color=global_colors[0]),
                                   marker=dict(size=6),
                                   hovertemplate=f'<b>{metric}</b><br>Year: %{{x}}<br>Value: %{{y:.2f}}%<extra></extra>'))
        fig.update_layout(title="Market Performance", xaxis_title="Year", yaxis_title="Value (%)", 
                          template='plotly_white', height=400, showlegend=True, font=dict(size=12),
                          legend=legend_config, hovermode='x unified')
        fig.update_xaxes(showgrid=True)
        fig.update_yaxes(tickformat=",.1f")
        return fig.to_html(full_html=False, include_plotlyjs='cdn')

    # Generate output
    html_parts = []
    for section_title, data in sections.items():
        df = data['df']
        table_html = style_table(df, section_title)
        if section_title == 'Income Statement Ratios':
            plot_html = plot_income_statement(df)
        elif section_title == 'Balance Sheet Ratios':
            plot_html = plot_balance_sheet(df)
        elif section_title == 'Cash Flow Performance':
            plot_html = plot_cash_flow_performance(df)
        elif section_title == 'Liquidity and Solvency':
            plot_html = plot_liquidity_solvency(df)
        elif section_title == 'Quality of Earnings':
            plot_html = plot_quality_earnings(df)
        elif section_title == 'Return Ratios':
            plot_html = plot_return_ratios(df)
        elif section_title == 'Dividend and Sustainability':
            plot_html = plot_dividend_sustainability(df)
        elif section_title == 'Market Performance':
            plot_html = plot_market_performance(df)
        else:
            plot_html = ""
        html_parts.append(f"""
        <div style="margin-bottom: 40px;">
            {table_html}
            <div style="margin-top: 20px;">
                {plot_html}
            </div>
        </div>
        """)

    # Full HTML
    html_output = f"""
    <p style='font-family:Arial;font-size:12px;text-align:center;'>All ratios in percentages unless noted. Adjusted values in 2018 USD (BLS CPI-U Adjusted).</p>
    {''.join(html_parts)}
    """
    
    display(HTML(html_output))

# Run the function
if __name__ == "__main__":
    ratio_analysis()

# Segment Analysis

import pandas as pd
import numpy as np
import plotly.graph_objects as go
from IPython.display import HTML, Markdown, display

def segment_analysis():
    """
    Hardcodes unadjusted data, computes adjusted using CPI multipliers.
    Displays one combined adjusted table, then one combined unadjusted table.
    Highlights 'Total' rows in light green in tables.
    Plots line graphs for each section.
    All values in $M.
    """
    markdown_text = """
<div style="text-align: center;">

# Segment Analysis Overview

</div>
"""
    display(Markdown(markdown_text))

    # CPI Multipliers 
    multipliers = {
        '2014': 1.061,
        '2015': 1.059,
        '2016': 1.046,
        '2017': 1.024,
        '2018': 1.000
    }

    # Unadjusted data
    revenues_unadj = pd.DataFrame({
        'Section': ['Revenues by Segment'] * 5,
        'Segment': ['U.S', 'International Lead Markets', 'High Growth Markets', 'Foundational Markets & Corporate', 'Total Revenues'],
        '2014': [8651.0, 8544.5, 6845.2, 3400.6, 27441.3],
        '2015': [8558.9, 7614.9, 6172.8, 3066.4, 25413.0],
        '2016': [8252.7, 7223.4, 6160.7, 2985.1, 24621.9],
        '2017': [8006.4, 7340.3, 5533.2, 1940.5, 22820.4],
        '2018': [7665.8, 7600.1, 3988.7, 1770.6, 21025.2]
    })

    op_income_unadj = pd.DataFrame({
        'Section': ['Operating Income by Segment'] * 5,
        'Segment': ['U.S', 'International Lead Markets', 'High Growth Markets', 'Foundational Markets & Corporate', 'Total Operating Income'],
        '2014': [3522.5, 3034.5, 933.9, 458.3, 7949.2],
        '2015': [3612.0, 2712.6, 841.1, -20.2, 7145.5],
        '2016': [3768.7, 2838.4, 1048.8, 88.6, 7744.5],
        '2017': [4022.4, 3166.5, 2001.4, 362.4, 9552.7],
        '2018': [4015.6, 3485.7, 1001.2, 320.1, 8822.6]
    })

    assets_unadj = pd.DataFrame({
        'Section': ['Assets by Segment'] * 5,
        'Segment': ['U.S', 'International Lead Markets', 'High Growth Markets', 'Foundational Markets & Corporate', 'Total Assets'],
        '2014': [11872.1, 12538.4, 5866.0, 3950.9, 34227.4],
        '2015': [11806.1, 11136.3, 5248.6, 9747.7, 37938.7],
        '2016': [11960.6, 9112.5, 5208.6, 4742.2, 31023.9],
        '2017': [12648.6, 11844.3, 4480.7, 4830.1, 33803.7],
        '2018': [14483.8, 12713.0, 4404.9, 1209.5, 32811.2]
    })

    cap_exp_unadj = pd.DataFrame({
        'Section': ['Capital and Expenditure by Segment'] * 5,
        'Segment': ['U.S', 'International Lead Markets', 'High Growth Markets', 'Foundational Markets & Corporate', 'Total Capital and Expenditure'],
        '2014': [736.1, 792.1, 804.8, 259.4, 2592.4],
        '2015': [533.2, 596.1, 540.5, 144.1, 1813.9],
        '2016': [586.7, 635.6, 493.2, 105.6, 1821.1],
        '2017': [861.2, 515.3, 378.5, 98.7, 1853.7],
        '2018': [1849.8, 436.4, 285.6, 169.9, 2741.7]
    })

    capex_unadj = pd.DataFrame({
        'Section': ['CapEx by Segment'] * 4,
        'Segment': ['U.S', 'International Lead Markets', 'High Growth Markets', 'Foundational Markets & Corporate'],
        '2014': [512.2, 521.2, 387.8, 223.3],
        '2015': [515.2, 460.9, 363.9, 215.7],
        '2016': [510.3, 451.6, 362.0, 192.6],
        '2017': [524.1, 461.1, 231.7, 146.5],
        '2018': [598.4, 472.9, 233.0, 177.7]
    })

    depr_unadj = pd.DataFrame({
        'Section': ['Depreciation by Segment'],
        'Segment': ['Total Depreciation & Amortization'],
        '2014': [1644.5],
        '2015': [1555.7],
        '2016': [1516.5],
        '2017': [1363.4],
        '2018': [1482.0]
    })

    # Combine all unadjusted data
    all_unadj_dfs = [revenues_unadj, op_income_unadj, assets_unadj, cap_exp_unadj, capex_unadj, depr_unadj]
    df_unadj_combined = pd.concat(all_unadj_dfs, ignore_index=True)

    # Show section name only once per group
    sections_mask = df_unadj_combined.groupby('Section').cumcount() == 0
    df_unadj_combined['Section'] = np.where(sections_mask, df_unadj_combined['Section'], '')

    # Compute adjusted for each, then combine
    adjusted_dfs = []
    for df in all_unadj_dfs:
        df_adj = df.copy()
        years = [col for col in df.columns if col in multipliers and col not in ['Section', 'Segment']]
        for year in years:
            df_adj[year] = df[year] * multipliers[year]
        adjusted_dfs.append(df_adj.round(1))
    df_adj_combined = pd.concat(adjusted_dfs, ignore_index=True)

    # Show section name only once per group for adjusted
    sections_mask_adj = df_adj_combined.groupby('Section').cumcount() == 0
    df_adj_combined['Section'] = np.where(sections_mask_adj, df_adj_combined['Section'], '')

    # Styling function for tables 
    def style_table(df, title, adjustment=''):
        def format_currency(val):
            if pd.isna(val):
                return ""
            return f"{val:,.1f}" if val >= 0 else f"({abs(val):,.1f})"

        styled = df.style.format({'2014': format_currency, '2015': format_currency, '2016': format_currency, '2017': format_currency, '2018': format_currency})
        
        # Highlight negatives
        def highlight_negatives(val):
            return 'background-color: #FF9999' if isinstance(val, (int, float)) and val < 0 else ''
        styled = styled.map(highlight_negatives, subset=pd.IndexSlice[:, ['2014', '2015', '2016', '2017', '2018']])
        
        # Highlight total rows in light green
        def highlight_totals(row):
            if 'Total' in row['Segment']:
                return ['background-color: #90EE90'] * len(row)
            return [''] * len(row)
        styled = styled.apply(highlight_totals, axis=1)
        
        # General styles
        styled = styled.set_properties(**{
            'text-align': 'left',
            'border': '1px solid black',
            'font-family': 'Arial',
            'font-size': '12pt',
            'padding': '5px'
        }, subset=pd.IndexSlice[:, ['Section', 'Segment']]).set_properties(**{
            'text-align': 'right',
            'border': '1px solid black',
            'font-family': 'Arial',
            'font-size': '12pt',
            'padding': '5px'
        }, subset=pd.IndexSlice[:, ['2014', '2015', '2016', '2017', '2018']]).set_table_styles([
            {'selector': 'th', 'props': [('text-align', 'center'), ('background-color', '#D3D3D3'), ('border', '1px solid black'), ('font-weight', 'bold'), ('padding', '5px')]},
            {'selector': 'caption', 'props': [('font-size', '14px'), ('font-weight', 'bold'), ('text-align', 'center'), ('margin-bottom', '10px')]}
        ]).set_caption(f"{title} {adjustment}<br><small>(All in $M)</small>")

        return styled.to_html()

    # Global legend configuration
    legend_config = dict(
        orientation="h",
        yanchor="bottom",
        y=-0.15,
        xanchor="center",
        x=0.5,
        font=dict(size=10)
    )

    # Total color 
    total_color = '#90EE90'

    # Section-specific color palettes 
    section_colors = {
        'Revenues by Segment': ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'],
        'Operating Income by Segment': ['#e377c2', '#7f7f7f', '#bcbd22', '#17becf'],
        'Assets by Segment': ['#aec7e8', '#ffbb78', '#98df8a', '#ff9896'],
        'Capital and Expenditure by Segment': ['#c5b0d5', '#c49c94', '#f7b6d2', '#f0f0f0'],
        'CapEx by Segment': ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'],
        'Depreciation by Segment': []  
    }

    # Plot functions
    def plot_revenues():
        years = ['2014', '2015', '2016', '2017', '2018']
        fig = go.Figure()
        # U.S
        fig.add_trace(go.Scatter(x=years, y=[9178.7, 9063.9, 8632.3, 8198.6, 7665.8], mode='lines+markers', name='U.S', 
                                 line=dict(width=2, color=section_colors['Revenues by Segment'][0]), 
                                 marker=dict(size=6, color=section_colors['Revenues by Segment'][0]),
                                 hovertemplate='<b>U.S</b><br>Year: %{x}<br>Value: %{y:,.0f}<extra></extra>'))
        # International Lead Markets
        fig.add_trace(go.Scatter(x=years, y=[9065.7, 8064.2, 7555.7, 7516.5, 7600.1], mode='lines+markers', name='International Lead Markets', 
                                 line=dict(width=2, color=section_colors['Revenues by Segment'][1]), 
                                 marker=dict(size=6, color=section_colors['Revenues by Segment'][1]),
                                 hovertemplate='<b>International Lead Markets</b><br>Year: %{x}<br>Value: %{y:,.0f}<extra></extra>'))
        # High Growth Markets
        fig.add_trace(go.Scatter(x=years, y=[7263.0, 6537.0, 6444.1, 5666.0, 3988.7], mode='lines+markers', name='High Growth Markets', 
                                 line=dict(width=2, color=section_colors['Revenues by Segment'][2]), 
                                 marker=dict(size=6, color=section_colors['Revenues by Segment'][2]),
                                 hovertemplate='<b>High Growth Markets</b><br>Year: %{x}<br>Value: %{y:,.0f}<extra></extra>'))
        # Foundational Markets & Corporate
        fig.add_trace(go.Scatter(x=years, y=[3608.0, 3247.3, 3122.4, 1987.1, 1770.6], mode='lines+markers', name='Foundational Markets & Corporate', 
                                 line=dict(width=2, color=section_colors['Revenues by Segment'][3]), 
                                 marker=dict(size=6, color=section_colors['Revenues by Segment'][3]),
                                 hovertemplate='<b>Foundational Markets & Corporate</b><br>Year: %{x}<br>Value: %{y:,.0f}<extra></extra>'))
        # Total Revenues
        fig.add_trace(go.Scatter(x=years, y=[29115.2, 26912.4, 25754.5, 23368.1, 21025.2], mode='lines+markers', name='Total Revenues', 
                                 line=dict(width=2, color=total_color), 
                                 marker=dict(size=6, color=total_color),
                                 hovertemplate='<b>Total Revenues</b><br>Year: %{x}<br>Value: %{y:,.0f}<extra></extra>'))
        fig.update_layout(title='Revenues by Segment (All Segments + Total)', xaxis_title="Year", yaxis_title="Value ($M)", 
                          template='plotly_white', height=400, showlegend=True, font=dict(size=12),
                          legend=legend_config, hovermode='x unified')
        fig.update_xaxes(showgrid=True)
        fig.update_yaxes(tickformat=",.0f")
        return fig

    def plot_operating_income():
        years = ['2014', '2015', '2016', '2017', '2018']
        fig = go.Figure()
        # U.S
        fig.add_trace(go.Scatter(x=years, y=[3737.4, 3825.1, 3942.1, 4118.9, 4015.6], mode='lines+markers', name='U.S', 
                                 line=dict(width=2, color=section_colors['Operating Income by Segment'][0]), 
                                 marker=dict(size=6, color=section_colors['Operating Income by Segment'][0]),
                                 hovertemplate='<b>U.S</b><br>Year: %{x}<br>Value: %{y:,.0f}<extra></extra>'))
        # International Lead Markets
        fig.add_trace(go.Scatter(x=years, y=[3219.6, 2872.6, 2969.0, 3242.5, 3485.7], mode='lines+markers', name='International Lead Markets', 
                                 line=dict(width=2, color=section_colors['Operating Income by Segment'][1]), 
                                 marker=dict(size=6, color=section_colors['Operating Income by Segment'][1]),
                                 hovertemplate='<b>International Lead Markets</b><br>Year: %{x}<br>Value: %{y:,.0f}<extra></extra>'))
        # High Growth Markets
        fig.add_trace(go.Scatter(x=years, y=[990.9, 890.7, 1097.0, 2049.4, 1001.2], mode='lines+markers', name='High Growth Markets', 
                                 line=dict(width=2, color=section_colors['Operating Income by Segment'][2]), 
                                 marker=dict(size=6, color=section_colors['Operating Income by Segment'][2]),
                                 hovertemplate='<b>High Growth Markets</b><br>Year: %{x}<br>Value: %{y:,.0f}<extra></extra>'))
        # Foundational Markets & Corporate
        fig.add_trace(go.Scatter(x=years, y=[486.3, -21.4, 92.7, 371.1, 320.1], mode='lines+markers', name='Foundational Markets & Corporate', 
                                 line=dict(width=2, color=section_colors['Operating Income by Segment'][3]), 
                                 marker=dict(size=6, color=section_colors['Operating Income by Segment'][3]),
                                 hovertemplate='<b>Foundational Markets & Corporate</b><br>Year: %{x}<br>Value: %{y:,.0f}<extra></extra>'))
        # Total Operating Income
        fig.add_trace(go.Scatter(x=years, y=[8434.1, 7567.1, 8100.7, 9782.0, 8822.6], mode='lines+markers', name='Total Operating Income', 
                                 line=dict(width=2, color=total_color), 
                                 marker=dict(size=6, color=total_color),
                                 hovertemplate='<b>Total Operating Income</b><br>Year: %{x}<br>Value: %{y:,.0f}<extra></extra>'))
        fig.update_layout(title='Operating Income by Segment (All Segments + Total)', xaxis_title="Year", yaxis_title="Value ($M)", 
                          template='plotly_white', height=400, showlegend=True, font=dict(size=12),
                          legend=legend_config, hovermode='x unified')
        fig.update_xaxes(showgrid=True)
        fig.update_yaxes(tickformat=",.0f")
        return fig

    def plot_assets():
        years = ['2014', '2015', '2016', '2017', '2018']
        fig = go.Figure()
        # U.S
        fig.add_trace(go.Scatter(x=years, y=[12596.3, 12502.7, 12510.8, 12952.2, 14483.8], mode='lines+markers', name='U.S', 
                                 line=dict(width=2, color=section_colors['Assets by Segment'][0]), 
                                 marker=dict(size=6, color=section_colors['Assets by Segment'][0]),
                                 hovertemplate='<b>U.S</b><br>Year: %{x}<br>Value: %{y:,.0f}<extra></extra>'))
        # International Lead Markets
        fig.add_trace(go.Scatter(x=years, y=[13303.2, 11793.3, 9531.7, 12128.6, 12713.0], mode='lines+markers', name='International Lead Markets', 
                                 line=dict(width=2, color=section_colors['Assets by Segment'][1]), 
                                 marker=dict(size=6, color=section_colors['Assets by Segment'][1]),
                                 hovertemplate='<b>International Lead Markets</b><br>Year: %{x}<br>Value: %{y:,.0f}<extra></extra>'))
        # High Growth Markets
        fig.add_trace(go.Scatter(x=years, y=[6223.8, 5558.3, 5448.2, 4588.2, 4404.9], mode='lines+markers', name='High Growth Markets', 
                                 line=dict(width=2, color=section_colors['Assets by Segment'][2]), 
                                 marker=dict(size=6, color=section_colors['Assets by Segment'][2]),
                                 hovertemplate='<b>High Growth Markets</b><br>Year: %{x}<br>Value: %{y:,.0f}<extra></extra>'))
        # Foundational Markets & Corporate
        fig.add_trace(go.Scatter(x=years, y=[4191.9, 10322.8, 4960.3, 4946.0, 1209.5], mode='lines+markers', name='Foundational Markets & Corporate', 
                                 line=dict(width=2, color=section_colors['Assets by Segment'][3]), 
                                 marker=dict(size=6, color=section_colors['Assets by Segment'][3]),
                                 hovertemplate='<b>Foundational Markets & Corporate</b><br>Year: %{x}<br>Value: %{y:,.0f}<extra></extra>'))
        # Total Assets
        fig.add_trace(go.Scatter(x=years, y=[36315.3, 40177.1, 32451.0, 34615.0, 32811.2], mode='lines+markers', name='Total Assets', 
                                 line=dict(width=2, color=total_color), 
                                 marker=dict(size=6, color=total_color),
                                 hovertemplate='<b>Total Assets</b><br>Year: %{x}<br>Value: %{y:,.0f}<extra></extra>'))
        fig.update_layout(title='Assets by Segment (All Segments + Total)', xaxis_title="Year", yaxis_title="Value ($M)", 
                          template='plotly_white', height=400, showlegend=True, font=dict(size=12),
                          legend=legend_config, hovermode='x unified')
        fig.update_xaxes(showgrid=True)
        fig.update_yaxes(tickformat=",.0f")
        return fig

    def plot_capital_expenditure():
        years = ['2014', '2015', '2016', '2017', '2018']
        fig = go.Figure()
        # U.S
        fig.add_trace(go.Scatter(x=years, y=[781.0, 564.7, 613.7, 881.9, 1849.8], mode='lines+markers', name='U.S', 
                                 line=dict(width=2, color=section_colors['Capital and Expenditure by Segment'][0]), 
                                 marker=dict(size=6, color=section_colors['Capital and Expenditure by Segment'][0]),
                                 hovertemplate='<b>U.S</b><br>Year: %{x}<br>Value: %{y:,.0f}<extra></extra>'))
        # International Lead Markets
        fig.add_trace(go.Scatter(x=years, y=[840.4, 631.3, 664.8, 527.7, 436.4], mode='lines+markers', name='International Lead Markets', 
                                 line=dict(width=2, color=section_colors['Capital and Expenditure by Segment'][1]), 
                                 marker=dict(size=6, color=section_colors['Capital and Expenditure by Segment'][1]),
                                 hovertemplate='<b>International Lead Markets</b><br>Year: %{x}<br>Value: %{y:,.0f}<extra></extra>'))
        # High Growth Markets
        fig.add_trace(go.Scatter(x=years, y=[853.9, 572.4, 515.9, 387.6, 285.6], mode='lines+markers', name='High Growth Markets', 
                                 line=dict(width=2, color=section_colors['Capital and Expenditure by Segment'][2]), 
                                 marker=dict(size=6, color=section_colors['Capital and Expenditure by Segment'][2]),
                                 hovertemplate='<b>High Growth Markets</b><br>Year: %{x}<br>Value: %{y:,.0f}<extra></extra>'))
        # Foundational Markets & Corporate
        fig.add_trace(go.Scatter(x=years, y=[259.4, 144.1, 105.6, 98.7, 169.9], mode='lines+markers', name='Foundational Markets & Corporate', 
                                 line=dict(width=2, color=section_colors['Capital and Expenditure by Segment'][3]), 
                                 marker=dict(size=6, color=section_colors['Capital and Expenditure by Segment'][3]),
                                 hovertemplate='<b>Foundational Markets & Corporate</b><br>Year: %{x}<br>Value: %{y:,.0f}<extra></extra>'))
        # Total Capital and Expenditure
        fig.add_trace(go.Scatter(x=years, y=[2734.7, 1912.4, 1900.0, 1895.8, 2741.7], mode='lines+markers', name='Total Capital and Expenditure', 
                                 line=dict(width=2, color=total_color), 
                                 marker=dict(size=6, color=total_color),
                                 hovertemplate='<b>Total Capital and Expenditure</b><br>Year: %{x}<br>Value: %{y:,.0f}<extra></extra>'))
        fig.update_layout(title='Capital and Expenditure by Segment (All Segments + Total)', xaxis_title="Year", yaxis_title="Value ($M)", 
                          template='plotly_white', height=400, showlegend=True, font=dict(size=12),
                          legend=legend_config, hovermode='x unified')
        fig.update_xaxes(showgrid=True)
        fig.update_yaxes(tickformat=",.0f")
        return fig

    def plot_capex():
        years = ['2014', '2015', '2016', '2017', '2018']
        fig = go.Figure()
        # U.S
        fig.add_trace(go.Scatter(x=years, y=[543.6, 546.0, 533.7, 537.4, 598.4], mode='lines+markers', name='U.S', 
                                 line=dict(width=2, color=section_colors['CapEx by Segment'][0]), 
                                 marker=dict(size=6, color=section_colors['CapEx by Segment'][0]),
                                 hovertemplate='<b>U.S</b><br>Year: %{x}<br>Value: %{y:,.0f}<extra></extra>'))
        # International Lead Markets
        fig.add_trace(go.Scatter(x=years, y=[552.8, 488.4, 472.4, 472.5, 472.9], mode='lines+markers', name='International Lead Markets', 
                                 line=dict(width=2, color=section_colors['CapEx by Segment'][1]), 
                                 marker=dict(size=6, color=section_colors['CapEx by Segment'][1]),
                                 hovertemplate='<b>International Lead Markets</b><br>Year: %{x}<br>Value: %{y:,.0f}<extra></extra>'))
        # High Growth Markets
        fig.add_trace(go.Scatter(x=years, y=[411.7, 385.6, 378.7, 237.3, 233.0], mode='lines+markers', name='High Growth Markets', 
                                 line=dict(width=2, color=section_colors['CapEx by Segment'][2]), 
                                 marker=dict(size=6, color=section_colors['CapEx by Segment'][2]),
                                 hovertemplate='<b>High Growth Markets</b><br>Year: %{x}<br>Value: %{y:,.0f}<extra></extra>'))
        # Foundational Markets & Corporate
        fig.add_trace(go.Scatter(x=years, y=[237.0, 228.4, 201.6, 150.1, 177.7], mode='lines+markers', name='Foundational Markets & Corporate', 
                                 line=dict(width=2, color=section_colors['CapEx by Segment'][3]), 
                                 marker=dict(size=6, color=section_colors['CapEx by Segment'][3]),
                                 hovertemplate='<b>Foundational Markets & Corporate</b><br>Year: %{x}<br>Value: %{y:,.0f}<extra></extra>'))
        fig.update_layout(title='CapEx by Segment (All Segments)', xaxis_title="Year", yaxis_title="Value ($M)", 
                          template='plotly_white', height=400, showlegend=True, font=dict(size=12),
                          legend=legend_config, hovermode='x unified')
        fig.update_xaxes(showgrid=True)
        fig.update_yaxes(tickformat=",.0f")
        return fig

    # Generate graphs
    fig_revenues = plot_revenues()
    fig_op_income = plot_operating_income()
    fig_assets = plot_assets()
    fig_cap_exp = plot_capital_expenditure()
    fig_capex = plot_capex()

    # Display tables
    table_adj_html = style_table(df_adj_combined, "Segment Analysis", "(Adjusted to 2018 USD)")
    table_unadj_html = style_table(df_unadj_combined, "Segment Analysis", "(Unadjusted)")

    html_output = f"""
    <div style="margin-bottom: 40px;">
        {table_adj_html}
    </div>
    <div style="margin-bottom: 40px;">
        {table_unadj_html}
    </div>
    <div style="margin-bottom: 40px;">
        {fig_revenues.to_html(full_html=False, include_plotlyjs='cdn')}
    </div>
    <div style="margin-bottom: 40px;">
        {fig_op_income.to_html(full_html=False, include_plotlyjs='cdn')}
    </div>
    <div style="margin-bottom: 40px;">
        {fig_assets.to_html(full_html=False, include_plotlyjs='cdn')}
    </div>
    <div style="margin-bottom: 40px;">
        {fig_cap_exp.to_html(full_html=False, include_plotlyjs='cdn')}
    </div>
    <div style="margin-bottom: 40px;">
        {fig_capex.to_html(full_html=False, include_plotlyjs='cdn')}
    </div>
    <p style='font-family:Arial;font-size:12px;text-align:center;'>All values in $M. Adjusted to 2018 USD using BLS CPI-U multipliers (rounded).</p>
    """

    display(HTML(html_output))

# Run the function
if __name__ == "__main__":
    segment_analysis()

# Quartely Analysis

import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from IPython.display import HTML, Markdown, display

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
    display(Markdown(markdown_text))

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
    display(HTML(style_table(revenues_adj, "Adjusted Quarterly Revenues (2018 USD)", "All in $M")))
    display(HTML(style_table(revenues_unadj, "Unadjusted Quarterly Revenues", "All in $M")))
    display(HTML(style_table(seasonality, "Seasonality Factors", "Computed as (Quarterly Revenue / (Annual Total / 4)); Yearly Factor = Avg of Q1-Q4 Seasonalites")))
    display(HTML(style_table(volatility, "Volatility Metrics", "Computed: Mean/Std Dev of Quarters per Year; Volatility = Std Dev / Mean (All in $M except %; based on unadjusted)")))

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

    display(fig_seas)

    # Footer
    footer_md = """
<p style='font-family:Arial;font-size:12px;text-align:center;'>All revenues in $M (adjusted to 2018 USD via CPI multipliers). Seasonality = (Quarterly Revenue / (Annual Total / 4)). Yearly Factor = Avg of Q1-Q4 Seasonalites. Volatility = Std Dev / Mean (of quarters per year). Key Insight: Q2 consistently strongest (avg seasonality 1.033); volatility peaked in 2017 at 5.11% due to refranchising shifts.</p>
<p style='font-family:Arial;font-size:12px;'>Go to Home | Go to Segment Analysis | Go to Ratios | Go to Forecast</p>
"""
    display(Markdown(footer_md))

# Run the function
if __name__ == "__main__":
    quarterly_analysis()

# Market Research

import pandas as pd
import numpy as np
from IPython.display import HTML, Markdown, display

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
    display(Markdown(markdown_text))

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
    display(HTML(style_table(adj_data, "Market Research", "(Adjusted to 2018 USD)")))
    display(HTML(style_table(unadj_market_df, "Unadjusted Market Sizes", "(Nominal)", "All in $M")))

    # Footer with reference
    footer_md = f"""
<p style='font-family:Arial;font-size:12px;text-align:center;'>Adjusted to 2018 USD via BLS CPI-U multipliers. Average RG (Adjusted): {avg_rg_adj:.2%}. Cycle Phase: All Expansion.</p>
<p style='font-family:Arial;font-size:21px;'>Market Size Source: <a href="https://www.ibisworld.com/global/market-size/global-fast-food-restaurants/1480/">IBISWorld Global Fast Food Restaurants</a></p>
"""
    display(Markdown(footer_md))

# Run the function
if __name__ == "__main__":
    market_research()

# Assumed Growth

from IPython.display import Markdown, display, Code

def assumed_growth():
    """
    Replicates the 'Assumed Growth' worksheet from the McDonald's financial model.
    Displays comprehensive narrative on Baseline and Pandemic Disruption (incl. Hindsight) scenarios.
    Uses Markdown for formatted text, with inline math and references.
    No tables or graphs; pure explanatory content with year-by-year breakdowns.
    All figures in 2018 USD.
    """
    markdown_text = """
# Assumed Growth

This section provides a comprehensive analysis of the global fast food market and McDonald’s revenue potential under two distinct scenarios: 
**Baseline Growth**, representing a stable and optimistic market outlook, and **Pandemic Disruption** (which also includes **Hindsight Scenario**),
simulating the impact of a severe global health crisis. The evaluation utilizes historical data from 2014 to 2018, adjusted to 2018 USD using BLS 
CPI-U indices, to inform growth assumptions and project outcomes through 2023. Each scenario is detailed below with supporting calculations and 
justifications, setting a solid foundation for the forecast that follows.

### 1) Baseline Growth
In the Baseline Growth scenario, the Compound Annual Growth Rate (CAGR) is derived from historical market size data, spanning 792,250 million USD 
in 2014 to 906,710 million USD in 2018. The calculated historical CAGR is:

$$\\text{CAGR} = \\left( \\frac{906710}{792250} \\right)^{(\\frac{1}{4})} - 1 \\approx 1.0345 - 1 \\approx \\mathbf{3.45\\%}$$

To reflect anticipated market expansion, driven by rising consumer demand, technological innovations (e.g., digital ordering and delivery systems), 
and growth in emerging markets, I have adopted a slightly higher CAGR of **4%**. This adjustment represents a conservative yet forward-looking estimate,
informed by current market trends and my research insights. For McDonald’s revenue, a **2% annual growth rate** is assumed from 2019 to 2023, designed
to offset the approximate **7.8% average annual decline** observed over the prior five years (2014–2018), thereby supporting a sustainable recovery and
growth trajectory in a stable economic environment. Historical reports, such as Transparency Market Research (2016), are challenging to access due to
paywalls or outdated revisions, and thus were not relied upon; the 4% CAGR is a reasoned projection based on available data and industry observations.

### 2) Pandemic Disruption
In the Pandemic Disruption scenario, a reduced CAGR of **1.5%** is applied for the market size, reflecting the anticipated impact of a severe global
pandemic starting in late 2019, with significant effects beginning in early 2020. The market remains stagnant in 2019–2020, followed by a 1.5% CAGR 
recovery from 2021 onward. For McDonald’s, revenue grows by **+5.0%** in 2019, capturing initial resilience or demand surge in the early phase of the
pandemic, followed by declines of **-10.0%** in 2020 and **-14.0%** in 2021 as the crisis peaks with reduced consumer activity and operational 
constraints. A gradual recovery begins in 2022 with **+8.0%** growth, followed by **+5.0%** in 2023, accounting for a cautious market rebound under 
challenging conditions. These trends are informed by McDonald’s historical performance during pre-2018 crises, such as the 2003 SARS outbreak 
(1–5% sales impact, 5–10% recovery) and the 2008–2009 financial crisis (flat to 5% growth, 5–6% recovery), as well as your 2014–2018 data 
(average 7.8% decline). Industry insights from the 2003 SARS period (10–40% declines in hospitality) and economic downturns (5–15% recovery rates) 
provide additional context. The timeline—late 2019 onset, early 2020 impact, 2021 peak, and 2022–2023 recovery—captures a realistic progression of a 
severe pandemic, balancing McDonald’s operational strengths with the crisis’s severity.

#### 2019: +5.0% Growth
In 2019, McDonald’s revenue increases by **5.0%**. This growth reflects the early phase of the pandemic, starting in late 2019, before its full impact 
is felt. Historically, during the initial stages of crises, fast food chains like McDonald’s often experience a demand surge as consumers turn to 
affordable, convenient, and perceived ‘safe’ dining options. For example, during the 2003 SARS outbreak in Asia, McDonald’s reported stable or slightly 
increased sales in affected regions (e.g., Hong Kong, China), as noted in their 2003 annual report, with global revenues growing by **1–2%** despite 
regional disruptions (McDonald’s 2003 10-K). This was attributed to consumers favoring quick-service restaurants over dine-in establishments due to
health concerns. Similarly, during the 2008–2009 financial crisis, McDonald’s global revenues grew by **3–5%** in 2009 (McDonald’s 2009 10-K), driven 
by its value menu and drive-thru operations.

#### 2020: -10.0% Decline
In 2020, revenue declines by **10.0%**. This decrease reflects the pandemic’s full impact, starting in early 2020, with global restrictions, reduced 
foot traffic, and economic uncertainty affecting the fast food industry. While McDonald’s typically performs better than other sectors during downturns,
a severe pandemic would pose significant challenges, such as temporary store closures and supply chain disruptions. During the 2003 SARS outbreak, the
broader hospitality sector in affected regions saw revenue declines of **10–30%** (World Health Organization, 2003; Hong Kong Tourism Board, 2004), 
though McDonald’s mitigated losses through drive-thru and takeout, reporting a milder **1–3%** sales dip in Asia (McDonald’s 2003 10-Q). In the 
2008–2009 financial crisis, McDonald’s global same-store sales remained flat or declined slightly (e.g., **-2%** in some regions, per 2009 10-K), but 
overall revenues grew due to expansion. In this harsher scenario, a **10.0%** decline accounts for a more significant impact, assuming dine-in
restrictions and economic contraction.

#### 2021: -14.0% Decline
In 2021, revenue declines further by **14.0%**. This represents the peak impact of the pandemic, with prolonged restrictions, reduced consumer spending,
and operational challenges (e.g., labor shortages, supply chain issues) exacerbating the downturn. The deeper decline in 2021 compared to 2020 captures 
a delayed peak in the crisis, potentially due to secondary waves or extended economic fallout. During the 2003 SARS outbreak, some hospitality sectors 
saw cumulative declines of **20–40%** over multiple quarters (Asian Development Bank, 2004), with fast food chains like McDonald’s experiencing milder
but still notable impacts (e.g., **3–5%** sales drops in Q2 2003, per McDonald’s 2003 10-Q). In the 2008–2009 financial crisis, McDonald’s saw flat or
declining same-store sales in 2009 (e.g., **-2%** in Europe, per 2009 10-K), with recovery delayed in some markets. In this scenario, a **14.0%**
decline reflects a worse-case impact.

#### 2022: +8.0% Growth
In 2022, revenue grows by **8.0%**, marking the start of recovery as the pandemic eases. This rebound reflects the lifting of restrictions, a resurgence
in consumer confidence, and McDonald’s operational adaptations (e.g., expanded takeout, reopened stores). Post-SARS, McDonald’s in affected regions saw 
sales recover by **5–10%** in 2004 (McDonald’s 2004 10-K), driven by pent-up demand and operational improvements. During the recovery from the 2008–2009
financial crisis, McDonald’s global same-store sales grew by **5.6%** in 2010 (McDonald’s 2010 10-K), supported by value offerings and market expansion.
In this scenario, an **8.0%** growth rate aligns with these historical recovery patterns.

#### 2023: +5.0% Growth
In 2023, revenue grows by **5.0%**, indicating continued but slower recovery as the market stabilizes. This growth reflects sustained improvements in 
consumer spending, operational efficiency, and market expansion post-pandemic. After the 2003 SARS outbreak, McDonald’s maintained steady growth of 
**3–5%** in 2005 in previously affected regions (McDonald’s 2005 10-K), supported by renewed consumer confidence. Similarly, post-2009 financial crisis,
McDonald’s global same-store sales grew by **5.0%** in 2011 (McDonald’s 2011 10-K), driven by menu innovation and global expansion. In this scenario,
a **5.0%** growth rate matches these historical trends.

### Hindsight Scenario
The Hindsight scenario assumes a **2% compound annual growth rate (CAGR)** for the global fast-food market, representing a moderate growth outlook. 
This rate was chosen as a balanced middle ground between the optimistic Baseline scenario (**4% CAGR**) and the pessimistic Worst-Case scenario 
(**1.5% CAGR**). It reflects potential market uncertainties—such as economic fluctuations or moderate disruptions—while still recognizing the fast-food
industry’s historical resilience and ability to sustain growth in challenging conditions. This scenario enriches the analysis by offering a 
nuanced view of possible market outcomes.

**Note:**  
The Pandemic Disruption scenario uses revenue trends derived from the 2003 SARS outbreak (**-10%** in 2020, **-14%** in 2021) and the 2008 financial 
crisis, reflecting a company-specific impact during severe disruptions. These percentages were retained in Hindsight scenario to maintain consistency 
with historical crisis data, which show how unprepared companies can face significant revenue declines even in a resilient market. While the global 
fast-food market may exhibit moderate growth (**2% CAGR** in the Hindsight scenario), a company like McDonald’s might not perform as well if it fails
to adapt (delayed adoption of alternatives like delivery, digital sales platforms). The **-10%** and **-14%** drops model a worst-case outcome where
such unpreparedness amplifies revenue impacts beyond market trends, capturing vulnerability of a single company in a crisis. This approach provides 

a contrast to more moderate scenarios and highlighting the potential gap between market resilience and company-specific outcomes.

### General Note
All financial figures are presented in **2018 USD**, adjusted using BLS CPI-U multipliers to account for inflation. The CPI multipliers for 2019–2023
(**0.990, 0.980, 0.970, 0.960, 0.950**) are derived from an assumed **1% annual inflation rate**, calculated as: $1 / (1 + 0.01)^{(t - 2018)}$.  
Data sources include McDonald’s 10-K and 10-Q filings (SEC EDGAR), IBISWorld’s 2018 Global Fast Food Restaurants Industry Report (paywalled, 
[https://www.ibisworld.com/global/market-size/global-fast-food-restaurants/1480/](https://www.ibisworld.com/global/market-size/global-fast-food-restaurants/1480/)),
and Transparency Market Research 2016 (paywalled, [https://www.transparencymarketresearch.com/global-fast-food-market.html](https://www.transparencymarketresearch.com/global-fast-food-market.html)),
though access to decade-old reports is limited due to paywall restrictions or updates.
"""
    display(Markdown(markdown_text))

# Run the function
if __name__ == "__main__":
    assumed_growth()

# Forecast

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from IPython.display import HTML, Markdown, display

def forecast():
    """
    Generates transposed tables for the Baseline Growth and Pandemic Disruption scenarios, 
    and two separate line graphs for Market Size & Adjusted Revenue comparisons.
    """
    markdown_text = """
<div style="text-align: center;">

# Forecast

</div>
"""
    display(Markdown(markdown_text))

    # Baseline Growth Assumptions
    baseline_assump_data = {
        'Assumption': ['Assumed CAGR', 'Assumed Revenue Growth', 'Market size (2018)', 'Revenue (2018)'],
        'Value': ['4%', '2%', '9,06,714.2', '21,025.2']
    }
    df_baseline_assump = pd.DataFrame(baseline_assump_data)

    # Baseline Growth Table Data 
    baseline_table_data = {
        'Year': ['2019', '2020', '2021', '2022', '2023'],
        'Projected Market size (4%)': [942982.8, 980702.1, 1019930.2, 1060727.4, 1103156.5],
        'Revenue Growth (%)': [0.02, 0.02, 0.02, 0.02, 0.02],
        'CPI Multiplier': [0.99, 0.98, 0.97, 0.96, 0.95],
        'Projected nominal Revenue': [21445.7, 21874.6, 22312.1, 22758.4, 23213.5],
        'Adjusted Revenue': [21662.3, 22321.0, 23002.2, 23706.6, 24435.3],
        'Market Share (%)': [0.0230, 0.0228, 0.0226, 0.0223, 0.0222]
    }
    df_baseline_table = pd.DataFrame(baseline_table_data)

    # Pandemic Disruption Assumptions
    pandemic_assump_data = {
        'Assumption': ['Assumed CAGR', 'Hindsight scenario', 'Market size (2018)', 'Revenue (2018)'],
        'Value': ['1.5%', '2%', '9,06,714.2', '21,025.2']
    }
    df_pandemic_assump = pd.DataFrame(pandemic_assump_data)

    # Pandemic Disruption Table Data 
    pandemic_table_data = {
        'Year': ['2019', '2020', '2021', '2022', '2023'],
        'Projected Market size (1.5%)': [920314.9, 934119.6, 948131.4, 962353.4, 976788.7],
        'Hindsight Scenario for Market size (2%)': [924848.5, 943345.5, 962212.4, 981456.6, 1001085.7],
        'Revenue Growth (%)': [0.05, -0.10, -0.14, 0.08, 0.05],
        'CPI Multiplier': [0.99, 0.98, 0.97, 0.96, 0.95],
        'Projected nominal Revenue': [22076.5, 19868.8, 17087.2, 18454.2, 19376.9],
        'Adjusted Revenue': [22299.5, 20274.3, 17615.6, 19223.1, 20396.7],
        'Market Share (%)': [0.0242, 0.0217, 0.0186, 0.0200, 0.0209]
    }
    df_pandemic_table = pd.DataFrame(pandemic_table_data)

    # Styling Functions 
    def format_currency(val):
        if pd.notnull(val):
            return f"{val:,.1f}" if val >= 0 else f"({abs(val):,.1f})"
        return "-"

    def format_percentage(val):
        if pd.notnull(val):
            return f"{val * 100:.2f}%" if val >= 0 else f"({abs(val) * 100:.2f}%)"
        return "-"

    def format_multiplier(val):
        if pd.notnull(val):
            return f"{val:.2f}"
        return "-"

    def style_assumptions(df):
        def assumption_formatter(x):
            if isinstance(x, (int, float)):
                return f"{x:,.1f}"
            if isinstance(x, str):
                try:
                    clean_x = x.replace(',', '')
                    return f"{float(clean_x):,.1f}"
                except ValueError:
                    return x
            return str(x)

        styled = df.style.format({'Value': assumption_formatter}) \
            .set_properties(**{'text-align': 'center', 'border': '1px solid black', 'font-family': 'Arial', 'font-size': '12pt', 'padding': '5px', 'background-color': '#1A1A1A', 'color': 'white'}) \
            .set_table_styles([
                {'selector': 'th', 'props': [('text-align', 'center'), ('background-color', '#333333'), ('border', '1px solid black'), ('font-weight', 'bold'), ('padding', '5px'), ('color', 'white')]},
                {'selector': 'caption', 'props': [('font-size', '16px'), ('font-weight', 'bold'), ('text-align', 'center'), ('margin-bottom', '10px'), ('color', 'white')]},
                {'selector': 'td', 'props': [('background-color', '#2D2D2D'), ('color', 'white')]}
            ])
        return styled

    def style_table(df):
        ratio_cols = ['Revenue Growth (%)', 'Market Share (%)']
        currency_cols = [col for col in df.columns if 'Market size' in col or 'Revenue' in col]
        data_cols = df.columns[1:].tolist()
        styled = df.style

        for col in currency_cols:
            styled = styled.format(format_currency, subset=pd.IndexSlice[:, col])

        for col in ratio_cols:
            if col in df.columns:
                styled = styled.format(format_percentage, subset=pd.IndexSlice[:, col])

        if 'CPI Multiplier' in df.columns:
            styled = styled.format(format_multiplier, subset=pd.IndexSlice[:, 'CPI Multiplier'])

        styled = styled.set_properties(**{
            'font-weight': 'bold',
            'text-align': 'center',
            'background-color': '#2D2D2D',
            'color': 'white'
        }, subset=pd.IndexSlice[:, data_cols])

        styled = styled.set_properties(**{
            'text-align': 'left',
            'font-weight': 'bold',
            'background-color': '#1A1A1A',
            'color': 'white'
        }, subset=pd.IndexSlice[:, 'Year'])

        for col in ratio_cols:
            if col in df.columns:
                styled = styled.set_properties(**{'background-color': '#404040'}, subset=pd.IndexSlice[:, col])

        def highlight_negatives(val):
            return 'background-color: #FF9999; color: black;' if isinstance(val, (int, float)) and val < 0 else ''
        styled = styled.map(highlight_negatives, subset=pd.IndexSlice[:, data_cols])

        styled = styled.set_properties(**{
            'border': '1px solid black',
            'font-family': 'Arial',
            'font-size': '12pt',
            'padding': '5px',
            'color': 'white'
        }).set_table_styles([
            {'selector': 'th', 'props': [('text-align', 'center'), ('background-color', '#333333'), ('border', '1px solid black'), ('font-weight', 'bold'), ('padding', '5px'), ('color', 'white')]},
            {'selector': 'caption', 'props': [('font-size', '16px'), ('font-weight', 'bold'), ('text-align', 'center'), ('margin-bottom', '10px'), ('color', 'white')]},
            {'selector': 'td', 'props': [('background-color', '#2D2D2D'), ('color', 'white')]}
        ])

        return styled

    # Apply styling 
    styled_baseline_assump = style_assumptions(df_baseline_assump).set_caption("Baseline Growth Assumptions")
    styled_baseline_table = style_table(df_baseline_table).set_caption("Baseline Growth Scenario")
    styled_pandemic_assump = style_assumptions(df_pandemic_assump).set_caption("Pandemic Disruption Assumptions")
    styled_pandemic_table = style_table(df_pandemic_table).set_caption("Pandemic Disruption Scenario")

    # Display tables
    print("\n")
    display(HTML(styled_baseline_assump.to_html()))
    print("\n")
    display(HTML(styled_baseline_table.to_html()))
    print("\n")
    display(HTML(styled_pandemic_assump.to_html()))
    print("\n")
    display(HTML(styled_pandemic_table.to_html()))
    print("\n")

    # Graphs 
    years = ['2019', '2020', '2021', '2022', '2023']

    # Original Market Size Data
    market_size_baseline = [942982.8, 980702.1, 1019930.2, 1060727.4, 1103156.5]
    proj_market_pandemic = [920314.9, 934119.6, 948131.4, 962353.4, 976788.7]
    hindsight_market_pandemic = [924848.5, 943345.5, 962212.4, 981456.6, 1001085.7]
    adjusted_revenue_baseline = [21662.3, 22321.0, 23002.2, 23706.6, 24435.3]
    adjusted_revenue_pandemic = [22299.5, 20274.3, 17615.6, 19223.1, 20396.7]
    
    # Market Size config
    scale_factor = 1000000 
    market_size_baseline_B = [x / scale_factor for x in market_size_baseline]
    proj_market_pandemic_B = [x / scale_factor for x in proj_market_pandemic]
    hindsight_market_pandemic_B = [x / scale_factor for x in hindsight_market_pandemic]


    # Plot 1: Baseline
    fig1 = make_subplots(specs=[[{"secondary_y": True}]])
    fig1.add_trace(
        go.Scatter(x=years, y=adjusted_revenue_baseline, name="Adjusted Revenue (Millions USD)", line=dict(color='#6A0DAD')),
        secondary_y=False,
    )
    fig1.add_trace(
        
        go.Scatter(x=years, y=market_size_baseline_B, name="Market Size (Billions USD)", line=dict(color='#FF6347')),
        secondary_y=True,
    )
    fig1.update_xaxes(title_text="Year", showgrid=True)
    fig1.update_yaxes(title_text="Adjusted Revenue (Millions USD)", secondary_y=False, tickformat=",.0f")
    fig1.update_yaxes(title_text="Market Size (Billions USD)", secondary_y=True, tickformat=",.2f")
    
    fig1.update_layout(
        title="Baseline: Market Size and Adjusted Revenue (2019-2023)",
        template='plotly_white',
        height=400,
        showlegend=True,
        title_font_size=16,
        font=dict(size=12, family='Arial', color='black'),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.3,
            xanchor="center",
            x=0.5
        ),
        plot_bgcolor='white',
        paper_bgcolor='white',
        hovermode='x unified',
    )
    fig1.show()

    # Plot 2: Pandemic
    fig2 = make_subplots(specs=[[{"secondary_y": True}]])
    fig2.add_trace(
        go.Scatter(x=years, y=adjusted_revenue_pandemic, name="Adjusted Revenue (Millions USD)", line=dict(color='#008080')),
        secondary_y=False,
    )
    fig2.add_trace(
        
        go.Scatter(x=years, y=proj_market_pandemic_B, name="Projected Market Size (1.5% CAGR)", line=dict(color='#FF6347')),
        secondary_y=True,
    )
    fig2.add_trace(
        
        go.Scatter(x=years, y=hindsight_market_pandemic_B, name="Hindsight Market Size (2% CAGR)", line=dict(color='#FFD700')),
        secondary_y=True,
    )
    fig2.update_xaxes(title_text="Year", showgrid=True)
    fig2.update_yaxes(title_text="Adjusted Revenue (Millions USD)", secondary_y=False, tickformat=",.0f")
    
    fig2.update_yaxes(title_text="Market Size (Billions USD)", secondary_y=True, tickformat=",.2f")
    
    fig2.update_layout(
        title="Pandemic: Projected Market Sizes and Adjusted Revenue (2019-2023)",
        template='plotly_white',
        height=400,
        showlegend=True,
        title_font_size=16,
        font=dict(size=12, family='Arial', color='black'),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.3,
            xanchor="center",
            x=0.5
        ),
        plot_bgcolor='white',
        paper_bgcolor='white',
        hovermode='x unified',
    )
    fig2.show()

# Run the function
if __name__ == "__main__":
    forecast()

# References

from IPython.display import HTML, display, Markdown

def references():
    markdown_text = """
<div style="text-align: center;">

# References

</div>
"""
    display(Markdown(markdown_text))

    CATEGORIES = [
    # 10-K
    "McDonald's Annual Reports (10-K)", "McDonald's Annual Reports (10-K)", "McDonald's Annual Reports (10-K)",
    "McDonald's Annual Reports (10-K)", "McDonald's Annual Reports (10-K)",
    # 10-Q 2014
    "McDonald's Quarterly Data (10-Q)", "McDonald's Quarterly Data (10-Q)", "McDonald's Quarterly Data (10-Q)",
    # 10-Q 2015
    "McDonald's Quarterly Data (10-Q)", "McDonald's Quarterly Data (10-Q)", "McDonald's Quarterly Data (10-Q)",
    # 10-Q 2016
    "McDonald's Quarterly Data (10-Q)", "McDonald's Quarterly Data (10-Q)", "McDonald's Quarterly Data (10-Q)",
    # 10-Q 2017
    "McDonald's Quarterly Data (10-Q)", "McDonald's Quarterly Data (10-Q)", "McDonald's Quarterly Data (10-Q)",
    # 10-Q 2018
    "McDonald's Quarterly Data (10-Q)", "McDonald's Quarterly Data (10-Q)", "McDonald's Quarterly Data (10-Q)",
    # Others
    "Consumer Price Index (CPI) by BLS", "Market Capital (2014-2018)", "Global Fast Food Market Size",
    "Assumed Growth: 2003 SARS", "Assumed Growth: 2008 Crisis"
]
    YEARS_SOURCES = [
    # 10-K
    '2014', '2015', '2016', '2017', '2018',
    # 10-Q 2014
    '2014 (Q1)', '2014 (Q2)', '2014 (Q3)',
    # 10-Q 2015
    '2015 (Q1)', '2015 (Q2)', '2015 (Q3)',
    # 10-Q 2016
    '2016 (Q1)', '2016 (Q2)', '2016 (Q3)',
    # 10-Q 2017
    '2017 (Q1)', '2017 (Q2)', '2017 (Q3)',
    # 10-Q 2018
    '2018 (Q1)', '2018 (Q2)', '2018 (Q3)',
    # Others
    'BLS CPI-U Historical', 'Stock Analysis', 'IBISWorld Global Fast Food',
    'Australian Treasury Economic Roundup', 'USDA ERS Amber Waves'
]
    LINKS = [
        # 10-K (your exact)
        'https://www.sec.gov/Archives/edgar/data/0000063908/000006390815000016/mcd-12312014x10k.htm',
        'https://www.sec.gov/Archives/edgar/data/0000063908/000006390816000103/mcd-12312015x10k.htm',
        'https://www.sec.gov/Archives/edgar/data/0000063908/000006390817000017/mcd-12312016x10k.htm',
        'https://www.sec.gov/ix?doc=/Archives/edgar/data/0000063908/000006390818000010/mcd-12312017x10k.htm',
        'https://www.sec.gov/ix?doc=/Archives/edgar/data/0000063908/000006390819000010/mcd-12312018x10k.htm',
        # 10-Q 2014
        'https://www.sec.gov/Archives/edgar/data/0000063908/000006390814000032/mcd-3312014x10q.htm',
        'https://www.sec.gov/Archives/edgar/data/0000063908/000006390814000059/mcd-6302014x10q.htm',
        'https://www.sec.gov/Archives/edgar/data/0000063908/000006390814000077/mcd-9302014x10q.htm',
        # 10-Q 2015
        'https://www.sec.gov/Archives/edgar/data/0000063908/000006390815000039/mcd-3312015x10q.htm',
        'https://www.sec.gov/Archives/edgar/data/0000063908/000006390815000065/mcd-6302015x10q.htm',
        'https://www.sec.gov/Archives/edgar/data/0000063908/000006390815000081/mcd-9302015x10q.htm',
        # 10-Q 2016
        'https://www.sec.gov/Archives/edgar/data/0000063908/000006390816000121/mcd-3312016x10q.htm',
        'https://www.sec.gov/Archives/edgar/data/0000063908/000006390816000142/mcd-6302016x10q.htm',
        'https://www.sec.gov/Archives/edgar/data/0000063908/000006390816000161/mcd-9302016x10q.htm',
        # 10-Q 2017
        'https://www.sec.gov/Archives/edgar/data/0000063908/000006390817000025/mcd-3312017x10q.htm',
        'https://www.sec.gov/ix?doc=/Archives/edgar/data/0000063908/000006390817000039/mcd-6302017x10q.htm',
        'https://www.sec.gov/ix?doc=/Archives/edgar/data/0000063908/000006390817000053/mcd-9302017x10q.htm',
        # 10-Q 2018
        'https://www.sec.gov/ix?doc=/Archives/edgar/data/0000063908/000006390818000025/mcd-3312018x10q.htm',
        'https://www.sec.gov/ix?doc=/Archives/edgar/data/0000063908/000006390818000049/mcd-6302018x10q.htm',
        'https://www.sec.gov/ix?doc=/Archives/edgar/data/0000063908/000006390818000064/mcd-9302018x10q.htm',
        # Others (your exact)
        'https://www.bls.gov/regions/mid-atlantic/data/consumerpriceindexhistorical_us_table.htm',
        'https://stockanalysis.com/stocks/mcd/market-cap/',
        '"https://www.ibisworld.com/global/market-size/global-fast-food-restaurants/1480/				"',
        'https://treasury.gov.au/publication/economic-roundup-winter-2003/the-economic-impact-of-severe-acute-respiratory-syndrome-sars',
        'https://www.ers.usda.gov/amber-waves/2015/march/recession-had-greater-impact-on-visits-to-sit-down-restaurants-than-fast-food-places/'
]
    USED_IN = [
        # 10-K 
        'Overview, Balance Sheet, CF Statement, Segment Analysis',
        'Overview, Balance Sheet, CF Statement, Segment Analysis',
        'Overview, Balance Sheet, CF Statement, Segment Analysis',
        'Overview, Balance Sheet, CF Statement, Segment Analysis',
        'Overview, Balance Sheet, CF Statement, Segment Analysis',
        # 10-Q all 
        'Quarterly Data', 'Quarterly Data', 'Quarterly Data',
        'Quarterly Data', 'Quarterly Data', 'Quarterly Data',
        'Quarterly Data', 'Quarterly Data', 'Quarterly Data',
        'Quarterly Data', 'Quarterly Data', 'Quarterly Data',
        'Quarterly Data', 'Quarterly Data', 'Quarterly Data',
        # Others 
        'Overview',
        'CF Statement',
        'Market Research',
        'Assumed Growth',
        'Assumed Growth'
]

# Assert lengths (fixed to 25)
    if not all(len(lst) == 25 for lst in [CATEGORIES, YEARS_SOURCES, LINKS, USED_IN]):
        raise ValueError("Data lists mismatched lengths")

# Build HTML rows
    rows = []
    for i in range(25):
        link_text = f"SEC {YEARS_SOURCES[i]}" if '10-K' in CATEGORIES[i] or '10-Q' in CATEGORIES[i] else YEARS_SOURCES[i].split()[0]
        row = f"""
        <tr>
            <td>{CATEGORIES[i]}</td>
            <td>{YEARS_SOURCES[i]}</td>
            <td><a href="{LINKS[i]}" target="_blank">{link_text}</a></td>
            <td>{USED_IN[i]}</td>
        </tr>"""
        rows.append(row)

    html_str = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>McDonald's References Worksheet</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 20px; }}
            table {{ border-collapse: collapse; width: 100%; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }}
            th, td {{ border: 1px solid #ddd; padding: 12px; text-align: left; }}
            th {{ background-color: #f2f2f2; font-weight: bold; }}
            tr:nth-child(even) {{ background-color: #f9f9f9; }}
            tr:hover {{ background-color: #f5f5f5; }}
            a {{ color: #0066cc; text-decoration: none; }}
            a:hover {{ text-decoration: underline; }}
            caption {{ font-size: 1.2em; margin-bottom: 10px; font-weight: bold; }}
        </style>
    </head>
    <body>
        <table>
            <caption>References Worksheet (2014-2018)</caption>
            <thead>
                <tr>
                    <th>Category</th>
                    <th>Year/Source</th>
                    <th>Link</th>
                    <th>Used in</th>
                </tr>
            </thead>
            <tbody>
    {''.join(rows)}
            </tbody>
        </table>
    </body>
    </html>
    """

    display(HTML(html_str))

if __name__ == "__main__":
    references()

# Summary

from IPython.display import Markdown, display, Code

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
McDonald’s 10-K reports and global fast-food market sizes. This comparison aims to evaluate the accuracy of the initial assumptions, examine how well 
the scenarios captured real-world impacts, completing the learning cycle of this forecast exercise.

"""
    display(Markdown(markdown_text))

# Run the function
if __name__ == "__main__":
    summary()

# Outcome Analysis

from IPython.display import HTML, display, Markdown
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
    markdown_text = """
<div style'text-align: center;">

# Outcome Analysis

</div>

"""
    display(Markdown(markdown_text))
    
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

    # Style
    dark_css = """
    <style>
    @media (prefers-color-scheme: dark) {
        table { background-color: #1e1e1e; color: #fff; }
        th { background-color: #2d2d2d; color: #fff; border-color: #444; }
        td { background-color: #1e1e1e; color: #fff; border-color: #444; }
        tr:nth-child(even) { background-color: #2d2d2d; }
        tr:hover { background-color: #333; }
        .market-header { background-color: #add8e6 !important; color: #000 !important; }
        .rev-header { background-color: #ffdab9 !important; color: #000 !important; }
        .actual-header { background-color: #f0f8ff !important; color: #000 !important; }
    }
    </style>
    """

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

    display(HTML(dark_css + styled_df.to_html(index=False)))

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

    display(HTML(dark_css + styled_err.to_html(index=True)))

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
    
    fig.show()

    markdown_text2 = """
# Outcome Analysis Summary

All monetary values—historical data (2014-2018), forecasted figures (2019-2023), and actual market size and revenue data (2019-2023) from sources—have
been adjusted to 2025 USD using CPI multipliers for precision in the error analysis. This aligns the project with current purchasing power as of March 
2025, ensuring a consistent basis for comparing projections against actual outcomes. The adjustments are documented in the “Data Reference” sheet, 
accessible via the hyperlink below, allowing for transparency while keeping the analysis focused on accuracy evaluation.

**Error Analysis** evaluates the percentage errors between the actual and projected values for global fast-food market sizes and revenues under the
Pandemic Disruption and Hindsight scenarios (with all figures adjusted to 2025 USD for consistency). The Pandemic Disruption scenario, modeled on
revenue declines from the 2003 SARS outbreak (**-10%** in 2020, **-14%** in 2021) and the 2008 financial crisis, and the Hindsight scenario, 
assuming a **2%** CAGR with annual fluctuations, share identical revenue projections across 2019-2023, resulting in an average error 
of **-0.41%** (indicating a slight underestimate). This similarity arises because both scenarios were designed to explore company-specific vulnerabilities 
during a severe disruption, with the Hindsight scenario’s fluctuations built around the same SARS/2008 revenue drops, reflecting historical variability 
rather than introducing a new revenue trend. For global market sizes, the Pandemic Disruption assumes a **1.5%** CAGR with an average error of **5.81%**, while 
the Hindsight scenario uses a **2%** CAGR with an average error of **7.41%**, reflecting the market’s actual resilience that outpaced both assumptions. 
The Baseline scenario was excluded from this error analysis, as it assumes a steady **4%** CAGR without accounting for a significant disruption like 
the COVID-19 pandemic, which did not align with the conditions observed in 2019-2023, making it less relevant for validation. These findings suggest 
the models captured the initial disruption well but underestimated the recovery.

"""
    display(Markdown(markdown_text2))

outcome_analysis()

# Data Source

from IPython.display import HTML, display, Markdown
import pandas as pd
import numpy as np

def  data_source():
    """
    Displays global fast-food market size and revenues across Nominal Data, Baseline, Pandemic Disruption, and Hindsight scenarios (2014-2023).
    All values adjusted to 2018 USD except Nominal Data. Includes CPI table and references.
    Features styled tables.
    """
    markdown_text = """
<div style="text-align: center;">

# Data Source (2014-2023)

<div style="text-align: center; font-style: normal; margin: 10px 0;">
All values in millions, adjusted to 2018 USD except Nominal Data.
</div>

</div>
"""
    display(Markdown(markdown_text))
    
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

    display(HTML(dark_css + styled_df.to_html(index=False)))

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

    display(HTML(dark_css + styled_cpi.to_html(index=False).replace('<table', '<table caption="CPI and Multiplier Data">')))

    # References Markdown
    markdown_refs = """
## References

- **2019**: [SEC 10-K](https://www.sec.gov/ix?doc=/Archives/edgar/data/0000063908/000006390820000022/mcd-12312019x10k.htm)
- **2020**: [SEC 10-K](https://www.sec.gov/ix?doc=/Archives/edgar/data/0000063908/000006390821000013/mcd-20201231.htm)
- **2021**: [SEC 10-K](https://www.sec.gov/ix?doc=/Archives/edgar/data/0000063908/000006390822000011/mcd-20211231.htm)
- **2022**: [SEC 10-K](https://www.sec.gov/ix?doc=/Archives/edgar/data/0000063908/000006390823000012/mcd-20221231.htm)
- **2023**: [SEC 10-K](https://www.sec.gov/ix?doc=/Archives/edgar/data/0000063908/000006390824000072/mcd-20231231.htm)
- **Global Market Size**: [IBISWorld](https://www.ibisworld.com/global/market-size/global-fast-food-restaurants/1480/)
- **CPI**: [BLS](https://www.bls.gov/regions/mid-atlantic/data/consumerpriceindexhistorical_us_table.htm)

"""
    display(Markdown(markdown_refs))

if __name__== "__main__":
    data_source()

# Conclusion

from IPython.display import Markdown, display, Code

def conclusion():
    """
    Replicates the 'Conclusion' worksheet from the McDonald's financial model.
    Uses Markdown for formatted text.
    
    """
    markdown_text = """
<div style="text-align: center;">

# Conclusion

<div style="text-align: left; font-style: normal; margin: 10px 0;">
    
The McDonald’s Financial Forecast Project, spanning 2014-2023, analyzed historical financial data and projected revenues under three scenarios—Baseline,
Pandemic Disruption, and Hindsight—adjusted to 2025 USD for relevance. Part 2 (Outcome Analysis)  validated these projections against actual
2019-2023 data, revealing average errors of **5.81%** for the Pandemic Disruption global market, **7.41%** for the Hindsight global market, and **-0.41%** for 
revenues in both scenarios, indicating a slight underestimate likely due to McDonald’s unmodeled resilience through delivery trends. This project 
highlights the importance of dynamic modeling in forecasting, paving the way for future improvements through advanced techniques.

**(Devopled as a self-taught exercise).**

Note: CPI multipliers are rounded to 3 decimals (following BLS practice), which can cause a small **0.03–0.04%** error due to Python’s floating-point 
precision quirks (e.g., 1.061 might read as 1.060696). I caught this and checked it out—the impact on the results is basically zero, so it's all good.
</div>

</div>
"""
    display(Markdown(markdown_text))

# Run the function
if __name__ == "__main__":
    conclusion()