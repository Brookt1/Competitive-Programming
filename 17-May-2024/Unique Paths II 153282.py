# Problem: Unique Paths II - https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        grid = [[0]*(n + 1) for _ in range(m + 1)]
        if obstacleGrid[0][0] or obstacleGrid[m - 1][n - 1]:
            return 0

        grid[1][1] = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if i == 1 and j == 1 or obstacleGrid[i - 1][j - 1]:
                    continue
                grid[i][j] = grid[i  - 1][j] + grid[i][j - 1]
        return grid[m][n]