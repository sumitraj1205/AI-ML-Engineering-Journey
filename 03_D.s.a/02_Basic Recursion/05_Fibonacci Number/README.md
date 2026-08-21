# Fibonacci Number Using Recursion

## Problem

Given a number `N`, find the `N`th Fibonacci number using recursion.

The Fibonacci sequence starts with:

```text id="k4t5bq"
0, 1, 1, 2, 3, 5, 8, 13, ...
```

Each number is the sum of the previous two numbers.

## Approach

* If `N` is `0` or `1`, return `N`.
* Otherwise, calculate the sum of the previous two Fibonacci numbers.
* Continue recursively until the base cases are reached.

The recursive relation is:

```text id="w9v5rm"
fibonacci(n) = fibonacci(n - 1) + fibonacci(n - 2)
```

## Example

**Input:**

```text id="8j2x2k"
6
```

**Output:**

```text id="v4z2kn"
8
```

## Complexity

* **Time Complexity:** O(2ⁿ)
* **Space Complexity:** O(n)


