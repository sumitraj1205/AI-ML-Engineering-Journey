# Check if an Array is Sorted Using Recursion

## Problem

Given an array, check whether the elements are arranged in ascending order using recursion.

## Approach

* Compare the current element with the next element.
* If the current element is greater than the next element, the array is not sorted.
* Otherwise, recursively check the remaining elements.
* Stop when the last element is reached.

## Example

**Input:**

```text id="p6s9vx"
[1, 2, 3, 4, 5]
```

**Output:**

```text id="z0c8qa"
Array is sorted
```

## Complexity

* **Time Complexity:** O(n)
* **Space Complexity:** O(n) due to the recursive call stack.

