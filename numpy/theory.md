## 1. What is NumPy?

NumPy (Numerical Python) is a Python library used for numerical computing, arrays, and mathematical operations.

It is mainly used in Data Science, Machine Learning, and AI for handling numerical data efficiently.

Features of NumPy:

- Fast numerical computations
- Supports arrays and matrix operations
- Efficient memory usage
- Widely used in AI and Data Science

Example:

```python
import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr)
```

## 2. Why is NumPy faster than Python lists?

NumPy is faster than Python lists because:

- Uses optimized arrays stored in continuous memory
- Stores fixed data types
- Supports vectorized operations (avoids manual loops)
- Uses optimized low-level code internally (C/C++)

Example:

Python list:

```python
result = []

for i in range(len(a)):
    result.append(a[i] + b[i])
```

NumPy:

```python
import numpy as np

a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print(a + b)
```

NumPy performs calculations faster and more efficiently.

## 3. What is an ndarray?

`ndarray` stands for **N-dimensional array** and is the main data structure in NumPy.

It is used to store numerical data efficiently and supports fast mathematical operations.

Example:

```python
import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr)
```

An ndarray can have multiple dimensions:

- 1D array → single row of values
- 2D array → rows and columns (matrix)
- 3D array → multiple matrices

NumPy ndarray is faster and more memory efficient than Python lists.

## 4. Difference between array and list

A list is Python’s built-in data structure, while an array is provided by NumPy for numerical computations.

### List
- Built into Python
- Can store mixed data types
- Slower for numerical operations

Example:

```python
numbers = [10, 20, 30]
```

### NumPy Array
- Provided by NumPy
- Faster and memory efficient
- Supports mathematical operations
- Usually stores same data type

Example:

```python
import numpy as np

arr = np.array([10, 20, 30])
```

Difference:

- List → flexible and general-purpose
- Array → optimized for numerical computing

## 5. What is broadcasting?

Broadcasting is a NumPy feature that allows mathematical operations between arrays of different sizes or shapes.

NumPy automatically expands smaller arrays or values to match larger arrays during calculations.

Example:

```python
import numpy as np

arr = np.array([10, 20, 30])

print(arr + 5)
```

Output:

```text
[15 25 35]
```

In this example, NumPy automatically applies `5` to all elements of the array.

Broadcasting helps perform calculations efficiently without using loops.

## What is vectorization in NumPy?

Vectorization is the process of performing operations on an entire NumPy array without using loops.

It allows operations to be applied to all elements at once.

Example:

```python
import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr * 2)
```

Output:

```text
[2 4 6 8]
```

Advantages of vectorization:

- Faster execution
- Cleaner code
- Efficient for AI and Data Science

## What is the difference between reshape() and resize()?

Both `reshape()` and `resize()` are used to change the shape of a NumPy array.

### reshape()
- Returns a reshaped version of the array
- Does not modify the original array

Example:

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

new_arr = arr.reshape(2, 3)

print(new_arr)
```

### resize()
- Modifies the original array
- Can also change the size of the array

Example:

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

arr.resize((2, 3))

print(arr)
```

Difference:

- `reshape()` → returns reshaped array
- `resize()` → modifies original array

## What are NumPy dimensions and axes?

Dimensions represent the number of levels in a NumPy array, while axes represent the direction of operations.

### Dimensions

1D array:

```python
import numpy as np

arr = np.array([1, 2, 3])

print(arr.ndim)
```

2D array:

```python
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr.ndim)
```

### Axes

`axis=0` → operation performed column-wise

Example:

```python
print(arr.sum(axis=0))
```

`axis=1` → operation performed row-wise

Example:

```python
print(arr.sum(axis=1))
```

Difference:

- Dimensions → number of levels in array
- Axes → direction of operation

## What is slicing in NumPy arrays?

Slicing is the process of selecting a portion of a NumPy array.

Syntax:

```python
[start:end]
```

Example:

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print(arr[1:4])
```

Output:

```text
[20 30 40]
```

Slicing can also be used in 2D arrays.

Example:

```python
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr[0:2, 1:3])
```

Slicing helps extract selected rows, columns, or elements from arrays.

## NumPy helps AI by:

speeding up mathematical operations
handling vectors and matrices
enabling linear algebra operations
removing slow Python loops
supporting large-scale data processing