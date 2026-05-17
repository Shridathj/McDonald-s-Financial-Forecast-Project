# Income overview

import streamlit as st
import pandas as pd
import plotly.express as px

def overview():
    """
    Replicates the 'Overview' worksheet from a financial model with transposed tables (metrics in rows, years in columns).
    Adjusts unadjusted values to 2018 USD using CPI multipliers, formats monetary values in US format,
    ratios in percentages, and highlights negatives in light red. CAGR and ratio cells are highlighted in blue.
    Adds a table for key ratios and generates an interactive bar chart.
    """
    st.header("Income Sheet Overview")

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
            'background-color': "#F85B72"
        }, subset=pd.IndexSlice[df['Metric'].isin(metrics_headers), :])

        # Apply normal and left-aligned text to subsection headers
        styled_df = styled_df.set_properties(**{
            'font-weight': 'normal',
            'text-align': 'left',
            'background-color': '#1A1A1A' # Light Gray
        }, subset=pd.IndexSlice[df['Metric'].isin(submetrics_headers), :])

        # Apply blue highlighting to ratio rows and CAGR column
        styled_df = styled_df.set_properties(**{'background-color': "#67c0ff"}, subset=pd.IndexSlice[df['Metric'].isin(ratio_metrics), :])
        styled_df = styled_df.set_properties(**{'background-color': '#67c0ff'}, subset=pd.IndexSlice[:, 'CAGR'])

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

    # Display the tables in the output
    st.markdown("**All values in 2018 USD (BLS CPI-U Adjusted)**")
    st.markdown("**In millions, except share data (10-K)**")
    st.write(styled_adjusted)
    st.write(styled_unadjusted)
    st.write(styled_key_ratios)
    st.write(styled_cpi)
    st.markdown("[CPI Data Source: BLS CPI Data](https://www.bls.gov/regions/mid-atlantic/data/consumerpriceindexhistorical_us_table.htm)")

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
    st.plotly_chart(fig, use_container_width=True)

# Run the function
if __name__ == "__main__":
    overview()