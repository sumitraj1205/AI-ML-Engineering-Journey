# Problem: Minimum Number of Coins
# Approach: Greedy + Sorting
# Time Complexity: O(d), where d is the number of denominations
# Space Complexity: O(d) for storing selected coins

class Solution:
    def minCoins(self, amount):
        coins = [1000, 500, 100, 50, 20, 10, 5, 2, 1]

        result = []

        for coin in coins:
            while amount >= coin:
                amount -= coin
                result.append(coin)

        return result


s = Solution()
ans = s.minCoins(93)

print(ans)        
print(len(ans))   