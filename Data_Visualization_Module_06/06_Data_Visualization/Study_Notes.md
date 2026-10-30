# Data Visualization — Comprehensive Study Notes

## 1. What visualization is for
Visualization helps **compare**, **track change**, **show distribution**, **show relationships**, and **communicate uncertainty**. Start with a business question, identify the unit of analysis, then select a chart. Avoid choosing a chart solely because it looks attractive.

## 2. Libraries
- **Matplotlib**: granular static charts, publication-quality figures; `fig, ax = plt.subplots()`; label axes and use `plt.tight_layout()`.
- **Seaborn**: statistical plots integrated with pandas, such as `sns.boxplot`, `sns.histplot`, `sns.scatterplot`, `sns.heatmap`.
- **Plotly Express**: interactive charts with hover, legend selection and zoom; `px.bar`, `px.line`, `px.scatter`, `px.imshow`.

## 3. Data grain and aggregation
Each row in the dataset is one order. Summing `revenue` by `category` yields category revenue. Averaging individual order revenue is **not** the same as averaging daily revenue. Choose the grain explicitly.

```python
import pandas as pd
df = pd.read_csv('data/retail_sales_synthetic.csv', parse_dates=['order_date'])
category_revenue = df.groupby('category', as_index=False)['revenue'].sum()
```

## 4. Chart selection
| Question | Recommended chart | Watch out for |
|---|---|---|
| Compare category totals | Sorted horizontal bar | Truncated bar axis |
| Trend over time | Line | Irregular time gaps |
| Shape of order values | Histogram | Bin size changes appearance |
| Outliers across segments | Boxplot | Small sample groups |
| Revenue vs profit | Scatter | Correlation ≠ causation |
| Correlation matrix | Heatmap | Spurious correlations and scale |
| Share of total | Bar or 100% stacked bar | Too many categories |

## 5. Descriptive statistics and uncertainty
- Mean is sensitive to extreme observations; median is robust.
- A boxplot shows median, quartiles and potential outliers; outliers are not automatically errors.
- Correlation measures association, not cause. For comparisons, show sample sizes and consider confidence intervals when applicable.
- Do not imply synthetic data validates real-world hypotheses.

## 6. Matplotlib patterns
```python
fig, ax = plt.subplots(figsize=(8, 4))
ax.bar(category_revenue['category'], category_revenue['revenue'])
ax.set(title='Revenue by category', ylabel='Revenue (USD)', xlabel='Category')
fig.tight_layout()
```

## 7. Seaborn patterns
```python
import seaborn as sns
sns.boxplot(data=df, x='region', y='revenue')
```
Compare distributions, not just averages. Order groups meaningfully.

## 8. Plotly patterns
```python
import plotly.express as px
fig = px.line(df.groupby('order_date', as_index=False)['revenue'].sum(),
              x='order_date', y='revenue', title='Daily revenue')
fig.show()
```
Hover reveals details, but the title, axes and units must still be self-explanatory.

## 9. Dashboard design
1. Define audience and decision.
2. Put 3–5 KPI cards at the top (revenue, profit, orders, margin).
3. Provide explicit filters (region, category, date).
4. Include a trend and a segment comparison.
5. Explain definitions and limitations; add a timestamp and source.
6. Validate KPI totals before polishing visual design.

**KPI definitions:** `revenue = sum(revenue)`, `profit = sum(profit)`, `orders = count(order_id)`, `profit_margin = profit/revenue` when revenue is nonzero. Margin is **not** the unweighted average of row margins.

## 10. Accessibility and ethics
Use descriptive chart titles, readable contrast, consistent units, and text labels when possible. Avoid 3D charts, misleading axis ranges, inappropriate dual axes, and selective date windows. Never use color as the only encoding for a critical distinction.

## 11. Common mistakes
- Plotting unsorted dates in a line chart.
- Treating missing data as zero without justification.
- Using pie charts with many slices.
- Showing totals without denominators or group sizes.
- Using an unweighted average of percentages.
- Calling a correlation a causal effect.

## 12. References
- [Matplotlib tutorials](https://matplotlib.org/stable/tutorials/index.html)
- [Seaborn tutorial](https://seaborn.pydata.org/tutorial.html)
- [Plotly Python](https://plotly.com/python/)
- [Pandas groupby](https://pandas.pydata.org/docs/user_guide/groupby.html)
