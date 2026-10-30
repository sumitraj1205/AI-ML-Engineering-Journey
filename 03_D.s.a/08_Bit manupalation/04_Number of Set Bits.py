# Problem: Count the number of set bits (1s) in a number.
# Approach: Repeatedly remove the rightmost set bit.
# Time Complexity: O(k), where k is the number of set bits.
# Space Complexity: O(1)

def count_set_bits(n):
    count = 0

    while n > 0:
        n = n & (n - 1)
        count += 1

    return count


n = 13
print(count_set_bits(n))