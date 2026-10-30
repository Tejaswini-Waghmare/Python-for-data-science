# Practice Questions — Module 03 Pandas

Use `sample_orders.csv` and `sample_customers.csv`. Try solving without opening `Solutions.md`. State your metric definitions clearly.

## Beginner
1. Load orders, parse `order_date`, and print row/column counts.
2. Show missing values per column and count duplicate `order_id` values.
3. Select orders from the `East` region with quantity at least 3.
4. Create a `gross_sales` column and display the first five rows.

## Intermediate
5. Fill missing regions with `Unknown` and add a Boolean missing-price flag.
6. Define eligible sales as completed orders with known prices; compute total net sales after discounts.
7. Produce a table of eligible order count, total net sales, and average order value by category.
8. Join eligible orders to customers and check that the row count is unchanged.

## Advanced
9. Create a region-by-category pivot table of eligible net sales.
10. Calculate monthly eligible net sales and identify the highest month.
11. Find the top three customers by eligible net sales, including their segments.
12. Explain two risks of treating missing prices as zero and two risks of an unchecked many-to-many join.

## Stretch challenges
13. Create a chart of sales by region and save it as `region_sales.png`.
14. Add a validation test that fails if a discount is outside 0–1 or if an order ID is duplicated.
15. Compare results when pending orders are included, and explain why the metric changes.

## Self-review checklist
- [ ] I can explain every filtering decision.
- [ ] I checked missingness and duplicates.
- [ ] I validated join cardinality.
- [ ] I can reproduce the results from the two CSVs.
- [ ] I did not confuse sales with profit.
