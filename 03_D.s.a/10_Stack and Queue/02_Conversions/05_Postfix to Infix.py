# Problem: Postfix to Infix Conversion
# Approach: Stack (Left to Right)
# Time Complexity: O(n^2) due to string concatenation
# Space Complexity: O(n^2) for intermediate expressions

class Solution:
    def postfixToInfix(self, s):
        stack = []

        for ch in s:
            if ch.isalnum():
                stack.append(ch)

            else:
                b = stack.pop()
                a = stack.pop()

                expression = '(' + a + ch + b + ')'
                stack.append(expression)

        return stack[-1]


s = Solution()
print(s.postfixToInfix("AB+CD-*"))  