# Problem: Understand the common patterns of subsequence recursion.
# Approach: Use take and not-take recursion.
# Time Complexity: O(n * 2^n) for printing,
#                   O(2^n) for checking and counting.
# Space Complexity: O(n) auxiliary recursion space.

# Pattern 1: Print all subsequences
def print_all(index, arr, current):
    if index == len(arr):
        print(current)
        return

    current.append(arr[index])
    print_all(index + 1, arr, current)

    current.pop()
    print_all(index + 1, arr, current)


# Pattern 2: Check if a subsequence with sum K exists
def check_sum(index, arr, total, k):
    if index == len(arr):
        return total == k

    take = check_sum(index + 1, arr, total + arr[index], k)
    if take:
        return True

    return check_sum(index + 1, arr, total, k)


# Pattern 3: Count subsequences with sum K
def count_sum(index, arr, total, k):
    if index == len(arr):
        return 1 if total == k else 0

    take = count_sum(index + 1, arr, total + arr[index], k)
    not_take = count_sum(index + 1, arr, total, k)

    return take + not_take


arr = [1, 2, 1]
k = 2

print("All subsequences:")
print_all(0, arr, [])

print("Exists:", check_sum(0, arr, 0, k))
print("Count:", count_sum(0, arr, 0, k))