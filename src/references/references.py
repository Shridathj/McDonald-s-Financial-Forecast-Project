# References

import streamlit as st
import pandas as pd

def references():
    st.header("References")

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
        'https://www.ibisworld.com/global/market-size/global-fast-food-restaurants/1480/',
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

    # Build DataFrame for references table
    df_refs = pd.DataFrame({
        'Category': CATEGORIES,
        'Year/Source': YEARS_SOURCES,
        'Used in': USED_IN
    })
    # Display table with links as markdown in the display
    st.dataframe(df_refs, use_container_width=True)
    st.markdown("### Reference Links")
    for i, link in enumerate(LINKS):
        st.markdown(f"- **{YEARS_SOURCES[i]}**: [{CATEGORIES[i]}]({link})")

if __name__ == "__main__":
    references()
