# Segment Analysis

import pandas as pd
import numpy as np
import plotly.graph_objects as go
import streamlit as st

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