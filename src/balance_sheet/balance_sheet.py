# Balance Sheet

import importlib
import pandas as pd
px = None
try:
    px = importlib.import_module("plotly.express")
except ImportError:
    px = None
import numpy as np

import importlib
try:
    ipy_display = importlib.import_module("IPython.display")
    HTML = ipy_display.HTML
    Markdown = ipy_display.Markdown
    display = ipy_display.display
except ModuleNotFoundError:
    def HTML(value):
        return value

    def Markdown(value):
        return value

    display = print

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
    if px is not None:
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
    else:
        display(Markdown("**Plotly is not installed. Skipping ratio chart display.**"))

# Run the function
if __name__ == "__main__":
    balance_sheet()