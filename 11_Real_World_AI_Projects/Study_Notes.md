# Real-World AI Projects — Comprehensive Study Notes

**Audience:** Python learners building a practical portfolio. **Data:** all records are synthetic; results are illustrative.

## Learning objectives

### 1. Define a stakeholder problem

### 2. Business metrics and baseline

### 3. Data validation and feature engineering

### 4. Train and evaluate a predictive model

### 5. Segment customers for interventions

### 6. Create a lightweight dashboard

### 7. Write limitations and deployment plan

### 8. Document reproducibility and portfolio presentation

State the business decision and intended user. For this capstone: which customers merit a retention review?

**Check yourself:** Explain when this idea is useful, a common mistake, and how you would test it.

Define churn prevalence, baseline model, false-positive cost, and recall. A dashboard should make metrics understandable.

**Check yourself:** Explain when this idea is useful, a common mistake, and how you would test it.

Validate IDs, types, missingness, and target leakage. Keep transformations reproducible inside a training pipeline.

**Check yourself:** Explain when this idea is useful, a common mistake, and how you would test it.

Train a simple model and compare against a dummy baseline. Evaluate with a held-out test set and document threshold assumptions.

**Check yourself:** Explain when this idea is useful, a common mistake, and how you would test it.

Use segments only as hypotheses for investigation; clustering labels are not causal or demographic truths.

**Check yourself:** Explain when this idea is useful, a common mistake, and how you would test it.

Provide a filterable HTML dashboard and clear KPI definitions. Visual polish cannot substitute for reliable metrics.

**Check yourself:** Explain when this idea is useful, a common mistake, and how you would test it.

List synthetic-data limitations, monitoring, fairness checks, retraining triggers, and approval steps before deployment.

**Check yourself:** Explain when this idea is useful, a common mistake, and how you would test it.

Include README, dataset provenance, instructions, evidence screenshots, limitations, and specific contributions.

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
