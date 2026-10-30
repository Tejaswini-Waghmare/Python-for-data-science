# Data Cleaning & Preprocessing — Study Notes

## 1. Why data cleaning matters
Models and dashboards inherit the errors in their input data. Common issues: missing values, duplicate records, mixed types, impossible values, inconsistent categories, invalid dates, and leakage. **Never overwrite raw data**; store clean outputs separately and document each decision.

## 2. Data quality dimensions
| Dimension | Question | Example check |
|---|---|---|
| Completeness | Are required fields present? | `df.isna().mean()` |
| Validity | Does each value follow business rules? | `amount > 0` for a purchase |
| Uniqueness | Is the record key unique? | `duplicated('transaction_id')` |
| Consistency | Are representations standardized? | `completed` vs `Completed` |
| Accuracy | Does data match reality? | Needs trusted reference data |
| Timeliness | Is data sufficiently recent? | Compare event and ingestion dates |

## 3. Profiling before changing anything
```python
import pandas as pd
df = pd.read_csv('data/messy_transactions.csv', dtype=str)
print(df.shape)
print(df.isna().sum())
print(df.nunique(dropna=False))
```
Reading as strings preserves malformed values until they can be audited.

## 4. Missingness and imputation
Missing Completely At Random (MCAR), Missing At Random (MAR), and Missing Not At Random (MNAR) require different reasoning. Missing identifiers usually require quarantine, not guessing. Numerical features can use median imputation **fitted on training data only**. Categorical features may use an explicit `Unknown` label where appropriate.

```python
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
X_train, X_test = train_test_split(features, test_size=0.2, random_state=42)
imputer = SimpleImputer(strategy='median').fit(X_train)
X_train_ready = imputer.transform(X_train)
X_test_ready = imputer.transform(X_test)
```

## 5. Data types and parsing
Use `pd.to_numeric(..., errors='coerce')` to reveal invalid numbers; first remove formatting such as commas. Use `pd.to_datetime(..., errors='coerce')` with a **documented date convention**. Ambiguous dates (e.g., 05/09/2026) should not be silently interpreted without source-system context.

## 6. Standardizing text
Trim whitespace, normalize case, and map known aliases through a dictionary. Preserve original raw values for audits.

```python
status = df['payment_status'].str.strip().str.casefold()
status = status.replace({'complete':'completed'})
```

## 7. Duplicates: exact vs conflicting
- **Exact duplicate:** every field matches; often safe to remove after verifying ingestion semantics.
- **Conflicting identifier:** same transaction ID with different data; quarantine for investigation rather than keeping the first arbitrarily.
- **Legitimate repeat:** same customer and amount may represent separate purchases; do not deduplicate by those columns alone.

## 8. Outliers vs errors
IQR fences and robust z-scores identify unusual values; they **do not prove** errors or fraud. In this tutorial, amounts over $10,000 are flagged for review, not silently dropped. Negative purchases violate this example's purchase-only contract, but refunds may be valid in a different dataset.

## 9. Validation and quarantine
Define required fields, accepted statuses, valid dates, amount range, and key uniqueness. Output a clean table and a quarantine table with a reason per record. Record counts must reconcile: `raw = clean + quarantined + exact_duplicates_removed` (with explicit precedence).

## 10. Feature engineering without leakage
Create month, weekday, log amount, and customer transaction count **only when allowed by the prediction time**. For supervised models, split before fitting imputers, encoders, or scalers; time-based splits may be preferable for transactions. Never use future outcomes to construct predictors.

## 11. Privacy and reproducibility
Avoid committing personal data, API keys, or proprietary datasets. Use fictional or approved public data. Fix random seeds, pin dependencies for production, document assumptions, and keep raw/clean outputs separate.

## 12. Mini case study
A fictional payments team receives transactions with blank IDs, malformed dates, inconsistent statuses, duplicates, and extreme values. The notebook creates a data-quality report, normalizes valid fields, quarantines ambiguous rows, and exports a reproducible clean dataset. This is a **data quality** exercise, not a fraud detection model.

## References
- [pandas missing data](https://pandas.pydata.org/docs/user_guide/missing_data.html)
- [pandas duplicate handling](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.duplicated.html)
- [scikit-learn common pitfalls](https://scikit-learn.org/stable/common_pitfalls.html)
- [scikit-learn preprocessing](https://scikit-learn.org/stable/modules/preprocessing.html)
