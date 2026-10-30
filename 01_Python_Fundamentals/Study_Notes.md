
# Python Fundamentals for Data Science

## 1. Introduction to Python

Python is a high-level programming language widely used for data analysis, machine learning, automation, and artificial intelligence.

### Why Python for Data Science?

- Easy-to-read syntax
- Large ecosystem of scientific libraries
- Supports data cleaning and transformation
- Used in machine learning and AI applications

## 2. Variables and Data Types

Variables store information.

```python
student_name = "Tejaswini"
age = 29
gpa = 3.31
is_student = True

print(type(student_name))
print(type(age))
print(type(gpa))
print(type(is_student))
```

Common data types:

| Type | Example | Purpose |
|---|---|---|
| int | 25 | Whole numbers |
| float | 3.14 | Decimal numbers |
| str | "Python" | Text |
| bool | True | Logical values |
| list | [1, 2, 3] | Ordered, mutable collection |
| tuple | (1, 2) | Ordered, immutable collection |
| dict | {"a": 1} | Key-value pairs |
| set | {1, 2, 3} | Unique elements |

## 3. Lists

Lists are useful for storing datasets and sequences.

```python
sales = [100, 250, 300, 450]

print(sales[0])
print(sum(sales))
print(max(sales))
print(min(sales))
```

## 4. Conditional Statements

Conditions help programs make decisions.

```python
score = 85

if score >= 90:
    print("Excellent")
elif score >= 70:
    print("Good")
else:
    print("Needs Improvement")
```

## 5. Loops

Loops automate repetitive tasks.

```python
sales = [100, 200, 300, 400]

for amount in sales:
    print(amount * 1.10)
```

## 6. Functions

Functions organize reusable logic.

```python
def calculate_average(numbers):
    if not numbers:
        raise ValueError("Input cannot be empty")
    return sum(numbers) / len(numbers)

marks = [80, 90, 75, 85]

print(calculate_average(marks))
```

## 7. List Comprehensions

List comprehensions create lists concisely.

```python
numbers = [1, 2, 3, 4, 5]

squares = [x**2 for x in numbers]

print(squares)
```

## 8. Exception Handling

Exception handling prevents unexpected input errors from crashing a program without explanation.

```python
try:
    value = int("abc")
except ValueError:
    print("Invalid number")
```

## 9. Data Science Example

Calculate the average transaction amount.

```python
transactions = [250, 400, 150, 600, 300]

average = sum(transactions) / len(transactions)

print("Average transaction:", average)
```

Expected output:

```text
Average transaction: 340.0
```

## 10. Practice Exercises

1. Create a list of 10 transaction amounts.
2. Calculate their total and average.
3. Find the maximum and minimum transaction.
4. Write a function that returns transactions above 500.
5. Use a dictionary to store monthly expenses.
6. Write a loop to calculate a 10% increase in each expense.
7. Handle invalid numerical input using try/except.

## Learning Outcomes

After completing this module, you should be able to:

- Understand Python's fundamental data types
- Write conditional statements and loops
- Create reusable functions
- Work with lists and dictionaries
- Perform basic data analysis
- Handle common programming errors

## References

- [Official Python Tutorial](https://docs.python.org/3/tutorial/)
- [Python Standard Library](https://docs.python.org/3/library/)
