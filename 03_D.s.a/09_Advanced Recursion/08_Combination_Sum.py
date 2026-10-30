# Problem: Find all combinations whose sum equals the target.
# Approach: Use recursion and allow the same element multiple times.
# Time Complexity: Exponential, O(2^target) as a rough upper bound
#                   when candidates are positive integers.
# Space Complexity: O(target / min(candidates)) auxiliary space,
#                    excluding the output.

def combination_sum(index, arr, target, current, ans):
    if index == len(arr):
        if target == 0:
            ans.append(current.copy())
        return

    # Take the current element again
    if arr[index] <= target:
        current.append(arr[index])
        combination_sum(
            index, arr, target - arr[index], current, ans
        )
        current.pop()

    # Move to the next element
    combination_sum(index + 1, arr, target, current, ans)


arr = [2, 3, 6, 7]
target = 7
ans = []

combination_sum(0, arr, target, [], ans)
print(ans)