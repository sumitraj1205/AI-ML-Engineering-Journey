# Power of a Number Using Recursion

## Problem

Given a number `base` and an exponent `n`, calculate `base^n` using recursion.

## Approach

* If the exponent is `0`, return `1`.
* Multiply the base by the result of `power(base, exponent - 1)`.
* Continue until the exponent becomes `0`.

The recursive relation is:

```text
power(base, n) = base × power(base, n - 1)
```

## Example

**Input:**

```text
base = 2
exponent = 5
```

**Output:**

```text
32
```

## Complexity

* **Time Complexity:** O(n)
* **Space Complexity:** O(n) due to the recursive call stack.
