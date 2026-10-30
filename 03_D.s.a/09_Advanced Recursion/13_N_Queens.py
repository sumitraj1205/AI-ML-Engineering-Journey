# Problem: Place N queens on an N x N chessboard so that
#          no two queens attack each other.
# Approach: Use backtracking and check columns and diagonals.
# Time Complexity: O(N!)
# Space Complexity: O(N^2) for the board.

def solve_n_queens(n):
    ans = []
    board = [["."] * n for _ in range(n)]

    cols = set()
    diagonal1 = set()  # row - col
    diagonal2 = set()  # row + col

    def solve(row):
        if row == n:
            ans.append(["".join(r) for r in board])
            return

        for col in range(n):
            if (col in cols or
                row - col in diagonal1 or
                row + col in diagonal2):
                continue

            board[row][col] = "Q"
            cols.add(col)
            diagonal1.add(row - col)
            diagonal2.add(row + col)

            solve(row + 1)

            # Backtracking
            board[row][col] = "."
            cols.remove(col)
            diagonal1.remove(row - col)
            diagonal2.remove(row + col)

    solve(0)
    return ans


n = 4
result = solve_n_queens(n)

for solution in result:
    for row in solution:
        print(row)
    print()