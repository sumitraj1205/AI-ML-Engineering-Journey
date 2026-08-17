# Right Rotate an Array by K Places

## Problem

Given an array and an integer `k`, rotate the array to the right by `k` positions.

## Approach

* Find the length of the array.
* Use `k % n` to handle cases where `k` is greater than the array length.
* Take the last `k` elements and place them at the beginning.
* Append the remaining elements after them.

## Example

**Input:**

```text
Array = [1, 2, 3, 4, 5]
K = 2
```

**Output:**

```text
[4, 5, 1, 2, 3]
```

## Complexity

* **Time Complexity:** O(n)
* **Space Complexity:** O(n)


