# Move Zeros to End

## Problem

Given an array containing zero and non-zero elements, move all the zeros to the end of the array while maintaining the relative order of the non-zero elements.

## Approach

* Use a pointer `j` to track the position where the next non-zero element should be placed.
* Traverse the array using `i`.
* Whenever a non-zero element is found, swap it with the element at position `j`.
* Increment `j`.
* After traversal, all zeros will be moved to the end.

## Example

**Input:**

```text
[1, 0, 2, 0, 3, 0, 4]
```

**Output:**

```text
[1, 2, 3, 4, 0, 0, 0]
```

## Complexity

* **Time Complexity:** O(n)
* **Space Complexity:** O(1)
