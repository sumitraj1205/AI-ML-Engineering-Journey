# Problem: Print all possible subsequences of an array.
# Approach: Use recursion with take and not-take choices.
# Time Complexity: O(n * 2^n)
# Space Complexity: O(n) auxiliary recursion space.

def print_subsequences(index, arr, current):
    if index == len(arr):
        print(current)
        return

    # Take the current element
    current.append(arr[index])
    print_subsequences(index + 1, arr, current)

    # Do not take the current element
    current.pop()
    print_subsequences(index + 1, arr, current)


arr = [1, 2, 3]
print_subsequences(0, arr, [])