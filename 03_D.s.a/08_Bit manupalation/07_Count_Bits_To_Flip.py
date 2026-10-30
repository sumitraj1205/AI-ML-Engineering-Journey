# Problem: Find the number of bits that need to be flipped
#          to convert A into B.
# Approach: XOR A and B, then count the set bits.
# Time Complexity: O(k), where k is the number of set bits.
# Space Complexity: O(1)

def count_bits_to_flip(a, b):
    n = a ^ b
    count = 0

    while n > 0:
        n = n & (n - 1)
        count += 1

    return count


a = 10
b = 20

print(count_bits_to_flip(a, b))