# Project Proposal – Classic Factors in China A-Share Market

> 中文文档: [docs/proposal_cn.md](proposal_cn.md)

This project aims to systematically analyze the performance of classic investment factors in the China A-share market. The analysis will cover:

- **Single Factor Analysis**: Factors include:
  - **Market Factors**
    - Beta
  - **Technical Factors**
    - Momentum
    - Reversal
    - Low Volatility
    - Turnover
  - **Fundamental Factors**
    - Size
    - Value
    - Quality
    - Investment
    - Profitability
- **Classical Factor Models**:
  - Fama-French 3-Factor Model (1993)
  - Carhart 4-Factor Model (1997)
  - Novy-Marx 4-Factor Model (2013)
  - Fama-French 5-Factor Model (2015)
  - Hou-Xue-Zhang 4-Factor Model (2015)
  - Stambaugh-Yuan 4-Factor Model (2017)
  - Hou-Xue-Zhang 5-Factor Model (2019)
  - Daniel-Hirshleifer-Sun 3-Factor Model (2020)

## Data Sources

- **Tushare**: A comprehensive data provider for Chinese financial markets, offering stock prices, financial statements, and other market data.

Data will be retrieved using the [Tushare API](https://tushare.pro) and stored in a local MySQL database via the [bagel-tushare](https://github.com/bagelquant/bagel-tushare) package. For simplicity, this project will extract data from the local MySQL database and save it as CSV files in the `data/` directory. All analyses will be performed using these CSV files.

## Factor Construction

- **Stock Universe**
  - All Main Board stocks listed on the Shanghai and Shenzhen Stock Exchanges (主板)
  - Exclude stocks with a market capitalization below 100 million RMB
  - Exclude stocks with less than 6 months of trading history
- **Construction Methods (Single Factor Analysis)**
  - Sorting: Divide stocks into 10 groups; the long-short portfolio is constructed as group 10 minus group 1
  - Cross-sectional regression
- For classical factor models, the construction methods will follow the original papers.

> [!NOTE]
> Reasons for only including stocks listed on the Main Board is to ensure all stocks are investable for individual
> investors. Stocks listed on the SME Board and ChiNext Board are often subject to stricter trading restrictions,
> which may not be suitable for small size portfolios.

## Reporting and Visualization

Interactive reporting and visualization will be implemented using Streamlit. The report will include:

- Single Factor Analysis
- Classical Factor Models

## Structure

The project will be structured as follows:

```plaintext
project_root/
├── data/                  # Directory for CSV files
├── docs/                  # Documentation files
├── src/                   # Source code for data processing and analysis
│   ├── database/          # Database access and management module
│   ├── analysis/          # Factor analysis and model implementation module
│   └── streamlit_pages/   # Streamlit page definitions and UI logic
├── tests/                 # Unit tests for the source code
├── reports/               # Generated reports and visualizations
├── requirements.txt       # Python package dependencies
├── README.md              # Project overview and setup instructions
├── config.json            # Database configuration file (Exclude from Git)
├── update_data.py         # Script to extract data from database and save as CSV files
├── main.py                # Main script to run the analysis
└── streamlit_app.py       # Streamlit application for interactive reporting
```
