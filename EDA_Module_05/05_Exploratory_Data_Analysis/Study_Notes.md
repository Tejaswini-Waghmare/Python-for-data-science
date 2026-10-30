# Module 5 — Exploratory Data Analysis (EDA)

## Learning objectives
Explain dataset grain, audit missingness and duplicates, describe distributions, compare groups, investigate relationships, visualize responsibly, and write actionable findings with limitations.

## 1. EDA workflow
1. **Frame the question:** Which regions, channels and categories drive revenue? How does delivery speed relate to satisfaction?
2. **Understand grain:** One row represents one synthetic order. `order_id` should be unique.
3. **Audit quality:** Inspect dtypes, null counts, duplicate IDs, impossible values, date coverage and outliers before interpretation.
4. **Univariate analysis:** Frequency tables, mean/median, quantiles, IQR, histogram and boxplot. Skewed sales often require median alongside mean.
5. **Bivariate analysis:** Compare revenue by category, channel and region; scatter delivery time versus satisfaction; compare numerical correlations.
6. **Multivariate checks:** Segment region by channel; inspect whether overall patterns differ within groups.
7. **Communicate:** Distinguish descriptive findings from causal claims, report sample size and uncertainty, and identify next analyses.

## 2. Key definitions
- **Mean:** Sum divided by count; sensitive to extreme values.
- **Median:** Middle observation; robust to skew.
- **Standard deviation:** Spread around the mean.
- **Quantile:** Cutoff below which a fraction of observations fall.
- **IQR:** Q3 − Q1; common outlier screening rule flags below Q1 − 1.5×IQR or above Q3 + 1.5×IQR.
- **Correlation:** Strength and direction of linear association (Pearson); not evidence of causation.
- **Missingness:** Missing completely at random, at random conditional on observed values, or not at random; diagnose before imputing.

## 3. Data dictionary
| Column | Meaning |
|---|---|
| order_id | Unique order identifier |
| order_date | Date of order |
| region | Sales region (some values missing) |
| channel | Online, Store or Partner |
| category | Product category |
| quantity | Items purchased |
| unit_price | Price per item; one deliberate high outlier |
| discount_rate | Fractional discount, e.g. 0.10 |
| customer_satisfaction | 1–5 rating, some missing |
| delivery_days | Delivery time in days |

**Derived metric:** `revenue = quantity * unit_price * (1 - discount_rate)`. This is a simplified order-level revenue proxy; excludes tax, refunds, shipping and returns.

## 4. Missing values and anomalies
Count missing values both as counts and percentages. Do not fill missing satisfaction with zero (zero is not on the rating scale). Keep missing region as `Unknown` for grouping only if explicitly labeled. An unusually high unit price should be investigated, not automatically deleted.

## 5. Charts and when to use them
- Histogram: numeric distribution, skew and possible multimodality.
- Boxplot: medians, quartiles and potential outliers by category.
- Bar chart: category totals; use a zero baseline.
- Scatterplot: two numeric variables, possible nonlinear relationships.
- Correlation heatmap: exploratory overview; correlated engineered variables can be redundant.
- Time series: daily or monthly trend; incomplete periods may mislead.

## 6. Common mistakes
- Comparing totals across unequal sample sizes without considering per-order averages.
- Treating correlations as causal effects.
- Using averages alone for heavily skewed revenue.
- Treating the synthetic data as a real company's performance.
- Interpreting charts before checking data quality.
- Claiming statistical significance without a suitable test and assumptions.

## 7. Reproducibility
Install dependencies using `pip install -r requirements.txt`. Run the notebook from the module folder, or upload the CSV to Colab and set `DATA_PATH` appropriately. The notebook creates charts in `outputs/`.

## 8. Further reading
- [pandas user guide](https://pandas.pydata.org/docs/user_guide/index.html)
- [Matplotlib tutorials](https://matplotlib.org/stable/tutorials/index.html)
- [Seaborn tutorial](https://seaborn.pydata.org/tutorial.html)
- [NIST Exploratory Data Analysis](https://www.itl.nist.gov/div898/handbook/eda/eda.htm)

**Dataset provenance:** Entirely synthetic, generated with a fixed random seed for educational use. Not customer data.
