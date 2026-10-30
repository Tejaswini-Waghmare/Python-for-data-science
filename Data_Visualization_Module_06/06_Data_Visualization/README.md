# Module 06 — Data Visualization & Interactive Dashboards

**Learning repository · Synthetic data · Reproducible examples**

Learn Matplotlib, Seaborn, and Plotly through a retail analytics case study. Includes a static visualization notebook, interactive Plotly notebook, standalone HTML dashboard generator, exercises, and worked solutions.

## Quick start

```bash
python -m pip install -r requirements.txt
jupyter notebook
```

Open `Examples.ipynb`, then `Interactive_Dashboard.ipynb`. Run cells top to bottom. Both notebooks read `data/retail_sales_synthetic.csv` relative to this module directory. On Google Colab, upload the CSV and change the path in the first data-loading cell to `retail_sales_synthetic.csv`.

Generate a standalone HTML dashboard from this directory:

```bash
python dashboard.py
```

Then open `outputs/retail_dashboard.html` in your browser. This dashboard has interactive Plotly charts; the notebook also demonstrates a region/category filter.

## Contents

- `Study_Notes.md`: chart selection, visual encodings, data preparation, accessibility, statistical pitfalls, and dashboard design
- `Examples.ipynb`: Matplotlib and Seaborn charts with analytical interpretation
- `Interactive_Dashboard.ipynb`: Plotly figures, KPI calculations, filtering and export
- `dashboard.py`: reproducible standalone HTML dashboard
- `Practice_Questions.md`: 18 exercises in three difficulty levels
- `Solutions.md`: reference solutions and reasoning
- `data/retail_sales_synthetic.csv`: 600 generated orders from 2025 (not real company data)

## Portfolio notes

Describe this as an **educational synthetic-data case study**, not client work. Replace the sample data with a properly licensed public dataset for a separate portfolio project. Include your own written findings and screenshots after executing the notebooks.
