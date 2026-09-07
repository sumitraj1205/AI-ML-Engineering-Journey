# Support Vector Machine (SVM)

This folder contains my implementation and practice of **Support Vector Machine (SVM)** algorithms using Python and Scikit-learn.

## Topics Covered

* SVM Classification
* SVM Regression
* Linear Kernel
* Polynomial Kernel
* RBF Kernel
* Hyperparameter tuning
* Model evaluation

## 1. SVM Classification

SVM Classification is used for **classification problems** where the model tries to find the best boundary (hyperplane) that separates different classes.

Example:

* Classifying emails as Spam / Not Spam
* Predicting whether a customer will churn or not
* Classifying different types of data

Main parameters used:

```python
SVC(
    kernel='rbf',
    C=1.0,
    gamma='scale'
)
```

## 2. SVM Regression

SVM can also be used for **regression problems** using Support Vector Regression (SVR).

Instead of separating classes, SVR tries to find a function that predicts continuous values while keeping most data points within a certain margin.

Example:

* House price prediction
* Sales prediction
* Temperature prediction

Main parameters used:

```python
SVR(
    kernel='rbf',
    C=1.0,
    epsilon=0.1
)
```

## Libraries Used

* Python
* NumPy
* Pandas
* Matplotlib
* Scikit-learn

## Files

```text
SVM/
│
├── SVM_Classification.ipynb
├── SVM_Regression.ipynb
└── README.md
```

## What I Learned

* How SVM works for classification and regression
* Difference between SVC and SVR
* Importance of feature scaling in SVM
* Different types of kernels
* Effect of `C`, `gamma` and `epsilon`
* How to evaluate SVM models

This folder contains my learning, implementation and practice of **SVM from scratch concepts and using Scikit-learn**.
