# Problem: Generate all possible letter combinations for a phone number.
# Approach: Use backtracking with a digit-to-letter mapping.
# Time Complexity: O(4^n * n)
# Space Complexity: O(n) auxiliary space, excluding output.

def letter_combinations(digits):
    if not digits:
        return []

    mapping = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    ans = []

    def solve(index, current):
        if index == len(digits):
            ans.append(current)
            return

        letters = mapping[digits[index]]

        for ch in letters:
            solve(index + 1, current + ch)

    solve(0, "")
    return ans


digits = "23"
print(letter_combinations(digits))