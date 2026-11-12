# Problem: Longest Substring Without Repeating Characters
# Approach: Sliding Window + Set
# Time Complexity: O(n)
# Space Complexity: O(min(n, charset))

class Solution:
    def lengthOfLongestSubstring(self, s):
        seen = set()
        left = 0
        maxi = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            maxi = max(maxi, right - left + 1)

        return maxi


s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb")) 