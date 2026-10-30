# Problem: Find all possible paths for a rat to reach the destination.
# Approach: Use backtracking to explore all four directions.
# Time Complexity: O(4^(n*n)) upper bound.
# Space Complexity: O(n*n) auxiliary space, excluding output.

def find_paths(maze):
    n = len(maze)

    if n == 0 or maze[0][0] == 0 or maze[n - 1][n - 1] == 0:
        return []

    ans = []
    visited = [[False] * n for _ in range(n)]

    directions = [
        (1, 0, "D"),
        (0, -1, "L"),
        (0, 1, "R"),
        (-1, 0, "U")
    ]

    def solve(row, col, path):
        if row == n - 1 and col == n - 1:
            ans.append(path)
            return

        visited[row][col] = True

        for dr, dc, move in directions:
            nr = row + dr
            nc = col + dc

            if (0 <= nr < n and 0 <= nc < n
                    and maze[nr][nc] == 1
                    and not visited[nr][nc]):

                solve(nr, nc, path + move)

        visited[row][col] = False

    solve(0, 0, "")
    return ans


maze = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [1, 1, 0, 0],
    [0, 1, 1, 1]
]

print(find_paths(maze))