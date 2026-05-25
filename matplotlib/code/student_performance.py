# =========================
# 1. IMPORT LIBRARIES
# =========================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =========================
# 2. CREATE DATASET
# =========================
np.random.seed(42)

df = pd.DataFrame({
    "student_id": range(1, 501),
    "study_hours": np.random.randint(1, 10, 500),
    "attendance": np.random.randint(50, 100, 500),
    "exam_score": np.random.randint(30, 100, 500)
})

# =========================
# 3. BASIC INSPECTION (EDA)
# =========================
print("HEAD:\n", df.head())
print("\nTAIL:\n", df.tail())
print("\nSAMPLE:\n", df.sample(5))
print("\nINFO:")
print(df.info())

print("\nDESCRIPTION:\n", df.describe())

print("\nMEAN VALUES:\n", df[["study_hours", "attendance", "exam_score"]].mean())

# =========================
# 4. FEATURE ENGINEERING
# =========================
df["performance"] = pd.cut(
    df["exam_score"],
    bins=[0, 50, 75, 100],
    labels=["Low", "Medium", "High"]
)

print("\nWITH PERFORMANCE COLUMN:\n", df.head())

# =========================
# 5. GROUP ANALYSIS
# =========================
group_analysis = df.groupby("performance")["exam_score"].agg(
    ["mean", "min", "max", "count"]
)

print("\nGROUP ANALYSIS:\n", group_analysis)

# =========================
# 6. FILTERING
# =========================
high_performers = df[(df["study_hours"] > 6) & (df["attendance"] > 80)]

print("\nHIGH PERFORMERS SAMPLE:\n", high_performers.head())

# =========================
# 7. SORTING
# =========================
top_students = df.sort_values("exam_score", ascending=False).head(10)

print("\nTOP 10 STUDENTS:\n", top_students)

# =========================
# 8. CORRELATION
# =========================
correlation = df.corr(numeric_only=True)
print("\nCORRELATION MATRIX:\n", correlation)

# =========================
# 9. VISUALIZATION
# =========================

# Pairplot
sns.pairplot(df[["study_hours", "attendance", "exam_score"]])
plt.show()

# Heatmap
sns.heatmap(correlation, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# Boxplot
sns.boxplot(x="performance", y="exam_score", data=df)
plt.title("Exam Score by Performance Category")
plt.show()

# Line Plot (Trend)
df_sorted = df.sort_values("study_hours")

plt.plot(df_sorted["study_hours"], df_sorted["exam_score"])
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.title("Study Hours vs Exam Score Trend")
plt.show()