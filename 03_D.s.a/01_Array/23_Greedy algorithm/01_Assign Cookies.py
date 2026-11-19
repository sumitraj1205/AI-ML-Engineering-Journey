# Problem: Assign Cookies
# Approach: Greedy + Sorting
# Time Complexity: O(n log n + m log m)
# Space Complexity: O(1) auxiliary space (excluding sorting)

class Solution:
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()

        i = 0  # Children pointer
        j = 0  # Cookies pointer

        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                i += 1

            j += 1

        return i


s = Solution()
print(s.findContentChildren([1, 2, 3], [1, 1]))
