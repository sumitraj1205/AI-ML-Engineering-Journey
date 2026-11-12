# Problem: Prefix to Postfix Conversion
# Approach: Stack (Right to Left)
# Time Complexity: O(n^2) due to string concatenation
# Space Complexity: O(n^2) for intermediate expressions

class Solution:
    def prefixToPostfix(self, s):
        stack = []

        for ch in reversed(s):
            if ch.isalnum():
                stack.append(ch)

            else:
                a = stack.pop()
                b = stack.pop()

                expression = a + b + ch
                stack.append(expression)

        return stack[-1]


s = Solution()
print(s.prefixToPostfix("*+AB-CD"))  