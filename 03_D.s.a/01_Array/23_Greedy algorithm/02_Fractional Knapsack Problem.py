# Problem: Fractional Knapsack
# Approach: Greedy + Sorting by value/weight ratio
# Time Complexity: O(n log n)
# Space Complexity: O(n) for sorting

class Solution:
    def fractionalKnapsack(self, val, wt, capacity):
        items = []

        for i in range(len(val)):
            ratio = val[i] / wt[i]
            items.append((ratio, val[i], wt[i]))

        # Sort by value/weight ratio in descending order
        items.sort(reverse=True)

        total_value = 0

        for ratio, value, weight in items:

            if capacity == 0:
                break

            if weight <= capacity:
                total_value += value
                capacity -= weight

            else:
                total_value += ratio * capacity
                capacity = 0

        return total_value


s = Solution()
print(s.fractionalKnapsack(
    [60, 100, 120],
    [10, 20, 30],
    50
))
