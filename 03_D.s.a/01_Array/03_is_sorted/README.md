# Check if Array is Sorted

## Problem

Given an array, check whether the elements are arranged in sorted order in ascending order.

## Approach

* Traverse the array from the first element to the second-last element.
* Compare each element with the next element.
* If `arr[i] > arr[i + 1]`, the array is not sorted.
* If no such pair is found, the array is sorted.

## Example

**Input:**

```text
[1, 2, 3, 4, 5]
```

**Output:**

```text
Array is sorted
```

## Complexity

* **Time Complexity:** O(n)
* **Space Complexity:** O(1)


