# Problem: Minimum Number of Platforms
# Approach: Greedy + Sorting + Two Pointers
# Time Complexity: O(n log n)
# Space Complexity: O(1) auxiliary space (excluding sorting)

class Solution:
    def findPlatform(self, arr, dep):
        arr.sort()
        dep.sort()

        n = len(arr)

        i = 1
        j = 0

        platforms = 1
        maxi = 1

        while i < n and j < n:

            # New train arrives before or at departure
            if arr[i] <= dep[j]:
                platforms += 1
                i += 1

            # A train departs, freeing a platform
            else:
                platforms -= 1
                j += 1

            maxi = max(maxi, platforms)

        return maxi


s = Solution()
print(s.findPlatform(
    [900, 940, 950, 1100, 1500, 1800],
    [910, 1200, 1120, 1130, 1900, 2000]
))