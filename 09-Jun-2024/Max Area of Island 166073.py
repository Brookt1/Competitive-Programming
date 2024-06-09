# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        inbound = lambda row, col: (0 <= row < m) and (0 <= col < n )

        def dfs(row, col):

            grid[row][col] = 0
            count = 0
            for x, y in dir:
                new_row, new_col = row + x, col + y
                if inbound(new_row, new_col) and grid[new_row][new_col] == 1:
                    count += dfs(new_row, new_col)
            return count + 1
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ans = max(ans, dfs(i, j))
        return ans