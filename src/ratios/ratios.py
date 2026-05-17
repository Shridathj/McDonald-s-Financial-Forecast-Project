# Ratios

import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st

def ratio_analysis():
    """
    Displays key ratios sequentially (one section at a time) with respective interactive plots.
    Formats ratios as percentages, highlights negatives in light red. Section headers in light pink.
    Individual plotting functions for easy customization per section.
    Dual y-axis for sections with mixed scales (e.g., Cash Flow Performance: left % for OCF/Revenue, right $M for OCF-CapEx).
    All values adjusted to 2018 USD where applicable (BLS CPI-U Adjusted).
    All graphs standardized to line plots with markers. Legend positioned below graph.
    """
    st.header("Ratio Analysis Overview")

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
            return 'background-color: #F85B72' if isinstance(val, (int, float)) and val < 0 else ''
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

        return styled

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
        return fig

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
        return fig

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
        return fig

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
        return fig

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
        return fig

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
        return fig

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
        return fig

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
        return fig

    # Display text note
    st.markdown("**All ratios in percentages unless noted. Adjusted values in 2018 USD (BLS CPI-U Adjusted).**")
    st.write("")
    
    # Generate and display each section
    for section_title, data in sections.items():
        df = data['df']
        styled_table = style_table(df, section_title)
        st.write(styled_table)
        
        # Get appropriate plot based on section
        if section_title == 'Income Statement Ratios':
            fig = plot_income_statement(df)
        elif section_title == 'Balance Sheet Ratios':
            fig = plot_balance_sheet(df)
        elif section_title == 'Cash Flow Performance':
            fig = plot_cash_flow_performance(df)
        elif section_title == 'Liquidity and Solvency':
            fig = plot_liquidity_solvency(df)
        elif section_title == 'Quality of Earnings':
            fig = plot_quality_earnings(df)
        elif section_title == 'Return Ratios':
            fig = plot_return_ratios(df)
        elif section_title == 'Dividend and Sustainability':
            fig = plot_dividend_sustainability(df)
        elif section_title == 'Market Performance':
            fig = plot_market_performance(df)
        else:
            fig = None
        
        if fig:
            st.plotly_chart(fig, use_container_width=True)
        st.write("")

# Run the function
if __name__ == "__main__":
    ratio_analysis()