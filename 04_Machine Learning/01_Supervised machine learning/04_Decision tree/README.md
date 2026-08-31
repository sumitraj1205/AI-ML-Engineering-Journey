# Decision Tree — From Scratch

This folder contains an implementation of **Decision Tree algorithms from scratch**, covering both:

* **Decision Tree Classifier**
* **Decision Tree Regressor**

The implementation focuses on understanding how Decision Trees make decisions, select the best features and split points, recursively build a tree, and make predictions.

---

## 📌 What is a Decision Tree?

A Decision Tree is a **supervised machine learning algorithm** that can be used for both **classification** and **regression** problems.

It works by repeatedly splitting the dataset based on feature values to create smaller and more homogeneous groups.

A Decision Tree can be visualized as a series of questions:

```text
                Feature 1 < 5?
                 /        \
               Yes         No
               /            \
        Feature 2 < 10?     Class 1
          /      \
        Yes       No
        /          \
    Class 0       Class 1
```

The tree consists of:

* **Root Node** — The first and most important split
* **Internal Nodes** — Further decisions/splits
* **Branches** — Outcomes of decisions
* **Leaf Nodes** — Final predictions

---

# 🌳 How a Decision Tree Works

The general process is:

```text
              Training Data
                   ↓
          Find the Best Split
                   ↓
          Split the Dataset
             /           \
            /             \
        Left Node       Right Node
            ↓               ↓
     Find Best Split   Find Best Split
            ↓               ↓
          Repeat Recursively
                   ↓
               Leaf Nodes
                   ↓
               Prediction
```

The algorithm keeps splitting the data until a stopping condition is reached.

---

# 🔹 Decision Tree Classifier

A **Decision Tree Classifier** is used when the target variable is categorical.

For example:

```text
Target:

0 → Not Spam
1 → Spam
```

The tree learns rules that separate different classes.

### Example

```text
        Age < 30?
        /       \
      Yes        No
      /           \
 Income < 50K?   Class 1
   /     \
Class 0  Class 1
```

The final leaf contains the predicted class.

---

# 📊 Splitting Criteria for Classification

The classifier can use measures such as:

### Gini Impurity

Gini impurity measures how mixed the classes are within a node.

```text
Gini = 1 - Σ(pᵢ²)
```

where `pᵢ` represents the proportion of samples belonging to class `i`.

A node containing only one class has:

```text
Gini = 0
```

which means the node is completely pure.

---

### Entropy

Entropy measures the amount of uncertainty or impurity in a node.

```text
Entropy = -Σ pᵢ log₂(pᵢ)
```

Lower entropy means the node is more pure.

The tree chooses splits that provide better class separation.

---

# 🔹 Decision Tree Regressor

A **Decision Tree Regressor** is used when the target variable is continuous.

For example:

```text
House Price
₹25,00,000
₹32,00,000
₹45,00,000
₹52,00,000
```

Instead of predicting a class, the tree predicts a numerical value.

Example:

```text
             Area < 1500?
              /       \
            Yes        No
            /           \
       ₹35,00,000     ₹65,00,000
```

The prediction at a leaf is generally based on the target values of the training samples that reach that leaf.

---

# 📈 Splitting Criteria for Regression

Regression trees commonly use measures based on the error within a node.

### Mean Squared Error (MSE)

```text
MSE = (1/n) Σ(yᵢ - ŷ)²
```

where:

* `yᵢ` = actual value
* `ŷ` = predicted value
* `n` = number of samples

The tree searches for splits that reduce the prediction error.

---

# 🔄 Classification vs Regression

| Feature          | Classifier        | Regressor            |
| ---------------- | ----------------- | -------------------- |
| Problem          | Classification    | Regression           |
| Target           | Categorical       | Continuous           |
| Example          | Spam / Not Spam   | House Price          |
| Common Criterion | Gini / Entropy    | MSE                  |
| Leaf Output      | Class             | Numerical value      |
| Prediction       | Most common class | Average target value |

---

# ⚙️ Core Implementation

The implementation covers the major components required to build Decision Trees.

### Main Components

* Finding the best feature
* Finding split points
* Splitting the dataset
* Calculating impurity/error
* Recursive tree construction
* Creating leaf nodes
* Stopping conditions
* Making predictions
* Classification
* Regression

---

# 🌱 Recursive Tree Building

One of the most important concepts in a Decision Tree is **recursion**.

After finding the best split:

```text
              Dataset
                 |
          Best Feature/Split
            /           \
           /             \
       Left Data       Right Data
          |                |
    Build Subtree    Build Subtree
          |                |
         ...              ...
```

The same process is repeated for each child node.

This continues until a stopping condition is reached.

---

# 🛑 Stopping Conditions

Without restrictions, a Decision Tree can continue splitting until it memorizes the training data.

This can lead to **overfitting**.

Common stopping conditions include:

* Maximum tree depth
* Minimum number of samples required for a split
* Minimum number of samples in a leaf
* No useful split remaining
* Node becomes sufficiently pure

These parameters control the complexity of the tree.

---

# 🎯 Overfitting

Decision Trees are particularly prone to overfitting when they are allowed to grow too deep.

For example:

```text
Small Tree
    ↓
May underfit

Very Large Tree
    ↓
May overfit

Properly Controlled Tree
    ↓
Better Generalization
```

Parameters such as `max_depth`, `min_samples_split`, and `min_samples_leaf` can help control this.

---

# 🔮 Prediction

Once the tree has been trained, a new sample is passed through the decision rules.

For example:

```text
New Sample
    ↓
Feature 1 < 10?
    ↓
   Yes
    ↓
Feature 2 > 5?
    ↓
   Yes
    ↓
Leaf Node
    ↓
Prediction
```

The process continues until the sample reaches a leaf node.

---

# 📁 Folder Structure

```text
Decision Tree/
│
├── Decision_Tree_Classifier.ipynb
├── Decision_Tree_Regressor.ipynb
└── README.md
```

The notebooks contain the implementations and experiments for both the classification and regression versions of the algorithm.

---

# 🛠️ Technologies Used

* Python
* NumPy
* Pandas
* Matplotlib
* Scikit-learn

The Decision Tree algorithms are implemented to understand their internal working rather than relying entirely on the pre-built estimator.

---

# 🎯 Learning Objectives

Through this implementation, the following concepts are explored:

* Decision Tree architecture
* Recursive tree construction
* Feature selection
* Finding optimal split points
* Gini Impurity
* Entropy
* Mean Squared Error
* Classification trees
* Regression trees
* Leaf node prediction
* Tree depth
* Stopping conditions
* Overfitting
* Model prediction

---

# 🚀 Key Takeaway

Implementing Decision Trees provides a deeper understanding of how tree-based machine learning algorithms make decisions.

The overall process can be summarized as:

```text
                Input Data
                    ↓
             Find Best Split
                    ↓
             Split the Data
                    ↓
            Build Sub-Trees
                    ↓
          Apply Stopping Conditions
                    ↓
                Leaf Nodes
                    ↓
               Prediction
```

The same fundamental tree-building process can be adapted for different tasks:

```text
Decision Tree
      │
      ├── Classifier
      │      └── Predicts Classes
      │
      └── Regressor
             └── Predicts Numerical Values
```

This implementation helped develop a practical understanding of **recursive algorithms, impurity/error measures, feature splitting, and the fundamentals behind tree-based machine learning models**.
