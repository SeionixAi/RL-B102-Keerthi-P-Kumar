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


Day 2

## What is dynamic typing in Python?

Python is a dynamically typed language, meaning Python automatically determines the data type of a variable at runtime.

Example:

```python
age = 25
name = "Keerthi"
height = 5.8
```

Python automatically detects:

- `25` → integer (`int`)
- `"Keerthi"` → string (`str`)
- `5.8` → float

A variable can also change type:

```python
x = 10
x = "Hello"
```

Dynamic typing makes Python flexible and easier to write.

## What is the difference between mutable and immutable data types?

Mutable objects can be changed after creation, while immutable objects cannot be changed.

### Mutable data types
Examples:
- `list`
- `dictionary`
- `set`

Example:

```python
numbers = [10, 20, 30]

numbers[0] = 100

print(numbers)
```

### Immutable data types
Examples:
- `int`
- `float`
- `string`
- `tuple`
- `bool`

Example:

```python
name = "hello"

# Not allowed
name[0] = "H"
```

Difference:

- Mutable → can be modified
- Immutable → cannot be modified

## What are local and global variables?

Variables in Python can be local or global depending on where they are created.

### Global variable
A global variable is defined outside a function and can be accessed throughout the program.

Example:

```python
name = "Keerthi"

def greet():
    print(name)

greet()
```

### Local variable
A local variable is defined inside a function and can only be accessed inside that function.

Example:

```python
def greet():
    message = "Hello"

    print(message)

greet()
```

Difference:

- Global variable → created outside a function
- Local variable → created inside a function

## What is the purpose of the return statement in a function?

The `return` statement is used to send a value back from a function.

It allows a function to produce a result that can be stored or used later.

Example:

```python
def add(a, b):
    return a + b

result = add(10, 20)

print(result)
```

Output:

```text
30
```
- `return` → sends value back from a function

## What is list comprehension?

List comprehension is a short and efficient way to create lists in Python.

Instead of using multiple lines with loops, list comprehension creates lists in a single line.

Example:

```python
numbers = [i * i for i in range(1, 6)]

print(numbers)
```

Output:

```text
[1, 4, 9, 16, 25]
```

Example with condition:

```python
even_numbers = [i for i in range(1, 11) if i % 2 == 0]

print(even_numbers)
```

List comprehension makes code shorter, cleaner, and easier to read.

## Difference between break, continue, and pass

`break`, `continue`, and `pass` are loop control statements in Python.

### break
Stops the loop completely.

Example:

```python
for i in range(1, 6):
    if i == 3:
        break

    print(i)
```

### continue
Skips the current iteration and moves to the next iteration.

Example:

```python
for i in range(1, 6):
    if i == 3:
        continue

    print(i)
```

### pass
Does nothing and acts as a placeholder.

Example:

```python
for i in range(1, 6):
    if i == 3:
        pass

    print(i)
```

Difference:

- `break` → stop loop
- `continue` → skip iteration
- `pass` → do nothing

## What is recursion? Give a simple example.

Recursion is a programming technique where a function calls itself to solve a problem.

A recursive function must have a stopping condition called a **base case**.

Example:

```python
def countdown(n):
    if n == 0:
        return

    print(n)
    countdown(n - 1)

countdown(5)
```

Output:

```text
5
4
3
2
1
```

In recursion, a function repeatedly calls itself until the base condition is reached.

## What is a lambda function?

A lambda function is a small anonymous function written in one line.

It is mainly used for short and simple operations.

Syntax:

```python
lambda arguments: expression
```

Example:

```python
square = lambda num: num * num

print(square(5))
```

Output:

```text
25
```

Difference:

- Normal function → uses `def`
- Lambda function → short one-line function

## What is the difference between `is` and `==`?

`==` compares values, while `is` compares object identity (memory location).

### `==`
Checks if values are equal.

Example:

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
```

Output:

```text
True
```

### `is`
Checks if two variables refer to the same object in memory.

Example:

```python
a = [1, 2, 3]
b = a

print(a is b)
```

Output:

```text
True
```

Difference:

- `==` → compares values
- `is` → compares memory/object identity

## What are docstrings and why are they important?

Docstrings (documentation strings) are used to explain the purpose of functions, classes, or modules in Python.

They are written using triple quotes.

Example:

```python
def add(a, b):
    """
    Returns the sum of two numbers.
    """

    return a + b
```

Importance of docstrings:

- Improve code readability
- Help explain function purpose
- Useful for teamwork and maintenance
- Provide documentation for developers

Docstrings make code easier to understand and maintain.

