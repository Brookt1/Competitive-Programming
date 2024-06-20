# Problem: Maximal Square - https://leetcode.com/problems/maximal-square/

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        grid = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                grid[i + 1][j + 1] = int(matrix[i][j])

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if grid[i][j]:
                    grid[i][j] = min(grid[i - 1][j - 1] , grid[i - 1][j], grid[i][j - 1]) + 1
        ans = 0
        for row in grid:
            ans = max(ans, max(row))
        return ans * ans
