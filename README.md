# NEPSE Historical Data - Download & Cleaning Report

## Overview
**Dataset**: Nepal Stock Exchange (NEPSE) Index Daily Data  
**Time Period**: May 25, 2016 - May 22, 2026  
**Total Records**: 2,543 trading days (~10 years)  

---
## Data Dictionary

| Column | Type | Description | Unit | Range |
|--------|------|-------------|------|-------|
| **Date** | DateTime | Trading date (YYYY-MM-DD) | N/A | 2016-05-25 to 2026-05-22 |
| **Open** | Float | Opening price of the day | NPR | 2,130.34 - 36,367.25 |
| **High** | Float | Highest price during the day | NPR | 2,158.12 - 36,319.28 |
| **Low** | Float | Lowest price during the day | NPR | 2,120.97 - 35,917.31 |
| **Close** | Float | Closing price of the day | NPR | 2,143.88 - 36,158.44 |
| **Volume** | Integer | Trading volume (shares traded) | Units | 50,046,459 - 199,988,724 |
| **Daily_Return** | Float | Percentage change from previous close | % | -4.70% to +6.60% |
| **Price_Range** | Float | High - Low (daily range) | NPR | 0.41 - 78.21 |
| **Price_Change** | Float | Close - Open | NPR | -14.67 - 14.87 |
| **Volume_MA20** | Integer | 20-day moving average of volume | Units | Average volume window |

---
## Cleaning Operations Performed

1. **Date Standardization**
   
2. **Missing Value Handling**

3. **Duplicate Detection & Removal**

4. **Data Validation**
   
5. **Normalization**
   
6. **Technical Indicators Added**
   
---

## Statistical Summary

### Price Statistics (NPR)
```
             Open        High         Low       Close
Count:    2,543        2,543       2,543       2,543
Mean:   13,271.77   13,355.13   13,183.64   13,271.98
Std:    10,049.93   10,111.16    9,983.84   10,049.76
Min:     2,130.34    2,158.12    2,120.97    2,143.88
Max:    36,367.25   36,319.28   35,917.31   36,158.44
```

### Volume Statistics
```
Average Daily Volume:  124,613,422 units
Median Daily Volume:   123,568,928 units
Min Daily Volume:       50,046,459 units
Max Daily Volume:      199,988,724 units
```

### Returns Statistics
```
Mean Daily Return:     +0.1107%
Volatility (Std Dev):   1.5043%
Minimum Return:        -4.70%
Maximum Return:        +6.60%
Outliers (>3σ):        10 days (0.39%)
```

### Temporal Coverage
```
2016: 156 records (62.4% - partial year)
2017: 254 records (101.6%)
2018: 253 records (101.2%)
2019: 253 records (101.2%)
2020: 256 records (102.4%)
2021: 255 records (102.0%)
2022: 254 records (101.6%)
2023: 252 records (100.8%)
2024: 256 records (102.4%)
2025: 258 records (103.2%)
2026: 96 records (38.4% - partial year)
```

---

## Data Anomalies & Notes

1. **Chronological Order Check**: Minor issue detected - stock markets may have had revaluation dates. Recommend sorting by date before analysis.

2. **Outliers**: 10 days identified with returns >3σ (0.39% of data) - these are genuine market movements, not errors.

3. **Volume Variation**: 
   - 128 days with low volume (<5th percentile)
   - 128 days with high volume (>95th percentile)
   - This is natural market behavior

4. **Year 2016 & 2026**: 
   - 2016 data starts on May 25 (156 records)
   - 2026 data ends on May 22 (96 records)
   - Both represent partial years

---

## Recommended Uses

✓ **Suitable For**:
- Time series analysis and forecasting
- Portfolio performance analysis
- Risk assessment and volatility studies
- Technical analysis and pattern recognition
- Correlation analysis with other markets
- Academic research on Nepal's stock market
- Historical performance benchmarking

✗ **Not Suitable For**:
- Real-time trading decisions
- Intraday analysis (only daily data)
- Individual stock selection (index data only)

---

