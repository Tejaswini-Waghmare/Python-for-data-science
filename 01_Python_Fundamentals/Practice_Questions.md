# Python Fundamentals — Practice Questions and Worked Solutions

Complete the exercises before reading the solutions. All examples use the Python standard library. These are original practice problems with synthetic data.

## Beginner

**Q1.** Given `amounts = [20, 50, -10, 40]`, calculate the count, net total, and average.  
**Q2.** From `numbers = [1, 2, 3, 4, 5, 6]`, create a list of squares of even numbers.  
**Q3.** Count how many times each category occurs in `['food', 'rent', 'food', 'travel', 'food']`.

## Intermediate

**Q4.** Write a function `positive_total(values)` returning the sum of strictly positive values.  
**Q5.** Group the following expenses by category and sum amounts: `[("food", 20), ("travel", 35), ("food", 15)]`.  
**Q6.** Write `safe_average(values)` that returns `None` for an empty list and otherwise returns the arithmetic mean.

## Advanced

**Q7.** Given transaction dictionaries with `id` and `amount`, find duplicate IDs without changing the input.  
**Q8.** Parse a list of numeric strings, skip invalid entries, and report both parsed numbers and invalid strings.  
**Q9.** Rank categories by total spending, highest first; use alphabetical category name to break ties.

---

# Worked Solutions

## A1
```python
amounts = [20, 50, -10, 40]
print(len(amounts), sum(amounts), sum(amounts) / len(amounts))
# 4 100 25.0
```

## A2
```python
numbers = [1, 2, 3, 4, 5, 6]
print([n ** 2 for n in numbers if n % 2 == 0])
# [4, 16, 36]
```

## A3
```python
from collections import Counter
categories = ['food', 'rent', 'food', 'travel', 'food']
print(dict(Counter(categories)))
# {'food': 3, 'rent': 1, 'travel': 1}
```

## A4
```python
def positive_total(values):
    return sum(value for value in values if value > 0)

assert positive_total([10, -3, 5, 0]) == 15
```

## A5
```python
expenses = [('food', 20), ('travel', 35), ('food', 15)]
totals = {}
for category, amount in expenses:
    totals[category] = totals.get(category, 0) + amount
assert totals == {'food': 35, 'travel': 35}
```

## A6
```python
def safe_average(values):
    return sum(values) / len(values) if values else None

assert safe_average([]) is None
assert safe_average([2, 4, 6]) == 4
```

## A7
```python
records = [{'id': 'A', 'amount': 10}, {'id': 'B', 'amount': 20}, {'id': 'A', 'amount': 30}]
seen, duplicates = set(), set()
for record in records:
    transaction_id = record['id']
    if transaction_id in seen:
        duplicates.add(transaction_id)
    seen.add(transaction_id)
assert duplicates == {'A'}
```

## A8
```python
raw_values = ['12.5', 'oops', '3', '']
parsed, invalid = [], []
for raw in raw_values:
    try:
        parsed.append(float(raw))
    except ValueError:
        invalid.append(raw)
assert parsed == [12.5, 3.0]
assert invalid == ['oops', '']
```

## A9
```python
totals = {'travel': 80, 'food': 120, 'rent': 120}
ranked = sorted(totals.items(), key=lambda pair: (-pair[1], pair[0]))
assert ranked == [('food', 120), ('rent', 120), ('travel', 80)]
```

## Further study

- [Python official tutorial](https://docs.python.org/3/tutorial/)
- [Python collections](https://docs.python.org/3/library/collections.html)
- [Python pathlib](https://docs.python.org/3/library/pathlib.html)

**Portfolio tip:** Add your own explanations and additional exercises as you learn. Never present unrun code or unverified output as tested.
