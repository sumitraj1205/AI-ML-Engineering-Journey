# Problem: Check for Balanced Parentheses
# Approach: Use Stack
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def isValid(self, s):
        stack = []

        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for ch in s:
            if ch in '({[':
                stack.append(ch)

            else:
                if not stack or stack[-1] != pairs[ch]:
                    return False

                stack.pop()

        return len(stack) == 0

s = Solution()

print(s.isValid("()[]{}"))  # True
print(s.isValid("([)]"))    # False