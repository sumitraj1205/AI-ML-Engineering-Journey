# Find Missing Number in an Array

## Problem

Given an array containing `n - 1` numbers from `1` to `n`, find the missing number.

## Approach

* Calculate the expected sum of numbers from `1` to `n`.
* Calculate the sum of all elements present in the array.
* Subtract the array sum from the expected sum.
* The difference is the missing number.

Formula:

```text
Sum = n × (n + 1) / 2
```

## Example

**Input:**

```text
[1, 2, 3, 5]
```

**Output:**

```text
4
```

## Complexity

* **Time Complexity:** O(n)
* **Space Complexity:** O(1)

