# Problem: Max Consecutive Ones III
# Approach: Sliding Window
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def longestOnes(self, nums, k):
        left = 0
        zeros = 0
        maxi = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1

            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            maxi = max(maxi, right - left + 1)

        return maxi


s = Solution()
print(s.longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))