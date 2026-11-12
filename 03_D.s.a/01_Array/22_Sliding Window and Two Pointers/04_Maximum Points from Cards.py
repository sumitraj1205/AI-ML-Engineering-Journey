# Problem: Maximum Points You Can Obtain from Cards
# Approach: Sliding Window from Both Ends
# Time Complexity: O(k)
# Space Complexity: O(1)

class Solution:
    def maxScore(self, cardPoints, k):
        n = len(cardPoints)

        # Initially take k cards from the left
        total = sum(cardPoints[:k])
        maxi = total

        # Replace left cards with right cards
        for i in range(1, k + 1):
            total -= cardPoints[k - i]
            total += cardPoints[n - i]

            maxi = max(maxi, total)

        return maxi


s = Solution()
print(s.maxScore([1, 2, 3, 4, 5, 6, 1], 3))
