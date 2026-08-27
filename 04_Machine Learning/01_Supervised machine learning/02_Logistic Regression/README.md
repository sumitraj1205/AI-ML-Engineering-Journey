# Logistic Regression

This folder contains the implementation of **Logistic Regression**, including an implementation built **from scratch** to understand how Logistic Regression works internally.

The goal is not just to use the `scikit-learn` implementation, but to understand the mathematical intuition, functions, optimization process, and how predictions are generated.

---

## 📌 What is Logistic Regression?

Logistic Regression is a **supervised machine learning algorithm** primarily used for **classification problems**.

Unlike Linear Regression, which predicts a continuous numerical value, Logistic Regression predicts the **probability of an observation belonging to a particular class**.

For binary classification, the model predicts a probability between **0 and 1**.

For example:

- `0.85` → high probability of class 1
- `0.20` → high probability of class 0

A threshold is then used to convert the probability into a class prediction.

---

## ⚙️ How Logistic Regression Works

The basic workflow is:

```text
Input Features
      ↓
Linear Combination
      ↓
z = wX + b
      ↓
Sigmoid Function
      ↓
Probability
      ↓
Apply Threshold
      ↓
Class Prediction