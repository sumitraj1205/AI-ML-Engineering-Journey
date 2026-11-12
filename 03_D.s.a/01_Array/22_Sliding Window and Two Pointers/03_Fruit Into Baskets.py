# Problem: Fruit Into Baskets
# Approach: Sliding Window + Dictionary
# Time Complexity: O(n)
# Space Complexity: O(1) - At most 2 fruit types in valid window

class Solution:
    def totalFruit(self, fruits):
        left = 0
        count = {}
        maxi = 0

        for right in range(len(fruits)):
            count[fruits[right]] = count.get(fruits[right], 0) + 1

            while len(count) > 2:
                count[fruits[left]] -= 1

                if count[fruits[left]] == 0:
                    del count[fruits[left]]

                left += 1

            maxi = max(maxi, right - left + 1)

        return maxi


s = Solution()
print(s.totalFruit([1, 2, 1, 2, 3]))
