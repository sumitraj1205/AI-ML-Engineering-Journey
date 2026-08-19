# Maximum Consecutive Ones

## Problem

Given a binary array containing only `0` and `1`, find the maximum number of consecutive `1`s in the array.

## Approach

* Initialize a counter to keep track of consecutive `1`s.
* Traverse the array.
* If the current element is `1`, increase the counter.
* If the current element is `0`, reset the counter to `0`.
* Keep track of the maximum count obtained.

## Example

**Input:**

```text
[1, 1, 0, 1, 1, 1, 0, 1]
```

**Output:**

```text
3
```

## Complexity

* **Time Complexity:** O(n)
* **Space Complexity:** O(1)

