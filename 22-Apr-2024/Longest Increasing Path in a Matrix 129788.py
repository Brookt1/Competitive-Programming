# Problem: Longest Increasing Path in a Matrix - https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        inbound = lambda row, col : (0 <= row < m) and (0 <= col < n)
        dir = [[1, 0], [-1, 0], [0, -1], [0,  1]]

        outdegree = [[0]*n for _ in range(m)]
        queue = deque()
        for i in range(m):
            for j in range(n):
                for x, y in dir:
                    if inbound(i + x, j + y) and matrix[i + x][j + y] > matrix[i][j]:
                        outdegree[i][j] += 1
                
                if outdegree[i][j] == 0:
                    queue.append([i, j])
        ans = 0
        while queue:
            ans += 1
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for x, y in dir:
                    new_row, new_col = i + x, j + y
                    if inbound(new_row, new_col) and matrix[new_row][new_col] < matrix[i][j]:
                        outdegree[new_row][new_col] -= 1
                        if outdegree[new_row][new_col] == 0:
                            queue.append([new_row, new_col])
        return ans