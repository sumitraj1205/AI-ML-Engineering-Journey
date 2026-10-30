# Problem: Find unique combinations whose sum equals the target.
# Approach: Sorting and backtracking with duplicate skipping.
# Time Complexity: O(2^n * n) including copying combinations.
# Space Complexity: O(n) auxiliary space, excluding output.

def combination_sum_2(arr, target):
    arr.sort()
    ans = []

    def solve(index, current, total):
        if total == target:
            ans.append(current.copy())
            return

        for i in range(index, len(arr)):
            if i > index and arr[i] == arr[i - 1]:
                continue

            if total + arr[i] > target:
                break

            current.append(arr[i])
            solve(i + 1, current, total + arr[i])
            current.pop()

    solve(0, [], 0)
    return ans


arr = [10, 1, 2, 7, 6, 1, 5]
target = 8

print(combination_sum_2(arr, target))