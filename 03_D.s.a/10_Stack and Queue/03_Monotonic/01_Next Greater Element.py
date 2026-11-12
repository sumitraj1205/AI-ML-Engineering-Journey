# Problem: Next Greater Element
# Approach: Monotonic Decreasing Stack
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def nextGreaterElement(self, arr):
        n = len(arr)
        result = [-1] * n
        stack = []

        for i in range(n - 1, -1, -1):

            while stack and stack[-1] <= arr[i]:
                stack.pop()

            if stack:
                result[i] = stack[-1]

            stack.append(arr[i])

        return result


s = Solution()
print(s.nextGreaterElement([4, 5, 2, 10, 8]))