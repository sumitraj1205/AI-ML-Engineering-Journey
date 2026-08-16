# 🛍️ Customer Product Recommendation System

A simple **rule-based product recommendation system built with Python** that processes customer data, performs basic data cleaning and analysis, and recommends a product brand based on customer ratings.

## 📌 Project Overview

This project demonstrates how raw customer data can be transformed into useful information using Python.

The workflow includes:

**Raw JSON Data → Data Cleaning → Data Analysis → Product Recommendation**

The system:

* Loads customer data from a JSON file
* Cleans and normalizes customer ratings
* Converts word-based ratings into numerical values
* Handles missing values
* Removes duplicate customers
* Calculates customer rating statistics
* Generates product recommendations based on ratings

## ⚙️ How It Works

### 1. Load Data

Customer information is loaded from a `data.json` file using Python's built-in `json` module.

### 2. Clean Data

The dataset is cleaned by:

* Removing unnecessary spaces
* Converting ratings such as `four` and `five` into numbers
* Handling missing age values
* Removing duplicate customers

### 3. Analyze Customer Ratings

The project calculates:

* Average customer rating
* Percentage of low ratings

For the current dataset:

```text
Average Rating: 3.9
Low Rating Percentage: 20.0%
```

### 4. Generate Recommendations

A simple rule-based recommendation system is used:

| Rating | Recommendation |
| :----: | :------------: |
|   ≤ 4  |    🍎 Apple    |
|   > 4  |   📱 Samsung   |

Example:

```text
Alice   → Samsung
Bob     → Apple
Charlie → Apple
Diana   → Samsung
Eve     → Apple
```

## 🧠 Recommendation Approach

The recommendation is currently **rule-based**, rather than machine-learning-based.

The basic logic is:

```python
if rating <= 4:
    recommendation = "Apple"
else:
    recommendation = "Samsung"
```

This makes the project useful for understanding the fundamentals of building a recommendation workflow before moving toward more advanced recommendation algorithms.

## 🛠️ Technologies Used

* **Python 3**
* **JSON**
* Python Lists & Dictionaries
* Functions
* Data Cleaning
* Basic Data Analysis
* Rule-Based Recommendation

## 📂 Project Structure

```text
Customer-Recommendation-System/
│
├── customer.ipynb
├── data.json
└── README.md
```

## 📊 Sample Dataset

The project works with customer information containing fields such as:

```text
Name
Rating
Feedback
Age
```

Example:

```json
{
    "name": "Alice",
    "rating": "5",
    "feedback": "Great product!!",
    "age": "25"
}
```

## 🎯 Key Learning Outcomes

This project helped me practice:

* Reading JSON data using Python
* Data cleaning and preprocessing
* Handling missing values
* Removing duplicate records
* Working with lists, dictionaries, and sets
* Writing reusable functions
* Performing basic statistical analysis
* Building a simple recommendation system

## 🚀 Future Improvements

The current system is intentionally simple. It can be extended by:

* Using a larger customer dataset
* Adding product categories
* Considering customer feedback
* Including purchase history
* Using customer preferences
* Implementing collaborative filtering
* Building a machine-learning-based recommendation system

## 👨‍💻 Author

Sumit

This project is part of my **AI/ML learning journey**, where I am building projects to strengthen my Python, data analysis, and machine learning fundamentals.
