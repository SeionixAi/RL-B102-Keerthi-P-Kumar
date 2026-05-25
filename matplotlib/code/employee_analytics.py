import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------
# Dataset Creation
# -------------------------
np.random.seed(10)

df = pd.DataFrame({
    "employee_id": range(1, 501),
    "experience_years": np.random.randint(0, 20, 500),
    "salary": np.random.randint(20000, 150000, 500),
    "performance_rating": np.random.randint(1, 6, 500),
    "department": np.random.choice(["IT", "HR", "Sales", "Finance"], 500)
})

# -------------------------
# Inspection
# -------------------------
print(df.info())
print(df.describe(include="all"))

# -------------------------
# GroupBy Analysis
# -------------------------
dept_salary_stats = df.groupby("department")["salary"].agg(["mean", "median", "max"])
print("\nSalary stats by department:\n", dept_salary_stats)

# -------------------------
# Pivot Table
# -------------------------
pivot = pd.pivot_table(
    df,
    values="salary",
    index="department",
    columns="performance_rating",
    aggfunc="mean"
)

print("\nPivot Table:\n", pivot)

# -------------------------
# Feature Engineering
# -------------------------

# Salary ranking (1 = highest salary)
df["salary_rank"] = df["salary"].rank(ascending=False)

# Experience-based level
df["level"] = np.where(df["experience_years"] >= 10, "Senior", "Junior")

# Department distribution
dept_distribution = df["department"].value_counts(normalize=True)
print("\nDepartment distribution:\n", dept_distribution)

# -------------------------
# Visualization
# -------------------------
sns.set_style("whitegrid")

# 1. Salary distribution
plt.figure(figsize=(8,5))
sns.histplot(df["salary"], kde=True)
plt.title("Salary Distribution")
plt.show()

# 2. Experience vs Salary
plt.figure(figsize=(8,5))
sns.scatterplot(x="experience_years", y="salary", hue="department", data=df)
plt.title("Experience vs Salary by Department")
plt.show()

# 3. Average Salary by Department
plt.figure(figsize=(8,5))
sns.barplot(x="department", y="salary", data=df)
plt.title("Average Salary by Department")
plt.show()

# 4. Salary spread by Department
plt.figure(figsize=(8,5))
sns.boxplot(x="department", y="salary", data=df)
plt.title("Salary Spread by Department")
plt.show()