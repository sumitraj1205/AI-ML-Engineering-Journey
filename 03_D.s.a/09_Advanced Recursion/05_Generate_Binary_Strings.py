# Problem: Generate all binary strings of length N.
# Approach: Recursively add 0 and 1 at each position.
# Time Complexity: O(2^n * n)
# Space Complexity: O(n) auxiliary space.

def generate_binary(index, n, current):
    if index == n:
        print("".join(current))
        return

    current.append("0")
    generate_binary(index + 1, n, current)
    current.pop()

    current.append("1")
    generate_binary(index + 1, n, current)
    current.pop()


n = 3
generate_binary(0, n, [])