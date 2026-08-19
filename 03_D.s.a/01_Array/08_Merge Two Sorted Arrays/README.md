# Merge Two Sorted Arrays

## Problem

Given two sorted arrays, merge them into a single sorted array.

## Approach

* Use two pointers, one for each array.
* Compare the elements pointed to by both pointers.
* Add the smaller element to the result array.
* Continue until one array is completely traversed.
* Add the remaining elements of the other array.
* The final array will be sorted.

## Example

**Input:**

```text
arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
```

**Output:**

```text
[1, 2, 3, 4, 5, 6, 7, 8]
```

## Complexity

* **Time Complexity:** O(n + m)
* **Space Complexity:** O(n + m)

