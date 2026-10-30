# Module 02 — NumPy for Data Science

**Level:** beginner to intermediate | **Prerequisites:** Python lists, loops, functions | **Estimated time:** 5–7 hours

## Learning objectives
- Explain why NumPy arrays are useful for numerical computing.
- Create arrays, inspect shape/dtype, and distinguish views from copies.
- Select, filter, reshape, and combine arrays.
- Apply broadcasting, aggregation, and vectorized calculations.
- Handle missing values and generate reproducible random samples.
- Analyze a small transaction dataset without Python loops.

## 1. Install and import

```bash
python -m pip install numpy jupyter
```

```python
import numpy as np
print(np.__version__)
```

NumPy's central object is `ndarray`: a homogeneous, N-dimensional array. Unlike a Python list, a numeric array stores values with a consistent data type, making many numerical operations efficient.

## 2. Arrays, dimensions, shape, and dtype

```python
one_d = np.array([10, 20, 30])
two_d = np.array([[1, 2, 3], [4, 5, 6]])
print(one_d.ndim, one_d.shape, one_d.dtype)
print(two_d.ndim, two_d.shape, two_d.size)
```

`ndim` is the number of axes; `shape` is the length along each axis; `size` is total elements; `dtype` describes stored values. Type promotion can occur when mixing ints and floats.

## 3. Array constructors

```python
np.zeros((2, 3))
np.ones((2, 2))
np.arange(0, 10, 2)       # 0,2,4,6,8
np.linspace(0, 1, 5)     # five evenly spaced values
np.eye(3)                # identity matrix
```

`arange` specifies a step; `linspace` specifies the number of samples. Floating-point `arange` can be surprising; use `linspace` for a known sample count.

## 4. Indexing, slicing, and boolean masks

```python
sales = np.array([120, 450, 80, 700, 250])
print(sales[0], sales[-1])
print(sales[1:4])
print(sales[sales >= 250])
```

NumPy slices generally return **views** of original data, so changing a slice may change the original array. Use `.copy()` when you need independent data.

## 5. Reshaping and axis

```python
matrix = np.arange(1, 13).reshape(3, 4)
print(matrix.sum(axis=0))  # column totals (4 values)
print(matrix.sum(axis=1))  # row totals (3 values)
```

For a 2D array, `axis=0` reduces rows, producing one value per column; `axis=1` reduces columns, producing one value per row. Reshaping requires a compatible element count.

## 6. Vectorization and broadcasting

```python
prices = np.array([100.0, 200.0, 300.0])
with_tax = prices * 1.08
monthly = np.array([[10, 20, 30], [40, 50, 60]])
weights = np.array([1, 2, 3])
print(monthly * weights)
```

Broadcasting aligns dimensions from the right: each pair must be equal or one must be 1. For example, `(2, 3)` and `(3,)` are compatible, but `(2, 3)` and `(2,)` are not.

## 7. Statistics and missing data

```python
scores = np.array([72., 85., np.nan, 91.])
print(np.mean(scores))       # nan
print(np.nanmean(scores))    # ignores nan
print(np.nanmedian(scores))
```

`np.nan` represents a missing numeric value; nan-aware functions exclude it. Check whether missingness itself is meaningful before dropping it. Standard deviation defaults to population `ddof=0`; use `ddof=1` for the usual sample standard deviation.

## 8. Randomness and reproducibility

```python
rng = np.random.default_rng(42)
sample = rng.normal(loc=100, scale=15, size=10)
print(sample.round(2))
```

A fixed seed makes a demonstration reproducible; it does not make a random sample representative of a population.

## 9. Linear algebra basics

```python
A = np.array([[1, 2], [3, 4]])
b = np.array([5, 6])
print(A @ b)             # matrix-vector multiplication
print(np.linalg.solve(A, b))
```

Prefer `np.linalg.solve(A, b)` to explicitly computing `np.linalg.inv(A) @ b` for linear systems.

## 10. Real-world mini case: transaction analytics

```python
amounts = np.array([120., -40., 350., -25., 90., 500.])
credits = amounts[amounts > 0]
debits = amounts[amounts < 0]
print('Net:', amounts.sum())          # 995.0
print('Total credits:', credits.sum()) # 1060.0
print('Total debits:', debits.sum())   # -65.0
print('Large credits:', (credits >= 300).sum()) # 2
```

This is synthetic example data. In real payments analysis, a positive/negative sign convention must be explicitly documented.

## Common mistakes
1. `a * b` is elementwise multiplication; `a @ b` is matrix multiplication.
2. `array == value` creates a boolean array; use `np.any`/`np.all` for a single truth value.
3. Slicing can produce a view; `.copy()` makes independent data.
4. An empty slice can produce warnings/NaNs for averages.
5. NumPy integer arrays cannot store `np.nan` without conversion to float.

## Study checklist
- [ ] Explain `shape`, `ndim`, `size`, and `dtype`
- [ ] Write a boolean filter
- [ ] Explain `axis=0` versus `axis=1`
- [ ] Show a view versus a copy
- [ ] Use broadcasting correctly
- [ ] Analyze synthetic transaction amounts
- [ ] Complete exercises before viewing solutions

## References
- [NumPy absolute beginners guide](https://numpy.org/doc/stable/user/absolute_beginners.html)
- [NumPy broadcasting guide](https://numpy.org/doc/stable/user/basics.broadcasting.html)
- [NumPy indexing guide](https://numpy.org/doc/stable/user/basics.indexing.html)
- [NumPy random Generator](https://numpy.org/doc/stable/reference/random/generator.html)
