# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        m, n = len(mat), len(mat[0])
        inbound = lambda row, col: (0 <= row < m) and (0 <= col < n)
        dir = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        ans = [[0]*n for _ in range(m)]
        queue = deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append([i, j])
                    mat[i][j] = -1
        level = 0
        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                ans[row][col] = level
                for x, y in dir:
                    new_row, new_col =x + row, y + col
                    if inbound(new_row, new_col) and mat[new_row][new_col] != -1:
                        mat[new_row][new_col] = -1
                        queue.append([new_row, new_col])
            level += 1
        return ans

