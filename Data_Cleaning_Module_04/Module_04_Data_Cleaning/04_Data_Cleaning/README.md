# Module 04 — Data Cleaning & Preprocessing

**Level:** Beginner → Intermediate | **Tools:** Python, pandas, NumPy, scikit-learn, matplotlib

## Objective
Build a reproducible data-quality pipeline for a **synthetic financial-transactions dataset**. Detect missing values, inconsistent labels, invalid dates, duplicates, suspicious amounts, and potential identifier conflicts; preserve an audit trail; and prepare features without data leakage.

## Files
- `Study_Notes.md` — detailed conceptual guide and practical examples
- `Examples.ipynb` — runnable end-to-end analysis, cleaning, validation and export
- `Practice_Questions.md` — 15 graduated exercises
- `Solutions.md` — reference solutions and reasoning
- `data/messy_transactions.csv` — intentionally flawed, synthetic input (82 rows)
- `requirements.txt` — dependencies

## Run in Colab
1. Upload `Examples.ipynb` to Google Colab.
2. Upload `data/messy_transactions.csv` to Colab's file pane (top-level is fine).
3. Run all cells; notebook searches both `data/` and current directory.
4. Download generated outputs from `outputs/`.

## Data ethics
All customers and transactions are **fictional**. Do not interpret synthetic examples as real fraud or business findings. Cleaning rules are documented assumptions and should be revised for actual business requirements.

## Learning outcomes
Profile a dataset; define a data-quality contract; separate invalid records from valid records; normalize categories; identify exact and conflicting duplicates; use robust outlier flags; prevent train/test leakage; export a clean dataset and quality report.
