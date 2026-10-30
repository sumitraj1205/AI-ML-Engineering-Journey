# Problem: Check whether a number is a power of 2.
# Approach: Use n & (n - 1).
# Time Complexity: O(1)
# Space Complexity: O(1)

def is_power_of_two(n):
    if n <= 0:
        return False

    return (n & (n - 1)) == 0


n = 16
print(is_power_of_two(n))