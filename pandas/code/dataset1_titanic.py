import numpy as np
import pandas as pd

# Create dataset
np.random.seed(1)
rows = 200

df = pd.DataFrame({
    "PassengerId": np.arange(1, rows + 1),
    "Name": np.random.choice(
        ["Mr. John", "Mrs. Anna", "Miss Emma", "Dr. Smith"],
        rows
    ),
    "Age": np.random.choice(
        np.append(np.random.randint(1, 80, 180), [np.nan] * 20),
        rows
    ),
    "Sex": np.random.choice(["male", "female"], rows),
    "Pclass": np.random.choice([1, 2, 3], rows),
    "Fare": np.round(np.random.uniform(10, 500, rows), 2)
})

print("First 5 rows")
print(df.head())

print("\nLast 5 rows")
print(df.tail())

print("\nRandom 3 rows")
print(df.sample(3))

print("\nShape")
print(df.shape)

print("\nColumns")
print(df.columns)

print("\nInfo")
print(df.info())

print("\nStatistical Summary")
print(df.describe())

print("\nMissing Values")
print(df.isnull().sum())

# Fill missing Age values
df["Age"] = df["Age"].fillna(df["Age"].mean())

print("\nFemale Passengers")
print(df[df["Sex"] == "female"].head())

print("\nPassengers Age > 30")
print(df[df["Age"] > 30].head())

print("\nAverage Fare by Pclass")
print(df.groupby("Pclass")["Fare"].mean())