import pandas as pd
df = pd.DataFrame({"category": ["Food", "Travel", "Food", "Rent"], "amount": [25, 40, 15, 900]})
print(df.isna().sum())
print(df.groupby("category", as_index=False)["amount"].agg(["sum", "mean"]))
