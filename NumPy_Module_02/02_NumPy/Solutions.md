# NumPy practice — worked solutions

> Try `Practice_Questions.md` before reading this file.

```python
import numpy as np
```

## 1. Array properties
```python
a = np.arange(1, 13)
print(a.shape, a.ndim, a.dtype)  # (12,), 1, integer dtype (platform-dependent)
```

## 2. Matrix selection
```python
m = np.arange(1, 13).reshape(3, 4)
print(m[1, :])  # [5 6 7 8]
print(m[:, 2])  # [3 7 11]
```

## 3. Boolean mask
```python
a = np.array([10, 20, 30, 40, 50])
print(a[a > 25])  # [30 40 50]
```

## 4. Evenly spaced values
```python
print(np.linspace(0, 1, 5))  # [0. 0.25 0.5 0.75 1.]
```

## 5. Aggregation by axis
```python
m = np.arange(1, 13).reshape(3, 4)
print(m.sum(axis=1))   # [10 26 42]
print(m.mean(axis=0))  # [5. 6. 7. 8.]
```

## 6. Vectorized tax
```python
prices = np.array([12.5, 20.0, 8.0])
print(np.round(prices * 1.08, 2))  # [13.5 21.6 8.64]
```

## 7. Views and copies
```python
a = np.array([1, 2, 3, 4])
view = a[1:3]
view[0] = 99
print(a)  # [1 99 3 4]
independent = a[1:3].copy()
independent[0] = 0
print(a)  # unchanged
```

## 8. Missing values
```python
values = np.array([10., np.nan, 30., 50.])
print(np.nanmean(values))  # 30.0
```

## 9. Seeded simulation
```python
rng = np.random.default_rng(42)
sample = rng.normal(50, 10, 100)
print(round(sample.mean(), 2))
print(round(sample.std(ddof=1), 2))
```
The sample statistics vary from the population parameters; the seed makes them reproducible.

## 10. Transactions
```python
amounts = np.array([120., -40., 350., -25., 90., 500.])
print(amounts.sum())  # 995.0
print(amounts[amounts > 0].sum())  # 1060.0
print(amounts[amounts < 0].sum())  # -65.0
print(np.sum(amounts >= 300))  # 2
```

## 11. Broadcasting
```python
sales = np.array([[100, 200, 300], [150, 250, 350]])
rates = np.array([0.05, 0.10, 0.20])
print(sales * rates)
# [[ 5. 20. 60.]
#  [ 7.5 25. 70.]]
```

## 12. Linear system
```python
A = np.array([[2., 1.], [1., -1.]])
b = np.array([5., 1.])
print(np.linalg.solve(A, b))  # [2. 1.]
```
