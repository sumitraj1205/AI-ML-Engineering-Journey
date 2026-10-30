# Problem: Check whether the i-th bit is set or not.
# Approach: Use left shift and bitwise AND.
# Time Complexity: O(1)
# Space Complexity: O(1)

def check_ith_bit(n, i):
    if n & (1 << i):
        return True
    return False


n = 13
i = 2

print(check_ith_bit(n, i))