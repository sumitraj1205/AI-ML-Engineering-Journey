# Problem: Infix to Postfix Conversion
# Approach: Stack
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def infixToPostfix(self, s):
        stack = []
        result = []

        precedence = {
            '^': 3,
            '*': 2,
            '/': 2,
            '+': 1,
            '-': 1
        }

        for ch in s:
            if ch.isalnum():
                result.append(ch)

            elif ch == '(':
                stack.append(ch)

            elif ch == ')':
                while stack and stack[-1] != '(':
                    result.append(stack.pop())
                stack.pop()

            else:
                while (stack and stack[-1] != '(' and
                       (precedence[stack[-1]] > precedence[ch] or
                        (precedence[stack[-1]] == precedence[ch]
                         and ch != '^'))):
                    result.append(stack.pop())

                stack.append(ch)

        while stack:
            result.append(stack.pop())

        return ''.join(result)


s = Solution()
print(s.infixToPostfix("A+B*(C-D)"))  