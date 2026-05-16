# Home

import importlib
import pandas as pd

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
if __name__ == "__main__":
    home()