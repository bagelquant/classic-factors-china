# Size Factor

- `circ_mv`: Free Float Market Capitalization
- `total_mv`: Total Market Capitalization
- `free_to_total_market_cap`: free float market capitalization / total market capitalization
- `ln_free_market_cap`: logarithm of Free Market Capitalization
- `ln_total_market_cap`: logarithm of Total Market Capitalization

## All Required Data For Size Factor

All required data from tushare database: 

- `daily_basic`
  - `circ_mv`: Free Float Market Capitalization
  - `total_mv`: Total Market Capitalization
 
## Factor Definitions

### Free Float Market Capitalization (`circ_mv`)

Free Float Market Capitalization is the market capitalization of a company's publicly traded shares, 
excluding closely held shares. 

Required Data:

- `daily_basic.circ_mv`: Free Float Market Capitalization


### Total Market Capitalization (`total_mv`)

Total Market Capitalization is the total market value of a company's outstanding shares,
including both publicly traded and closely held shares.

Required Data:

- `daily_basic.total_mv`: Total Market Capitalization

### Free to Total Market Capitalization Ratio (`free_to_total_market_cap`)

The Free to Total Market Capitalization Ratio is the ratio of Free Float Market Capitalization to Total Market Capitalization.

Required Data:

- `daily_basic.circ_mv`: Free Float Market Capitalization
- `daily_basic.total_mv`: Total Market Capitalization

### Logarithm of Free Market Capitalization (`ln_free_market_cap`)

The Logarithm of Free Market Capitalization is the natural logarithm of Free Float Market Capitalization.

Required Data:

- `daily_basic.circ_mv`: Free Float Market Capitalization

### Logarithm of Total Market Capitalization (`ln_total_market_cap`)

The Logarithm of Total Market Capitalization is the natural logarithm of Total Market Capitalization.

Required Data:

- `daily_basic.total_mv`: Total Market Capitalization

