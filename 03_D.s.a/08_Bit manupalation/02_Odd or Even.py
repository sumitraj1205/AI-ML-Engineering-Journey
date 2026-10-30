# Problem: Check whether a number is odd or even.
# Approach: Check the rightmost bit using AND with 1.
# Time Complexity: O(1)
# Space Complexity: O(1)

def check_odd_even(n):
    if n & 1:
        return "Odd"
    return "Even"


n = 15
print(check_odd_even(n))