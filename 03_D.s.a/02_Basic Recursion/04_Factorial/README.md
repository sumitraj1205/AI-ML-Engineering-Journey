# Factorial of a Number Using Recursion

## Problem

Given a positive integer `N`, find its factorial using recursion.

The factorial of a number is the product of all positive integers from `1` to `N`.

## Approach

* If `N` is `0` or `1`, return `1`.
* Multiply `N` with the factorial of `N - 1`.
* Continue until the base case is reached.

The recursive relation is:

```text
factorial(n) = n × factorial(n - 1)
```

## Example

**Input:**

```text
5
```

**Output:**

```text
120
```

## Complexity

* **Time Complexity:** O(n)
* **Space Complexity:** O(n)


