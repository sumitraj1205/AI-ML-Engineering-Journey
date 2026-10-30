# Problem: Generate all valid combinations of N pairs of parentheses.
# Approach: Add '(' if open < n and ')' if close < open.
# Time Complexity: O(Cn * n), where Cn is the nth Catalan number.
# Space Complexity: O(n) auxiliary recursion space.

def generate_parentheses(n):
    ans = []

    def solve(current, open_count, close_count):
        if len(current) == 2 * n:
            ans.append(current)
            return

        if open_count < n:
            solve(current + "(", open_count + 1, close_count)

        if close_count < open_count:
            solve(current + ")", open_count, close_count + 1)

    solve("", 0, 0)
    return ans


n = 3
print(generate_parentheses(n))