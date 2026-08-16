# Remove Duplicates from Sorted Array

## Problem

Given a sorted array, remove the duplicate elements in-place so that each unique element appears only once.

## Approach

* Use two pointers, `i` and `j`.
* `j` points to the position of the last unique element.
* Traverse the array using `i`.
* If `arr[i]` is different from `arr[j]`, move `j` forward and store the new unique element.
* Return the number of unique elements.

## Example

**Input:**

```text
[1, 1, 2, 2, 3, 4, 4, 5]
```

**Output:**

```text
[1, 2, 3, 4, 5]
```

## Complexity

* **Time Complexity:** O(n)
* **Space Complexity:** O(1)

