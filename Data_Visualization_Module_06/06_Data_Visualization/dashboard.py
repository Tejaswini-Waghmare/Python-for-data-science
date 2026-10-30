'''Generate a self-contained Plotly HTML dashboard from the synthetic dataset.'''
from pathlib import Path
import pandas as pd
import plotly.express as px

HERE=Path(__file__).resolve().parent
df=pd.read_csv(HERE/'data/retail_sales_synthetic.csv',parse_dates=['order_date'])
revenue=df.revenue.sum();profit=df.profit.sum();margin=100*profit/revenue
monthly=df.set_index('order_date').resample('MS')[['revenue','profit']].sum().reset_index()
by_cat=df.groupby('category',as_index=False)['revenue'].sum().sort_values('revenue',ascending=False)
by_region=df.groupby('region',as_index=False)['profit'].sum().sort_values('profit',ascending=False)
figures=[
 px.line(monthly,x='order_date',y=['revenue','profit'],markers=True,title='Monthly revenue and profit'),
 px.bar(by_cat,x='category',y='revenue',title='Revenue by category'),
 px.bar(by_region,x='region',y='profit',title='Profit by region'),
 px.scatter(df,x='revenue',y='profit',color='category',hover_data=['order_id','region'],title='Order revenue vs profit'),
]
html=['''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Retail Analytics — Synthetic Case Study</title><style>body{font-family:system-ui,sans-serif;background:#f4f7fb;color:#18263c;margin:0;padding:24px}.wrap{max-width:1180px;margin:auto}.kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:14px}.card,.chart{background:white;border-radius:14px;padding:18px;box-shadow:0 2px 14px #18263c10;margin:14px 0}.kpi{font-size:1.7rem;font-weight:700}small{color:#526078}</style></head><body><div class="wrap"><h1>Retail Analytics Dashboard</h1><p>Educational case study — 600 synthetic 2025 orders. Not real business performance.</p><div class="kpis">''']
for label,value in [('Revenue',f'${revenue:,.0f}'),('Profit',f'${profit:,.0f}'),('Orders',f'{len(df):,}'),('Profit margin',f'{margin:.1f}%')]:
 html.append(f'<div class="card"><small>{label}</small><div class="kpi">{value}</div></div>')
html.append('</div>')
for idx,fig in enumerate(figures):
 html.append('<section class="chart">'+fig.to_html(full_html=False,include_plotlyjs=True if idx==0 else False)+'</section>')
html.append('<p><small>Definitions: margin = total profit / total revenue. Generated for learning; no live data connection.</small></p></div></body></html>')
out=HERE/'outputs'/'retail_dashboard.html';out.parent.mkdir(exist_ok=True)
out.write_text(''.join(html),encoding='utf-8')
print(f'Created {out}')
