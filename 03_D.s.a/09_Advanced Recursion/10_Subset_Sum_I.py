# Problem: Find the sum of every possible subset.
# Approach: Use take and not-take recursion.
# Time Complexity: O(2^n)
# Space Complexity: O(2^n) for storing all subset sums.

def subset_sums(index, arr, total, ans):
    if index == len(arr):
        ans.append(total)
        return

    # Take the current element
    subset_sums(index + 1, arr, total + arr[index], ans)

    # Do not take the current element
    subset_sums(index + 1, arr, total, ans)


arr = [3, 1, 2]
ans = []

subset_sums(0, arr, 0, ans)
ans.sort()

print(ans)