## 1. What is Pandas?

Pandas is a Python library used for data analysis and data manipulation.

It helps work with structured data such as tables, CSV files, and datasets.

Features of Pandas:

- Handles table-like data efficiently
- Reads CSV and Excel files
- Supports filtering and data analysis
- Helps clean and prepare data for AI and Machine Learning

Example:

```python
import pandas as pd

data = {
    "Name": ["Alice", "Bob"],
    "Age": [22, 24]
}

df = pd.DataFrame(data)

print(df)
```

Pandas is widely used in Data Science, AI, and Machine Learning.

## 2. What is a DataFrame?

A DataFrame is the main data structure in Pandas used to store data in rows and columns.

It looks similar to an Excel sheet or database table.

Example:

```python
import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [22, 24, 23],
    "Marks": [85, 90, 88]
}

df = pd.DataFrame(data)

print(df)
```

A DataFrame helps organize, filter, and analyze structured data efficiently.

## 3. Difference between Series and DataFrame

Series and DataFrame are data structures in Pandas.

### Series
- One-dimensional data structure
- Represents a single column of data

Example:

```python
import pandas as pd

data = pd.Series([10, 20, 30])

print(data)
```

### DataFrame
- Two-dimensional data structure
- Represents rows and columns (table)

Example:

```python
import pandas as pd

data = {
    "Name": ["Alice", "Bob"],
    "Age": [22, 24]
}

df = pd.DataFrame(data)

print(df)
```

Difference:

- Series → single column of data
- DataFrame → table with multiple columns

## 4. What is CSV?

CSV stands for **Comma-Separated Values**.

It is a file format used to store tabular data (rows and columns).

Example CSV data:

```text
Name,Age,Marks
Alice,22,85
Bob,24,90
Charlie,23,88
```

Pandas can read CSV files easily.

Example:

```python
import pandas as pd

df = pd.read_csv("data.csv")

print(df)
```

CSV files are widely used in Data Science, AI, and Machine Learning for storing datasets.

## 5. Why is Pandas important for AI?

Pandas is important for AI because it helps clean, organize, analyze, and prepare data before training Machine Learning models.

Uses of Pandas in AI:

- Reads datasets such as CSV files
- Cleans missing or incorrect data
- Filters and analyzes data
- Helps prepare structured data for Machine Learning

Example:

```python
import pandas as pd

df = pd.read_csv("data.csv")

print(df["Age"].mean())
```

Pandas is widely used in Data Science and AI for data preprocessing and analysis.

## Pandas - Data Cleaning and Preprocessing

### 1. What is data cleaning in Pandas?

Data cleaning means fixing or removing incorrect, missing, or inconsistent data.

Pandas helps by:
- removing null values
- filling missing values
- removing duplicates

Example:
```python
df.dropna()
df.fillna(0)
```

---

### 2. Difference between loc and iloc

- `loc` → label-based indexing
- `iloc` → index-based (position)

Example:
```python
df.loc[0, "Age"]
df.iloc[0, 1]
```

---

### 3. Missing values

Missing values are empty or undefined data.

Pandas handles them using:
```python
df.dropna()
df.fillna(0)
```

---

### 4. groupby()

Used to group data and perform aggregations.

Example:
```python
df.groupby("Dept")["Salary"].mean()
```

---

### 5. Pandas in AI preprocessing

Pandas is used to:
- clean data
- handle missing values
- transform data
- prepare datasets for AI models

