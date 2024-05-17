# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        r, c= len(matrix), len(matrix[0])
        grid = [[float('inf')] + [0]*c + [float('inf')] for i in range(r)]
        grid.insert(0, [float('inf')] * (c + 1))
        for i in range(1, r + 1):
            for j in range(1, c + 1):
                if i == 1:
                    grid[i][j] = matrix[i - 1][j - 1]
                else:
                    grid[i][j] = matrix[i - 1][j - 1] + min(grid[i - 1][j], grid[i - 1][j - 1], grid[i - 1][j + 1])
        return min(grid[r])