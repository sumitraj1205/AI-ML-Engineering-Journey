# Print 1 to N Using Recursion

## Problem

Given a positive integer `N`, print all numbers from `1` to `N` using recursion.

## Approach

* If `N` becomes `0`, stop the recursion.
* Call the function with `N - 1`.
* Print `N` after the recursive call.
* This prints the numbers in ascending order.

## Example

**Input:**

```text
5
```

**Output:**

```text
1
2
3
4
5
```

## Complexity

* **Time Complexity:** O(n)
* **Space Complexity:** O(n)
