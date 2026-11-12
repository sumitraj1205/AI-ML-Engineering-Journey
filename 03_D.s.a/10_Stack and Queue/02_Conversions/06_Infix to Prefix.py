# Problem: Infix to Prefix Conversion
# Approach: Reverse + Infix to Postfix + Reverse
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def infixToPrefix(self, s):
        s = s[::-1]

        # Swap brackets
        s = ''.join(
            ')' if ch == '(' else
            '(' if ch == ')' else ch
            for ch in s
        )

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
                         and ch == '^'))):
                    result.append(stack.pop())

                stack.append(ch)

        while stack:
            result.append(stack.pop())

        return ''.join(result[::-1])


s = Solution()
print(s.infixToPrefix("A+B*(C-D)"))  