# Machine Learning — Comprehensive Study Notes

**Audience:** Python learners building a practical portfolio. **Data:** all records are synthetic; results are illustrative.

## Learning objectives

### 1. Supervised vs unsupervised learning

### 2. Train/test split and leakage prevention

### 3. Linear and logistic regression

### 4. Decision trees and random forests

### 5. Feature preprocessing with pipelines

### 6. Classification metrics and confusion matrix

### 7. Cross-validation and hyperparameter tuning

### 8. K-means clustering and scaling

Supervised learning predicts a known target; unsupervised learning finds structure without labels. Use churned as a classification target and never include customer_id as a feature.

**Check yourself:** Explain when this idea is useful, a common mistake, and how you would test it.

Split before fitting preprocessing. A stratified test set preserves approximate class proportions. Keep the test set untouched until final evaluation.

**Check yourself:** Explain when this idea is useful, a common mistake, and how you would test it.

Linear regression predicts continuous values; logistic regression estimates a class probability. Logistic regression is a useful interpretable baseline.

**Check yourself:** Explain when this idea is useful, a common mistake, and how you would test it.

Trees learn threshold rules; forests average many randomized trees to reduce variance. Compare to simple baselines before claiming improvement.

**Check yourself:** Explain when this idea is useful, a common mistake, and how you would test it.

Impute missing values, scale numeric columns when appropriate, and one-hot encode categories inside a ColumnTransformer + Pipeline fitted on training data only.

**Check yourself:** Explain when this idea is useful, a common mistake, and how you would test it.

Accuracy can mislead when churn is rare. Inspect precision, recall, F1, ROC-AUC, and a confusion matrix; choose a decision threshold based on costs.

**Check yourself:** Explain when this idea is useful, a common mistake, and how you would test it.

Use StratifiedKFold on training data. GridSearchCV tunes model settings; report cross-validation performance and independent test performance separately.

**Check yourself:** Explain when this idea is useful, a common mistake, and how you would test it.

K-means groups customers by distance. Standardize numerical features, choose k with diagnostics, and interpret clusters rather than calling them true customer types.

**Check yourself:** Explain when this idea is useful, a common mistake, and how you would test it.

## Workflow checklist
1. Define the question and the unit of analysis.
2. Inspect schema, missingness, duplicates, and target leakage.
3. Build a simple baseline and keep an independent test set where relevant.
4. Create interpretable charts and explain uncertainty.
5. Record assumptions, limitations, and next actions.

## Suggested references
- pandas documentation: https://pandas.pydata.org/docs/
- scikit-learn user guide: https://scikit-learn.org/stable/user_guide.html
- Matplotlib documentation: https://matplotlib.org/stable/
