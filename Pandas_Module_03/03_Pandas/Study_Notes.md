# Module 03 — Pandas for Data Science

## Learning objectives
Read and validate tabular data, clean missing values, transform features, join tables, aggregate business metrics, work with dates, and communicate analytical findings. This module uses **synthetic retail orders**, not real customer records.

## 1. Series and DataFrame
`pd.Series` is a labeled one-dimensional array. `pd.DataFrame` is a two-dimensional table with labeled rows and columns. Index labels are not guaranteed to be unique.

```python
import pandas as pd
s = pd.Series([12, 18, 24], name="sales")
df = pd.DataFrame({"product": ["A", "B"], "units": [3, 5]})
print(df.shape, df.dtypes)
```

## 2. Load and inspect
`pd.read_csv("sample_orders.csv", parse_dates=["order_date"])` parses dates while loading. Inspect `head()`, `shape`, `info()`, `describe(include="all")`, `isna().sum()`, and `duplicated().sum()` before cleaning. Always document the **grain** (one row per order here).

## 3. Select, filter, and sort
`loc` selects by labels and boolean conditions; `iloc` selects by integer position. Prefer `.loc[condition, "column"]` for assignment to avoid chained-assignment pitfalls.

```python
completed = df.loc[df["units"] >= 4, ["product", "units"]]
```

Use `query`, `isin`, `between`, `sort_values`, `nlargest`, and `drop_duplicates` when appropriate.

## 4. Missing data and validation
Missingness may be meaningful. Count it first, then decide whether to impute, exclude, or flag. In the example dataset, missing `unit_price` cannot produce a reliable revenue value, so keep a missing-price flag and exclude such rows from *known-revenue* calculations. Don't silently replace missing prices with zero.

```python
orders["price_missing"] = orders["unit_price"].isna()
orders["region"] = orders["region"].fillna("Unknown")
```

Validate nonnegative prices, quantities greater than zero, discount percentages between 0 and 1, and unique order IDs.

## 5. Type conversion and new columns
Use `pd.to_numeric(errors="coerce")`, `pd.to_datetime(errors="coerce")`, and `astype` deliberately. Create `gross_sales = quantity * unit_price` and `net_sales = gross_sales * (1 - discount_pct)`. These are **order amounts**, not profit.

## 6. GroupBy and aggregation
`groupby(..., dropna=False).agg(...)` summarizes groups. Name outputs so business meaning stays clear. Use `transform` when a group-level statistic must align with every original row.

```python
summary = orders.groupby("category").agg(order_count=("order_id", "count"))
```

## 7. Joins and relational thinking
`merge` joins datasets by keys. `validate="many_to_one"` catches unexpected duplicate customer IDs on the right; `indicator=True` helps identify unmatched orders. Check row counts before and after a join to detect accidental duplication.

## 8. Pivot tables and reshaping
`pivot_table(index="region", columns="category", values="net_sales", aggfunc="sum", fill_value=0)` makes a cross-tab. `melt` turns wide data into long data. Understand that filling a pivot output with zero is different from imputing missing underlying transactions.

## 9. Date and time operations
`dt.to_period("M")` creates monthly buckets; `resample("W")` works on a datetime index. Sort dates before rolling calculations. Beware of partial months and timezone assumptions.

## 10. Performance and reproducibility
Prefer vectorized operations over row-wise `apply` when practical. Use clear column names, deterministic data, assertions, and relative file paths. Keep raw and cleaned data separate in larger projects.

## 11. Mini case study: retail order analysis
**Business question:** Which regions and categories contribute the most known completed-order sales? **Metric definition:** sum of `quantity * unit_price * (1 - discount_pct)` for completed orders with nonmissing prices. Pending and returned orders are excluded. This is an illustrative definition; actual accounting policies vary.

**Analysis checklist:** inspect → validate → flag missing → calculate amounts → filter eligible orders → aggregate → visualize → report caveats. The notebook follows this workflow and provides a chart and exportable summary.

## 12. Common mistakes
- Using `count()` when you mean `size()` (count ignores missing values in that column).
- Forgetting join cardinality checks.
- Averaging group averages without weighting.
- Reporting revenue from pending or returned orders without defining treatment.
- Treating correlation as causation.
- Committing private customer information to a public repository.

## References
- [Pandas user guide](https://pandas.pydata.org/docs/user_guide/index.html)
- [Pandas API reference](https://pandas.pydata.org/docs/reference/index.html)
- [10 minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html)
