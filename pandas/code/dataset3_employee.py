import numpy as np
import pandas as pd

# Create dataset
np.random.seed(3)
rows = 120

df = pd.DataFrame({
    "EmpId": np.arange(1, rows + 1),
    "Dept": np.random.choice(
        ["HR", "IT", "Sales"],
        rows
    ),
    "Salary": np.random.randint(
        30000, 150000, rows
    ),
    "Gender": np.random.choice(
        ["male", "female"],
        rows
    )
})

print("Original Data")
print(df.head())

# Rename column
df.rename(
    columns={"Dept": "Department"},
    inplace=True
)

# Drop column
df.drop(
    "Gender",
    axis=1,
    inplace=True
)

print("\nUpdated Data")
print(df.head())

print("\nAggregation")
print(
    df.groupby("Department")["Salary"]
    .agg(["mean", "max"])
)