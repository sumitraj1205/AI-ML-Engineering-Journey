# Right Rotate an Array by One Place

## Problem

Given an array, rotate all elements one position to the right.

The last element moves to the first position, and every other element moves one position to the right.

## Approach

* Store the last element of the array.
* Traverse the array from right to left.
* Shift each element one position to the right.
* Place the stored last element at the first position.

## Example

**Input:**

```text
[1, 2, 3, 4, 5]
```

**Output:**

```text
[5, 1, 2, 3, 4]
```

## Complexity

* **Time Complexity:** O(n)
* **Space Complexity:** O(1)


