## 1. What is Machine Learning?

Machine Learning (ML) is a field of Artificial Intelligence that enables computers to learn patterns from data without being explicitly programmed.

Instead of writing fixed rules, the system learns from examples and improves its performance over time.


---

## 2. Main Types of Machine Learning

### 1. Supervised Learning
- Training data contains input and correct output (label)
- Model learns mapping from input to output

Example:
- Email classification (spam / not spam)
- House price prediction


### 2. Unsupervised Learning
- Training data contains only inputs (no labels)
- Model finds hidden patterns or structure in data

Example:
- Customer segmentation
- Clustering similar data points


### 3. Reinforcement Learning
- Learning based on reward and punishment
- An agent interacts with an environment

Example:
- Game playing AI
- Robotics control systems


---

## 3. Classification vs Regression

### Classification
- Predicts categorical values (classes)
- Output is discrete

Example:
- Spam or Not Spam
- Cat or Dog


### Regression
- Predicts continuous numerical values
- Output is a real number

Example:
- House price prediction
- Temperature prediction


---

## 4. Feature in Machine Learning

A feature is an input variable used by the model for prediction.

Example:
For house price prediction:
- Size
- Number of rooms
- Location

Features represent the input information used for learning.


---

## 5. Label / Target Variable

A label (or target variable) is the output that the model is trying to predict.

Example:
For house price prediction:
- Label = Price of the house

For spam detection:
- Label = Spam or Not Spam

The label is the answer the model learns from the features.

## 1. Overfitting and Underfitting

### Overfitting
Overfitting occurs when a model learns the training data too well, including noise and irrelevant patterns.

- High accuracy on training data
- Poor performance on new/unseen data

### Underfitting
Underfitting occurs when a model is too simple to learn the underlying patterns in the data.

- Poor performance on training data
- Poor performance on testing data

### Key Idea
- Overfitting → model is too complex
- Underfitting → model is too simple
- Good model → balanced learning


---

## 2. Supervised vs Unsupervised Learning

### Supervised Learning
- Data contains input and correct output (labels)
- Model learns mapping from input to output

Example:
- Classification
- Regression

### Unsupervised Learning
- Data contains only inputs (no labels)
- Model finds hidden patterns or structure

Example:
- Clustering
- Grouping similar data points


---

## 3. Training and Testing Dataset

### Training Dataset
- Used to train the model
- Model learns patterns from this data

### Testing Dataset
- Used to evaluate model performance
- Model does not see this data during training

### Importance of Data Splitting
- Prevents overfitting
- Helps measure real-world performance
- Ensures generalization


---

## 4. Feature Scaling

Feature scaling is the process of normalizing or standardizing features so they are in a similar range.

### Why it is needed
- Prevents large-valued features from dominating
- Improves performance of distance-based and gradient-based algorithms

### Common methods
- Normalization (0 to 1 range)
- Standardization (mean = 0, std = 1)


---

## 5. Linear Regression

Linear Regression is a supervised learning algorithm used to predict continuous values.

It models the relationship between input and output using a linear equation:

Output = slope × input + intercept

### Working
- Finds the best-fit line
- Minimizes error between predicted and actual values
- Uses the line for future predictions

### Example
- House price prediction
- Salary prediction based on experience