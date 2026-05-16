# Conclusion

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