# Problem:
# Remove the outermost parentheses from every primitive valid parentheses string.
#
# Approach:
# Keep track of the parentheses depth.
# When '(' appears at depth 0, it is an outermost opening bracket, so skip it.
# When ')' makes the depth become 0, it is an outermost closing bracket, so skip it.
# Add all other parentheses to the result.
#
# Time Complexity: O(n)
# Space Complexity: O(n)


def remove_outer_parentheses(s):
    result = []
    depth = 0

    for ch in s:
        if ch == '(':
            if depth > 0:
                result.append(ch)
            depth += 1

        else:
            depth -= 1
            if depth > 0:
                result.append(ch)

    return ''.join(result)


s = "(()())(())"
print(remove_outer_parentheses(s))