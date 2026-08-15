# Second Largest Element in an Array

## Problem

Given an array of integers, find the **second largest element** in the array.

### Example

**Input:**

```text
[10, 5, 8, 20, 15]
```

**Output:**

```text
15
```

### Approach

We can find the second largest element in a **single traversal** of the array.

* Keep track of the largest element.
* Keep track of the second largest element.
* For every element:

  * If it is greater than the largest, update both values.
  * Otherwise, if it is smaller than the largest but greater than the second largest, update the second largest.

### Complexity

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(1)`
