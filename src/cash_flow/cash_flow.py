# Cash Flow Statement

import streamlit as st  
import pandas as pd
import numpy as np

def cash_flow_statement():
    """
    Replicates the 'CF Statement' worksheet from a financial model.
    Adjusts unadjusted values to 2018 USD using CPI multipliers, formats monetary values in US format,
    ratios in percentages, and highlights negatives in light red. Ratio cells are highlighted in blue.
    Displays Adjusted, Unadjusted, Key Ratios, and CPI tables, with an interactive bar chart for key ratios.
    """
    st.header("Cash Flow Statement Overview")

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
            'background-color': '#F85B72' # Light Pink
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
        styled_df = styled_df.set_properties(**{'background-color': '#67c0ff'}, subset=pd.IndexSlice[df['Metrics'].isin(ratio_metrics + ocf_capex), df.columns[1:]])

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
            {'selector': 'th', 'props': [('text-align', 'center'), ('background-color', '#666565'), ('border', '1px solid black'), ('font-weight', 'bold'), ('padding', '5px')]},
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

    # Display the tables
    st.markdown("**All values in 2018 USD (BLS CPI-U Adjusted)**")
    st.markdown("**In millions (10-K)**")
    st.write(styled_adjusted)
    st.markdown("**CPI Adjustment Note:** Monetary values have been CPI-adjusted to reflect real purchasing power. This ensures consistency in economic analysis across years. Minor rounding differences (0.03–0.04%) may occur due to CPI multiplier precision, as noted in the Excel file, but these have negligible impact.")
    st.write(styled_unadjusted)
    st.write(styled_key_ratios)
    st.write(styled_cpi)
    st.markdown("[CPI Data Source: BLS CPI Data](https://www.bls.gov/regions/mid-atlantic/data/consumerpriceindexhistorical_us_table.htm)")

# Run the function
if __name__ == "__main__":
    cash_flow_statement()