# Check if String is Palindrome Using Recursion

## Problem

Given a string, check whether it reads the same forwards and backwards using recursion.

## Approach

* Use two pointers, `left` and `right`.
* Compare the characters at both positions.
* If they are different, the string is not a palindrome.
* If they are the same, move both pointers towards the center.
* Stop when `left` becomes greater than or equal to `right`.

## Example

**Input:**

```text id="q6jv3e"
"madam"
```

**Output:**

```text id="z7p2yr"
Palindrome
```

## Complexity

* **Time Complexity:** O(n)
* **Space Complexity:** O(n) due to the recursive call stack.
