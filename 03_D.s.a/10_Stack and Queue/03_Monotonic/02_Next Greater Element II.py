# Problem: Next Greater Element II
# Approach: Monotonic Stack + Circular Traversal
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def nextGreaterElements(self, nums):
        n = len(nums)
        result = [-1] * n
        stack = []

        for i in range(2 * n - 1, -1, -1):
            index = i % n

            while stack and stack[-1] <= nums[index]:
                stack.pop()

            if i < n and stack:
                result[index] = stack[-1]

            stack.append(nums[index])

        return result


s = Solution()
print(s.nextGreaterElements([1, 2, 1]))