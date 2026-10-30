# Problem: Swap two numbers without using a third variable.
# Approach: Use the XOR operator.
# Time Complexity: O(1)
# Space Complexity: O(1)

def swap_numbers(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b

    return a, b


a = 10
b = 20

a, b = swap_numbers(a, b)

print("a =", a)
print("b =", b)