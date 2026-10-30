# Problem: Find K numbers from 1 to 9 whose sum equals N.
# Approach: Backtracking without repeating numbers.
# Time Complexity: O(C(9, k) * k)
# Space Complexity: O(k) auxiliary space, excluding output.

def combination_sum_3(k, n):
    ans = []

    def solve(start, current, total):
        if len(current) == k:
            if total == n:
                ans.append(current.copy())
            return

        for i in range(start, 10):
            if total + i > n:
                break

            current.append(i)
            solve(i + 1, current, total + i)
            current.pop()

    solve(1, [], 0)
    return ans


k = 3
n = 7

print(combination_sum_3(k, n))