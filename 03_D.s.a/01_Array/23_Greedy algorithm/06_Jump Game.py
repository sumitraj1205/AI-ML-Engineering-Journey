# Problem: Jump Game
# Approach: Greedy
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def canJump(self, nums):
        farthest = 0

        for i in range(len(nums)):

            if i > farthest:
                return False

            farthest = max(farthest, i + nums[i])

            if farthest >= len(nums) - 1:
                return True

        return True


s = Solution()
print(s.canJump([2, 3, 1, 1, 4])) 
print(s.canJump([3, 2, 1, 0, 4]))  