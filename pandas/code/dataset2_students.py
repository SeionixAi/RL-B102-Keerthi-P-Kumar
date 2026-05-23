import numpy as np
import pandas as pd

# Create dataset
np.random.seed(2)
rows = 150

df = pd.DataFrame({
    "StudentId": np.arange(1, rows + 1),
    "Age": np.random.randint(18, 30, rows),
    "Gender": np.random.choice(["male", "female"], rows),
    "Course": np.random.choice(
        ["AI", "DS", "ML", "Python"],
        rows
    ),
    "Marks": np.random.randint(35, 100, rows)
})

print("First 5 rows")
print(df.head())

print("\nSorted by Marks")
print(df.sort_values(by="Marks", ascending=False).head())

print("\nGender Count")
print(df["Gender"].value_counts())

# Apply function
df["Result"] = df["Marks"].apply(
    lambda x: "Pass" if x >= 50 else "Fail"
)

print("\nWith Result Column")
print(df.head())

print("\nAverage Marks by Course")
print(df.groupby("Course")["Marks"].mean())