# Methodology

## Overview

This document outlines the methodology used in our project, including the data collection, analysis techniques. 
This project systematically analyzes the performance of classic investment factors in the China A-share market.

Factor models are a widely used tool in finance to explain the returns of a portfolio or an asset. They are based on 
the idea that the returns of an asset can be explained by its exposure to certain risk factors. We could write the 
relationship between the returns of an asset and its exposure to risk factors as follows (linear relationship assumed):

$$
E(r_i) = \alpha + \beta_1 \lambda_1 + \beta_2 \lambda_2 + ... + \beta_n \lambda_n
$$

Where:

- $E(r_i)$ is the expected return of asset $i$.
- $\alpha$ is the intercept term.
- $\beta_n$ is the sensitivity of asset $i$ to factor $n$. (Factor loading)
- $\lambda_n$ is the risk premium of factor $n$. (Factor return)

This project focuses on the following classic investment factors:

- Market Beta
- Momentum
- Reversal
- Low Volatility
- Turnover
- Size
- Value
- Quality
- Investment

Details of factors please refer to the [factor_list.md](factors/factor_list.md) file.

More information about the factor models can be found in my personal blog: [Factor Models](https://bagelquant.com/factor-models/).

## Analysis Framework and Process

1. **Sample Selection**: 
   - Select stocks listed on the Main Board of the Shanghai and Shenzhen Stock Exchanges.
   - Exclude stocks with a market capitalization below 100 million RMB.
   - Exclude stocks with less than 6 months of trading history.
   - ST stocks and *ST stocks are also excluded.
2. **Data Pre-processing**:
   - Missing
   - Outliers
   - Special treatments
3. **Single Factor Analysis**
    - Return significance test: t-test
    - Monotonic relationship test: IC, ICIR
    - Stability test: Rolling IC, Rolling ICIR
4. **Tradable Factor Model Based Portfolio**
    - Factor correlation analysis
    - Returns and covariance matrix prediction
    - Residual risk analysis
    - Optimized portfolio construction
5. **Classical Factor Models**
    - Fama-French 3-Factor Model (1993)
    - Carhart 4-Factor Model (1997)
    - Novy-Marx 4-Factor Model (2013)
    - Fama-French 5-Factor Model (2015)
    - Hou-Xue-Zhang 4-Factor Model (2015)
    - Stambaugh-Yuan 4-Factor Model (2017)
    - Hou-Xue-Zhang 5-Factor Model (2019)
    - Daniel-Hirshleifer-Sun 3-Factor Model (2020)

