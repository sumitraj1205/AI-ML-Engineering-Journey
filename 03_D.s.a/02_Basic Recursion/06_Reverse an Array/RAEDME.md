# Reverse an Array Using Recursion

## Problem

Given an array, reverse its elements using recursion.

## Approach

* Use two pointers: `left` and `right`.
* Swap the elements at `left` and `right`.
* Move `left` one position forward and `right` one position backward.
* Repeat recursively.
* Stop when `left` becomes greater than or equal to `right`.

## Example

**Input:**

```text
[1, 2, 3, 4, 5]
```

**Output:**

```text
[5, 4, 3, 2, 1]
```

## Complexity

* **Time Complexity:** O(n)
* **Space Complexity:** O(n) due to the recursive call stack.


