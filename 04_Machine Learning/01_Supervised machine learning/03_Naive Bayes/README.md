# Naive Bayes Classification

This folder contains an implementation of the **Naive Bayes Classification algorithm** using Python.

The implementation focuses on understanding how Naive Bayes works internally, including probability calculation, Bayes' theorem, feature likelihoods, class priors, prediction, and model evaluation.

---

## 📌 What is Naive Bayes?

Naive Bayes is a **supervised machine learning algorithm** used primarily for classification problems.

It is based on **Bayes' Theorem** and assumes that the features are conditionally independent given the class.

The algorithm calculates the probability of each possible class given the input features and selects the class with the highest probability.

---

## 🧠 Why is it called "Naive"?

The algorithm makes a **naive assumption** that all features are independent of each other given the target class.

For example, in a spam classification problem, features such as:

```text
"free"
"offer"
"money"
"click"
```

are treated as conditionally independent when calculating the probability of spam.

Although this assumption is often not completely true in real-world data, Naive Bayes can still perform very well on many classification tasks.

---

## 🔢 Bayes' Theorem

The basic idea is:

```text
Posterior Probability
        =
Likelihood × Prior
-------------------
     Evidence
```

Where:

* **Prior** → Probability of the class before observing the features
* **Likelihood** → Probability of observing the features given the class
* **Evidence** → Overall probability of observing the features
* **Posterior** → Probability of the class given the observed features

---

## ⚙️ Implementation

The implementation covers the major steps involved in building a Naive Bayes classifier.

### Main Components

* Data preprocessing
* Class probability calculation
* Prior probability calculation
* Feature likelihood calculation
* Conditional probability
* Naive Bayes probability calculation
* Prediction
* Model evaluation

---

## 🔹 1. Calculate Class Priors

The prior probability of a class is calculated from the training data.

For example, if:

```text
Class 0 → 60 samples
Class 1 → 40 samples
```

then:

```text
P(Class 0) = 60 / 100
P(Class 1) = 40 / 100
```

These probabilities represent how frequently each class occurs in the dataset.

---

## 🔹 2. Calculate Likelihood

The likelihood represents the probability of observing a particular feature value given a class.

Conceptually:

```text
P(feature | class)
```

For multiple features, Naive Bayes assumes conditional independence and combines their probabilities.

---

## 🔹 3. Calculate Posterior Probability

For a given input sample, the model calculates the probability of the sample belonging to each class.

The class with the highest posterior probability becomes the prediction.

```text
Input Features
      ↓
Calculate Prior
      ↓
Calculate Likelihood
      ↓
Combine Probabilities
      ↓
Calculate Posterior
      ↓
Select Highest Probability
      ↓
Predicted Class
```

---

## 🔹 4. Prediction

For every input sample, the model evaluates all possible classes.

For example:

```text
P(Class 0 | X) = 0.25
P(Class 1 | X) = 0.75
```

Therefore:

```text
Prediction = Class 1
```

---

## 🛡️ Handling Zero Probabilities

A probability of zero can cause the entire probability calculation to become zero when probabilities are multiplied together.

To avoid this problem, **Laplace smoothing** can be used.

Instead of:

```text
count / total
```

the smoothed probability becomes:

```text
(count + 1) / (total + number_of_possible_values)
```

This prevents unseen feature values from completely eliminating a class.

---

## 📊 Model Pipeline

```text
              Training Data
                    ↓
             Calculate Classes
                    ↓
             Calculate Priors
                    ↓
          Calculate Likelihoods
                    ↓
            Apply Bayes Theorem
                    ↓
              Make Prediction
                    ↓
            Evaluate Performance
```

---

## 🧪 Example

Suppose we want to classify an email as:

```text
Spam
Not Spam
```

The model calculates:

```text
P(Spam | features)
P(Not Spam | features)
```

If:

```text
P(Spam | features) > P(Not Spam | features)
```

the model predicts:

```text
Spam
```

Otherwise:

```text
Not Spam
```

---

## 📈 Evaluation

The model can be evaluated using metrics such as:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix

These metrics help understand how well the classifier performs on unseen data.

---

## 📁 Folder Structure

```text
Naive Bayes/
│
├── Naive_Bayes_Classification.ipynb
│
└── README.md
```

---

## 🛠️ Technologies Used

* Python
* NumPy
* Pandas
* Matplotlib
* Scikit-learn

Scikit-learn can be used for dataset handling and evaluation, while the Naive Bayes algorithm is implemented to understand its internal working.

---

## 🎯 Learning Objectives

Through this implementation, the following concepts are explored:

* Bayes' Theorem
* Conditional Probability
* Prior Probability
* Likelihood
* Posterior Probability
* Conditional Independence
* Laplace Smoothing
* Classification
* Model Evaluation

---

## 🚀 Key Takeaway

Implementing Naive Bayes from scratch helps understand how probability-based classification works internally.

Instead of simply using a pre-built classifier, the implementation breaks the algorithm down into its fundamental components:

```text
Features
   ↓
Prior Probability
   ↓
Likelihood
   ↓
Bayes' Theorem
   ↓
Posterior Probability
   ↓
Highest Probability
   ↓
Prediction
```

This provides a practical understanding of the relationship between **probability, mathematics, and machine learning classification**.
