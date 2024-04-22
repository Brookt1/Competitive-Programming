# Problem: Longest Increasing Path in a Matrix - https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        inbound = lambda row, col : (0 <= row < m) and (0 <= col < n)
        dir = [[1, 0], [-1, 0], [0, -1], [0,  1]]
        memo = [[-1]*n for _ in range(m)]
        def dfs(i, j):
            if memo[i][j] != -1:
                return memo[i][j]
            count = 0
            for x, y in dir:
                new_row, new_col = x + i, y + j
                if inbound(new_row, new_col) and matrix[new_row][new_col] < matrix[i][j]:
                    count = max(count, dfs(new_row, new_col))
            memo[i][j] = count + 1
            return count + 1
        ans = 1
        for i in range(m):
            for j in range(n):
                count = 0
                for x, y in dir:
                    new_row, new_col = x + i, y + j
                    if inbound(new_row, new_col) and matrix[new_row][new_col] < matrix[i][j]:
                        count += 1
                if count:
                    ans = max(ans, dfs(i, j))
        return ans