## 1. What is Python? Why is it popular in AI & Data Science?

Python is a high-level, interpreted, and general-purpose programming language. It is simple, readable, and easy to learn.

Python is popular in AI and Data Science because:

- Easy syntax and readability
- Large number of libraries such as NumPy, Pandas, TensorFlow and PyTorch
- Strong community support
- Good for data analysis and visualization
- Fast development and experimentation in AI/ML

## 2. Difference between List, Tuple, Set and Dictionary

### List
- Ordered collection
- Mutable (can be changed)
- Allows duplicate values

### Tuple
- Ordered collection
- Immutable (cannot be changed)
- Allows duplicate values

### Set
- Unordered collection
- Mutable (can be changed)
- No duplicate values

### Dictionary
- Key-value pairs
- Mutable (can be changed)
- No duplicate keys
- Orderd collection

## 3. What are variables and data types in Python?

### Variables
Variables are containers used to store data in memory. They help store and reuse values in a program.

Example:

```python
name = "Keerthi"
age = 28
```

### Data Types
Data types define the type of data stored in a variable.

Common data types in Python:

- `int` → Integer values

- `float` → Decimal values

- `str` → Text values

- `bool` → True or False value

- `list` → Ordered collection

- `tuple` → Immutable ordered collection

- `set` → Unique values

- `dictionary` → Key-value pairs

## 4. What is the difference between `==` and `=`?

### `=` (Assignment Operator)

The `=` operator is used to assign a value to a variable.

Example:

```python
age = 28
```

Here, `28` is assigned to the variable `age`.

### `==` (Comparison Operator)

The `==` operator is used to compare two values and check if they are equal.

Example:

```python
age = 28

print(age == 28)
```

Output:

```text
True
```
## 5. Explain `if`, `elif` and `else`

`if`, `elif`, and `else` are used for decision making in Python.

### `if`

Used to check a condition.

Example:

```python
age = 20

if age >= 18:
    print("Adult")
```

### `elif`

Used to check multiple conditions.

Example:

```python
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
```

### `else`

Runs when all conditions are false.

Example:

```python
age = 15

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

Difference:

- `if` → checks first condition
- `elif` → checks additional conditions
- `else` → runs if no condition is true

## 6. What is a function? Why do we use functions?

A function is a reusable block of code that performs a specific task.

Functions are created using the `def` keyword.

Example:

```python
def square(num):
    return num * num

print(square(5))
```

Why do we use functions?

- Code reusability (write once, use many times)
- Reduces repeated code
- Makes programs easier to organize
- Easier debugging and maintenance

Functions can take inputs (parameters) and return outputs.

## 7. Difference between `for` loop and `while` loop

Loops are used to repeat code multiple times.

### `for` loop

A `for` loop is used when the number of repetitions is known.

Example:

```python
for i in range(1, 6):
    print(i)
```

### `while` loop

A `while` loop is used when repetition depends on a condition.

Example:

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

Difference:

- `for` loop → used when repetitions are known
- `while` loop → used when repetitions depend on a condition

## 8. What is a module? Example

A module is a Python file that contains reusable code such as functions, variables, and classes.

Modules help reuse code and organize programs.

Example using the `math` module:

```python
import math

print(math.sqrt(25))
```

Output:

```text
5.0
```

Types of modules:

- Built-in modules (e.g., `math`, `random`)
- User-defined modules (created by programmers)

## 9. What is exception handling?

Exception handling is a way to handle errors in a program so that it does not crash.

Python mainly uses `try` and `except` blocks for exception handling.

Example:

```python
try:
    num = int(input("Enter a number: "))
    print(num)

except:
    print("Invalid input")
```

In this example, if the user enters invalid input, the program handles the error instead of crashing.

Purpose of exception handling:

- Prevents program crashes
- Handles unexpected errors
- Improves program reliability

## 10. What is pip?

`pip` is Python’s package manager used to install and manage Python libraries and packages.

It stands for:

**Pip Installs Packages**

Example:

Install NumPy:

```bash
pip install numpy
```

Common pip commands:

```bash
pip --version
pip install package_name
pip list
pip uninstall package_name
```

`pip` helps developers install external libraries required for projects.

