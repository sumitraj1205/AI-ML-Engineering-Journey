# Sum of First N Natural Numbers Using Recursion

## Problem

Given a positive integer `N`, find the sum of the first `N` natural numbers using recursion.

## Approach

* If `N` becomes `0`, return `0`.
* Add `N` to the result of `sum_n(n - 1)`.
* Continue until the base case is reached.

The recursive relation is:

```text
sum(n) = n + sum(n - 1)
```

## Example

**Input:**

```text
5
```

**Output:**

```text
15
```

## Complexity

* **Time Complexity:** O(n)
* **Space Complexity:** O(n)


