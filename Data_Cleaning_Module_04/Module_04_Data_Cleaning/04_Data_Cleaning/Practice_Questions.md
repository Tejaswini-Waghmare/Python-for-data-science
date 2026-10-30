# Practice Questions — Module 04

Work through these **before** opening `Solutions.md`. Use `data/messy_transactions.csv`.

## Beginner
1. Load every column as a string. Report shape and column names.
2. Calculate missing counts and percentages for each column.
3. Count raw `payment_status` categories, including blanks.
4. Detect exact duplicate rows and report how many there are.
5. Parse amounts after removing commas; count invalid amounts.

## Intermediate
6. Normalize `payment_status` values and report the new counts.
7. Standardize `category` labels, including `GROCERY` and whitespace.
8. Parse ISO dates and separately handle documented slash-formatted dates. Identify invalid or blank dates.
9. Find transaction IDs associated with more than one distinct row. Explain why keeping the first row is risky.
10. Write a validation function that returns reason codes for missing ID, invalid date, missing/negative amount, and invalid status.

## Advanced
11. Create a quarantine table with one row per rejected record and its reason(s).
12. Compare raw, exact-deduplicated, accepted, and quarantined row counts; verify reconciliation.
13. Flag amounts above $10,000 without automatically deleting them. Discuss possible false positives.
14. Add `transaction_month` and `transaction_weekday` for accepted rows. Explain leakage risks for prediction tasks.
15. Design a train/test-safe median imputation and scaling pipeline for a numeric feature. Explain why fitting on the full dataset is wrong.

## Reflection
Which cleaning decisions would change if negative amounts represented refunds? Which checks require a business stakeholder's approval?
