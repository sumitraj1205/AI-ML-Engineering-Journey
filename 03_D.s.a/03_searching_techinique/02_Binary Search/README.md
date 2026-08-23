# Binary Search

## Problem

Given a sorted array and a target element `X`, find the index of `X` using Binary Search.

If `X` is not present, return `-1`.

## Approach

Binary Search repeatedly divides the sorted search space into two halves.

- Find the middle element.
- If it is equal to `X`, return its index.
- If it is smaller than `X`, search the right half.
- If it is greater than `X`, search the left half.
- Continue until the element is found or the search space becomes empty.

## Complexity

- Time Complexity: O(log n)
- Space Complexity: O(1)