# Problem: Postfix to Prefix Conversion
# Approach: Stack (Left to Right)
# Time Complexity: O(n^2) due to string concatenation
# Space Complexity: O(n^2) for intermediate expressions

class Solution:
    def postfixToPrefix(self, s):
        stack = []

        for ch in s:
            if ch.isalnum():
                stack.append(ch)

            else:
                b = stack.pop()
                a = stack.pop()

                expression = ch + a + b
                stack.append(expression)

        return stack[-1]


s = Solution()
print(s.postfixToPrefix("AB+CD-*"))  