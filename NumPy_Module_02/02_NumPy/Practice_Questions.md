# NumPy practice questions

**Instructions:** Work through the questions in order. Try each one before opening `Solutions.md`. Use `import numpy as np`. All data is synthetic.

## Beginner
1. Create an array of integers 1 through 12. Print its `shape`, `ndim`, and `dtype`.
2. Create a 3×4 matrix of integers 1 through 12. Return the second row and third column.
3. For `a = np.array([10, 20, 30, 40, 50])`, select the elements greater than 25.
4. Create five evenly spaced values between 0 and 1 (inclusive).

## Intermediate
5. For `m = np.arange(1, 13).reshape(3, 4)`, calculate row sums and column means.
6. Add an 8% tax to `[12.5, 20.0, 8.0]` using vectorization; round to 2 decimals.
7. Explain and demonstrate how modifying a slice can change the original array, and how to avoid it.
8. Find the mean of `[10., np.nan, 30., 50.]` while ignoring the missing value.

## Advanced / applied
9. With a seeded generator (`42`), draw 100 values from a normal distribution with mean 50 and standard deviation 10. Report sample mean and sample standard deviation (`ddof=1`).
10. For `amounts = np.array([120., -40., 350., -25., 90., 500.])`, calculate net, total positive, total negative, and number of positive transactions >= 300.
11. Given `sales = np.array([[100, 200, 300], [150, 250, 350]])` and `rates = np.array([0.05, 0.10, 0.20])`, compute the discount amount for each cell using broadcasting.
12. Solve the linear system `2x + y = 5`, `x - y = 1` with NumPy.

## Reflection
- When is vectorization clearer than a loop?
- Why do views matter when cleaning data?
- Why should analysts document the meaning of missing values and transaction signs?
