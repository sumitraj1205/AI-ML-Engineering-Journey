# Problem: Find the number that appears an odd number of times.
# Approach: Use XOR to cancel out numbers appearing even times.
# Time Complexity: O(n)
# Space Complexity: O(1)

def find_odd_occurring(arr):
    ans = 0

    for num in arr:
        ans = ans ^ num

    return ans


arr = [1, 2, 3, 2, 3, 1, 3]

print(find_odd_occurring(arr))