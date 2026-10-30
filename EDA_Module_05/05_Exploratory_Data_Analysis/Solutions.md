# Module 5 — Worked Solutions

Start with:
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("data/retail_orders_synthetic.csv",parse_dates=["order_date"])
df["revenue"]=df.quantity*df.unit_price*(1-df.discount_rate)
```

## 1. Inspect row count, columns and types.

```python
df.shape; df.dtypes
```

## 2. Count missing values and compute percentages.

```python
df.isna().sum(); df.isna().mean()*100
```

## 3. Verify unique order IDs and report date coverage.

```python
df.order_id.duplicated().sum(); (df.order_date.min(),df.order_date.max())
```

## 4. Calculate revenue proxy per order.

```python
df["revenue"]=df.quantity*df.unit_price*(1-df.discount_rate)
```

## 5. Find mean, median, standard deviation and 90th percentile of revenue.

```python
df.revenue.agg(["mean","median","std"]);df.revenue.quantile(.9)
```

## 6. Flag high revenue outliers using 1.5×IQR.

```python
q1,q3=df.revenue.quantile([.25,.75]);df[df.revenue>q3+1.5*(q3-q1)]
```

## 7. Compute total revenue by category.

```python
df.groupby("category").revenue.sum().sort_values(ascending=False)
```

## 8. Compute average revenue per order by channel.

```python
df.groupby("channel").revenue.mean()
```

## 9. Compare order counts by region including missing region.

```python
df.region.value_counts(dropna=False)
```

## 10. Create a histogram of revenue and explain skew.

```python
sns.histplot(df.revenue,bins=30);plt.show()
```

## 11. Create a boxplot of unit price by category.

```python
sns.boxplot(data=df,x="category",y="unit_price");plt.show()
```

## 12. Plot weekly revenue and describe possible fluctuations.

```python
df.set_index("order_date").resample("W").revenue.sum().plot();plt.show()
```

## 13. Compare median satisfaction across delivery-day groups.

```python
df.groupby("delivery_days").customer_satisfaction.median()
```

## 14. Compute correlation between delivery days and satisfaction; explain its limitation.

```python
df[["delivery_days","customer_satisfaction"]].corr().iloc[0,1] # association only
```

## 15. Create a region × channel pivot of mean revenue.

```python
df.pivot_table(index="region",columns="channel",values="revenue",aggfunc="mean")
```

## 16. Write three evidence-backed findings and two limitations.

```python
Use actual values from your notebook. Mention synthetic sampling and missingness.
```

### Challenge discussion
The mean is sensitive to extreme prices. Check the source record and unit conventions; compare median, trimmed mean, and plots before deciding whether the value is an error.
