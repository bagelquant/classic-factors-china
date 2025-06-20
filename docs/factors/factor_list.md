# Factor List

## Technical

### Momentum(Monthly)

Naming: `mom_<momentum_calculate_month>_<skipping_month>_<holding_period>`

Example: `mom_12_1_1`: Using t - 13 to t -1 return to calculate momentum, skiping t-1 to t month, hold from t to t+1

Test list:

- `mom_1_0_1`
- `mom_2_0_1`
- `mom_3_0_1`
- `mom_3_1_1`
- `mom_6_0_1`
- `mom_6_1_1`
- `mom_9_0_1`
- `mom_9_1_1`
- `mom_12_1_1`
- `mom_12_0_1`

### Reversal

### Low Volatility

### Turnover

## Fundamental

### Size

Details: [Size Factor](size.md)

- `circ_mv`: Free Float Market Capitalization
- `total_mv`: Total Market Capitalization
- `free_to_total_market_cap`: free float market capitalization / total market capitalization
- `ln_free_market_cap`: logarithm of Free Market Capitalization
- `ln_total_market_cap`: logarithm of Total Market Capitalization

### Value

- `bp_lr`: book (latest) / latest market capitalization
- `bp_ttm`: book (trailing twelve months) / total market capitalization
- `dp_ttm`: dividend (ttm) / total market capitalization
- `ep_lyr`: earnings (latest) / latest market capitalization
- `ep_ttm`: earnings (ttm) / total market capitalization
- `ev2ebitda`: enterprise value / EBITDA
- `fcfp_ttm`: free cash flow (ttm) / total market capitalization
- `ncfp_ttm`: net cash flow (ttm) / total market capitalization
- `ocfp_ttm`: operating cash flow (ttm) / total market capitalization
- `peg_ttm`: PEG ratio (ttm) = PE (ttm) / earnings growth rate (5 years)

### Quality(Profitability)

- `wct`: working capital turnover
- `wct_ttm`: working capital turnover (ttm) = operating revenue (ttm) / working capital (average)
- `dpr_ttm`: dividend payout ratio (ttm) = dividend (ttm) / earnings (ttm)
- `npm`: net profit margin = net profit (ttm) / operating revenue (ttm)
- `npm_ttm`: net profit margin (ttm) = net profit (ttm) / operating revenue (ttm)
- `opm`: operating profit margin = operating profit (ttm) / operating revenue (ttm)
- `opm_ttm`: operating profit margin (ttm) = operating profit (ttm) / operating revenue (ttm)
- `roa`: return on assets = net profit (ttm) / average total assets
- `roa_ttm`: return on assets (ttm) = net profit (ttm) / average total assets
- `roe`: return on equity = net profit (ttm) / average shareholders' equity
- `roe_ttm`: return on equity (ttm) = net profit (ttm) / average shareholders' equity

### Investment(Growth)

- `bpg_ttm`: equity growth per share (ttm) = (book (ttm) - book (previous year)) / shares outstanding
- `epsg_ttm`: earnings per share growth (ttm) = (earnings (ttm) - earnings (previous year)) / shares outstanding
- `npg_ttm`: net profit growth (ttm) = (net profit (ttm) - net profit (previous year)) / shares outstanding
- `ocfg_ttm`: operating cash flow growth (ttm) = (operating cash flow (ttm) - operating cash flow (previous year)) / shares outstanding
- `opg_ttm`: operating profit growth (ttm) = (operating profit (ttm) - operating profit (previous year)) / shares outstanding
- `roag_ttm`: return on assets growth (ttm) = (ROA (ttm) - ROA (previous year)) / shares outstanding
- `roeg_ttm`: return on equity growth (ttm) = (ROE (ttm) - ROE (previous year)) / shares outstanding
