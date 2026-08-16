# 🌸 Pandas Assignment – Iris Dataset

## 📌 Overview

This assignment focuses on practical **data exploration and analysis using Pandas** with the **Iris Flower Dataset**.

The assignment covers data inspection, filtering, grouping, statistical analysis, and creating a new calculated column.

## 🎯 Tasks Covered

### 1. Dataset Exploration

* Display the first 10 rows
* Check the shape of the dataset
* Display data types
* Generate summary statistics including:

  * Mean
  * Standard deviation
  * Minimum
  * Maximum

### 2. Data Filtering

Select flowers where:

* `petal_length > 4.5`
* `species = "Iris-virginica"`

### 3. Grouping and Aggregation

Group the data by `species` and calculate:

* Average `sepal_length`
* Maximum `petal_width`
* Standard deviation of `sepal_width`

### 4. Feature Creation

Create a new column:

```text
petal_ratio = petal_length / petal_width
```

Then calculate the **average petal ratio for each species**.

## 🛠️ Technologies Used

* Python
* Pandas
* Jupyter Notebook

## 📂 Project Structure

```text
Pandas-Iris-Assignment/
│
├── iris_assignment.ipynb
└── README.md
```

## 📚 Learning Outcomes

Through this assignment, I practiced:

* Loading and exploring datasets with Pandas
* Filtering rows based on conditions
* Grouping data using `groupby()`
* Performing aggregate operations
* Calculating summary statistics
* Creating new DataFrame columns
* Performing basic data analysis with Pandas

