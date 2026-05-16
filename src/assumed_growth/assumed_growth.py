# Assumed Growth

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