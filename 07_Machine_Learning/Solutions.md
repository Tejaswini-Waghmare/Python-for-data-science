# Machine Learning — Worked Solutions

These are reference approaches; compare with executed notebook outputs.

## 1. Load the customers CSV and show its shape and column types.

`pd.read_csv("data/customers_synthetic.csv")`; inspect `df.shape` and `df.dtypes`.

## 2. Count missing values and duplicate customer IDs.

`df.isna().sum()` and `df.customer_id.duplicated().sum()`; investigate before dropping records.

## 3. Calculate churn rate and explain the denominator.

`df.churned.mean()` because `churned` is 0/1; denominator is all customer rows.

## 4. Compare churn rates by plan.

`df.groupby("plan").churned.agg(["mean","count"])`; note small subgroup uncertainty.

## 5. Plot monthly spending distribution.

`df.monthly_spend.hist(bins=25)`; label the axes and state the unit.

## 6. Find the five highest-spending customers without exposing identifying information.

`df.nlargest(5,"monthly_spend")[["monthly_spend","plan"]]`; avoid customer IDs in published reports.

## 7. Create a reproducible 80/20 split.

`train_test_split(df,test_size=.2,random_state=42,stratify=df.churned)`; for unsupervised tasks split only when evaluating generalization.

## 8. Identify two ways leakage could occur.

Including target-derived fields or fitting preprocessing on the entire dataset leaks test information.

## 9. Build a simple baseline appropriate for this module.

See the runnable module notebook for a baseline; choose the simplest viable approach.

## 10. Evaluate results with at least two meaningful metrics.

For classification use recall and ROC-AUC; for regression MAE/RMSE; for retrieval hit rate. Explain denominators.

## 11. Create a visualization supporting a business question.

Use a bar chart of churn by plan or monthly sales trend; title and axis labels must name units.

## 12. Explain one misleading interpretation to avoid.

Correlation is not causation; synthetic patterns are not real-world evidence.

## 13. Test a sensitivity or alternate assumption.

Change a random seed, classification threshold, cluster count, or missingness rule; compare outputs.

## 14. Write three actionable insights grounded in the data.

Write insights after running the code, referencing exact computed values rather than inventing numbers.

## 15. List two limitations of synthetic data.

Simulated behavior may be unrealistic; no external validation exists.

## 16. Document how a teammate could reproduce the result.

Pin dependencies, keep input files and seed, document commands and expected outputs.

## 17. Stretch: add a quality gate and a failure case.

Assert uniqueness of IDs and fail when impossible values appear.

## 18. Stretch: design a monitoring plan for this workflow.

Track drift, performance, missingness, latency, and stakeholder review frequency.

