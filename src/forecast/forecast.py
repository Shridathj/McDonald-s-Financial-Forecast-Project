# Forecast

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st

def forecast():
    """
    Generates transposed tables for the Baseline Growth and Pandemic Disruption scenarios, 
    and two separate line graphs for Market Size & Adjusted Revenue comparisons.
    """
    markdown_text = """

# Forecast

"""
    st.markdown(markdown_text)

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
    st.write("")
    st.markdown(styled_baseline_assump.to_html(), unsafe_allow_html=True)
    st.write("")
    st.markdown(styled_baseline_table.to_html(), unsafe_allow_html=True)
    st.write("")
    st.markdown(styled_pandemic_assump.to_html(), unsafe_allow_html=True)
    st.write("")
    st.markdown(styled_pandemic_table.to_html(), unsafe_allow_html=True)
    st.write("")

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
    st.plotly_chart(fig1, use_container_width=True)

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
    st.plotly_chart(fig2, use_container_width=True)

# Run the function
if __name__ == "__main__":
    forecast()