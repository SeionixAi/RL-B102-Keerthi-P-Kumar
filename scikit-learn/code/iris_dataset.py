import numpy as np
import matplotlib.pyplot as plt

# Dataset
from sklearn.datasets import load_iris

# Train test split
from sklearn.model_selection import train_test_split

# Models
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

# Metrics
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

# Preprocessing
from sklearn.preprocessing import (
    StandardScaler,
    LabelEncoder
)

# Cross validation
from sklearn.model_selection import (
    cross_val_score,
    learning_curve
)

# Pipeline
from sklearn.pipeline import Pipeline


# ==================================
# 1. LOAD DATASET
# ==================================
iris = load_iris()

X = iris.data
y = iris.target

print("Feature Shape:", X.shape)
print("Target Shape:", y.shape)

print("\nFirst 5 Features")
print(X[:5])

print("\nFirst 5 Labels")
print(y[:5])


# ==================================
# 2. TRAIN TEST SPLIT
# ==================================
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Shape:", X_train.shape)
print("Testing Shape:", X_test.shape)


# ==================================
# 3. LOGISTIC REGRESSION MODEL
# ==================================
model = LogisticRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("\nPredictions:")
print(y_pred)


# ==================================
# 4. EVALUATION
# ==================================
print("\nAccuracy Score")
print(accuracy_score(y_test, y_pred))

print("\nConfusion Matrix")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report")
print(classification_report(y_test, y_pred))


# ==================================
# 5. STANDARDIZATION
# ==================================
scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

print("\nScaled Data Sample")
print(X_scaled[:5])


# ==================================
# 6. LABEL ENCODING
# ==================================
encoder = LabelEncoder()

y_encoded = encoder.fit_transform(y)

print("\nEncoded Labels")
print(y_encoded[:10])


# ==================================
# 7. DECISION TREE
# ==================================
tree = DecisionTreeClassifier()

tree.fit(X_train, y_train)

tree_pred = tree.predict(X_test)

print("\nDecision Tree Accuracy")
print(accuracy_score(y_test, tree_pred))


# ==================================
# 8. RANDOM FOREST
# ==================================
rf = RandomForestClassifier()

rf.fit(X_train, y_train)

rf_pred = rf.predict(X_test)

print("\nRandom Forest Accuracy")
print(accuracy_score(y_test, rf_pred))


# ==================================
# 9. CROSS VALIDATION
# ==================================
scores = cross_val_score(
    model,
    X,
    y,
    cv=5
)

print("\nCross Validation Scores")
print(scores)

print("Mean Accuracy:")
print(scores.mean())


# ==================================
# 10. PIPELINE
# ==================================
pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("classifier", LogisticRegression())
])

pipe.fit(X_train, y_train)

pipeline_pred = pipe.predict(X_test)

print("\nPipeline Accuracy")
print(accuracy_score(y_test, pipeline_pred))


# ==================================
# 11. LEARNING CURVE
# ==================================
train_sizes, train_scores, test_scores = learning_curve(
    model,
    X,
    y,
    cv=5,
    train_sizes=np.linspace(0.1, 1.0, 5)
)

plt.plot(
    train_sizes,
    train_scores.mean(axis=1),
    label="Train"
)

plt.plot(
    train_sizes,
    test_scores.mean(axis=1),
    label="Test"
)

plt.legend()

plt.title("Learning Curve")

plt.xlabel("Training Size")

plt.ylabel("Score")

plt.show()