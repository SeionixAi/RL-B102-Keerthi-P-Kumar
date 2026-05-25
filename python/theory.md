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

## What is File Handling in Python?

File handling is the process of creating, reading, writing, updating, and deleting files in Python. It is used to store and retrieve data permanently.

We use the `open()` function to work with files.

Syntax:

file = open("filename", "mode")

### File Modes

- `r` → Read mode (default). Used to read a file.
- `w` → Write mode. Overwrites existing content.
- `a` → Append mode. Adds new content without deleting old data.
- `x` → Create mode. Creates a new file.
- `b` → Binary mode. Used for images, videos, etc.
- `t` → Text mode (default).

Combined modes:

- `r+` → Read and write
- `w+` → Write and read
- `a+` → Append and read

File handling is important for reading datasets, saving logs, storing results, and working with files permanently.

## Difference between read(), readline(), and readlines()

Python provides different methods to read files.

### read()

- Reads the entire file content at once.
- Returns a string.

Example:

content = file.read()

### readline()

- Reads one line at a time.
- Returns a string.
- Each call reads the next line.

Example:

line = file.readline()

### readlines()

- Reads all lines and stores them in a list.
- Each line becomes one item in the list.

Example:

lines = file.readlines()

Difference:

- `read()` → complete file
- `readline()` → one line
- `readlines()` → all lines as a list

## What is Exception Hierarchy in Python?

An exception is an error that occurs during program execution.

Python exceptions follow a hierarchy (parent-child structure). The main parent class is `Exception`, and specific exceptions inherit from it.

Example hierarchy:

BaseException
└── Exception
    ├── ArithmeticError
    │   └── ZeroDivisionError
    ├── LookupError
    │   ├── IndexError
    │   └── KeyError
    ├── ValueError
    ├── TypeError
    └── FileNotFoundError

Common exceptions:

- `ZeroDivisionError` → division by zero
- `ValueError` → invalid value
- `TypeError` → wrong data type operation
- `IndexError` → invalid list index
- `KeyError` → missing dictionary key
- `FileNotFoundError` → file not found

Exception hierarchy helps Python organize errors and allows developers to catch either specific or general exceptions.

## Difference between try-except and try-except-finally

### try-except

Used to handle errors and prevent program crashes.

Syntax:

try:
    risky code
except:
    handle error

Example:

try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

### try-except-finally

Used to handle errors and execute code that must run whether an error occurs or not.

Syntax:

try:
    risky code
except:
    handle error
finally:
    always execute

Example:

try:
    x = 10 / 0
except ZeroDivisionError:
    print("Error")
finally:
    print("Finished")

Difference:

- `try-except` → handles errors
- `try-except-finally` → handles errors and always executes cleanup code

`finally` is commonly used for closing files, database connections, and cleanup operations.

## Purpose of the with Statement in Python

The `with` statement is used to work with resources (such as files) safely and automatically.

It automatically closes the file after use, even if an error occurs.

Syntax:

with open("file.txt", "mode") as file:
    # work with file

Example:

with open("data.txt", "r") as file:
    content = file.read()
    print(content)

Advantages:

- Automatically closes files
- Cleaner and shorter code
- Prevents resource leaks
- Safer than manually calling `close()`

`with` is commonly used in file handling, database connections, and resource management.

## What are Iterators in Python?

An iterator is an object that allows accessing elements of a collection one at a time.

### Iterable
An iterable is an object that can be looped over (e.g., list, tuple, string).

### Iterator
An iterator is an object that returns elements one by one using the `next()` function.

### Creating an Iterator

it = iter([1, 2, 3])

### Accessing Elements

next(it)  # 1
next(it)  # 2
next(it)  # 3

After all elements are consumed, Python raises StopIteration.

### How for loop works internally

A for loop uses iter() and next() internally and stops when StopIteration is raised.

### Advantages of Iterators

- Memory efficient
- Useful for large datasets
- Supports lazy evaluation (data generated on demand)

## What are Generators in Python?

Generators are special functions that return values one at a time using the `yield` keyword instead of `return`.

### How Generators Work

- `yield` produces a value and pauses the function
- Execution resumes from where it stopped on the next call

### Example

def my_gen():
    yield 1
    yield 2
    yield 3

### Usage

gen = my_gen()

next(gen)  # 1
next(gen)  # 2
next(gen)  # 3

After all values are produced, StopIteration is raised.

### Difference between Function and Generator

| Function | Generator |
|----------|-----------|
| Uses return | Uses yield |
| Returns once | Returns multiple values over time |
| Stores full result | Produces values one at a time |
| Memory heavy | Memory efficient |

### Advantages

- Saves memory
- Useful for large datasets
- Supports streaming data processing
- Used in ML pipelines and data processing workflows

## What is *args and **kwargs?

`*args` and `**kwargs` are used in Python functions to pass variable-length arguments.

### *args

- Used to pass multiple positional arguments
- Stored as a tuple

Example:

def add(*args):
    return sum(args)

add(1, 2, 3, 4)

### **kwargs

- Used to pass multiple keyword arguments
- Stored as a dictionary

Example:

def person(**kwargs):
    print(kwargs)

person(name="Keerthi", age=25)

### Difference

| Feature | *args | **kwargs |
|--------|------|----------|
| Type | Tuple | Dictionary |
| Input | Positional arguments | Keyword arguments |

### Key Idea

- *args → multiple values
- **kwargs → multiple named values

## What is Type Casting in Python?

Type casting is the process of converting one data type into another.

### Types of Type Casting

1. Implicit Casting (Automatic)
Python automatically converts smaller data types to larger ones.

Example:

x = 10
y = 2.5
print(x + y)  # 12.5

2. Explicit Casting (Manual)
We manually convert data types using functions.

Common functions:
- int()
- float()
- str()
- list()
- tuple()

### Examples

String to Integer:
x = "10"
y = int(x)

Integer to String:
x = 10
y = str(x)

Float to Integer:
x = 10.9
y = int(x)  # 10

### Key Idea
Type casting is used to convert data types so operations between them are possible.

## What are Built-in Functions in Python?

Built-in functions are pre-defined functions provided by Python that can be used directly without importing any module.

### Examples of Built-in Functions

- print() → displays output
- input() → takes user input
- type() → returns data type
- len() → returns length of an object
- sum() → returns sum of elements

### Other Common Built-ins

- max()
- min()
- abs()
- round()
- sorted()
- range()

### Key Idea

Built-in functions help perform common tasks easily without writing custom code.

