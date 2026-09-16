# Problem:
# Find the maximum nesting depth of parentheses in a valid parentheses string.
#
# Approach:
# Keep a variable depth.
# Increase it whenever '(' is found.
# Decrease it whenever ')' is found.
# Keep track of the maximum depth reached.
#
# Time Complexity: O(n)
# Space Complexity: O(1)


def max_depth(s):
    depth = 0
    maximum = 0

    for ch in s:
        if ch == '(':
            depth += 1
            maximum = max(maximum, depth)

        elif ch == ')':
            depth -= 1

    return maximum


s = "(1+(2*3)+((8)/4))+1"

print(max_depth(s))