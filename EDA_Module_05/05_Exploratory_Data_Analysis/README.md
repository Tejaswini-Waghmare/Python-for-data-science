# 05 — Exploratory Data Analysis

An original, reproducible study module using **synthetic retail orders**, not real customer data.

## Contents
- `Study_Notes.md` — concepts, methodology and pitfalls
- `Examples.ipynb` — executable EDA with charts and summaries
- `Practice_Questions.md` — 16 exercises and a challenge
- `Solutions.md` — worked Python solutions
- `data/retail_orders_synthetic.csv` — 360 synthetic orders with intentional missingness and a high-price outlier
- `requirements.txt` — dependencies

## Run locally
```bash
python -m pip install -r requirements.txt
jupyter notebook Examples.ipynb
```

## Run in Colab
Upload the notebook **and** `data/retail_orders_synthetic.csv` to Colab. Upload the CSV at the session root; the notebook automatically checks both paths. Run all cells.

## Learning outcomes
Data audit, distribution analysis, group comparisons, correlations, time series, visual communication and careful interpretation.

**Integrity:** Educational synthetic data; findings are illustrative, not evidence about an actual retailer.
