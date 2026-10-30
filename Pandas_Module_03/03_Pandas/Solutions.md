# Worked Solutions — Module 03 Pandas

Run this common setup first:

```python
import pandas as pd
orders = pd.read_csv("sample_orders.csv", parse_dates=["order_date"])
customers = pd.read_csv("sample_customers.csv", parse_dates=["signup_date"])
```

## 1. Shape
```python
print(orders.shape)
```

## 2. Missing values and duplicates
```python
print(orders.isna().sum())
print(orders["order_id"].duplicated().sum())
```

## 3. Conditional selection
```python
print(orders.loc[(orders["region"] == "East") & (orders["quantity"] >= 3)])
```

## 4. Gross sales
```python
orders["gross_sales"] = orders["quantity"] * orders["unit_price"]
print(orders[["order_id", "gross_sales"]].head())
```

## 5. Missingness policy
```python
orders["region"] = orders["region"].fillna("Unknown")
orders["price_missing"] = orders["unit_price"].isna()
```

## 6. Eligible net sales
```python
orders["net_sales"] = orders["quantity"] * orders["unit_price"] * (1 - orders["discount_pct"])
eligible = orders.loc[(orders["status"] == "Completed") & (~orders["price_missing"])].copy()
print(eligible["net_sales"].sum())
```

## 7. Category metrics
```python
print(eligible.groupby("category").agg(order_count=("order_id", "size"), total_sales=("net_sales", "sum"), avg_order_value=("net_sales", "mean")))
```

## 8. Join integrity
```python
joined = eligible.merge(customers, on="customer_id", how="left", validate="many_to_one", indicator=True)
assert len(joined) == len(eligible)
print(joined["_merge"].value_counts())
```

## 9. Pivot table
```python
print(eligible.pivot_table(index="region", columns="category", values="net_sales", aggfunc="sum", fill_value=0))
```

## 10. Monthly summary
```python
monthly = eligible.groupby(eligible["order_date"].dt.to_period("M"))["net_sales"].sum()
print(monthly)
print("Highest month:", monthly.idxmax())
```

## 11. Top customers
```python
customer_totals = joined.groupby(["customer_id", "segment"], as_index=False)["net_sales"].sum()
print(customer_totals.nlargest(3, "net_sales"))
```

## 12. Reasoning
Missing prices set to zero understate sales and conceal data-quality problems. An unchecked many-to-many join can multiply rows and inflate totals. Always inspect and validate keys.

## 13. Plot and save
```python
import matplotlib.pyplot as plt
region = eligible.groupby("region")["net_sales"].sum().sort_values(ascending=False)
ax = region.plot.bar(title="Known completed-order sales by region")
ax.set_ylabel("Sales ($)")
plt.tight_layout()
plt.savefig("region_sales.png", dpi=150)
plt.show()
```

## 14. Validation
```python
assert orders["discount_pct"].between(0, 1).all()
assert orders["order_id"].is_unique
```

## 15. Sensitivity analysis
```python
known_price = orders.loc[~orders["price_missing"]]
with_pending = known_price.loc[known_price["status"].isin(["Completed", "Pending"]), "net_sales"].sum()
completed_only = eligible["net_sales"].sum()
print("Including pending:", with_pending, "Completed only:", completed_only)
```
The difference is attributable to pending orders, which may not represent recognized sales.
