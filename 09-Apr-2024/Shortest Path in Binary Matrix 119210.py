# Problem: Shortest Path in Binary Matrix - https://leetcode.com/problems/shortest-path-in-binary-matrix/description/

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        m, n = len(grid), len(grid[0])
        dir = [[1, 0], [-1, 0], [0, - 1], [0,  1], [-1, -1], [-1, 1], [1, -1], [1, 1]]
        inbound = lambda row, col: (0 <= row < m ) and (0 <= col < n)
        queue = deque([[0, 0, 1]])
        grid[0][0] = -1
        ans = n*m + 1
        while queue:
            for _ in range(len(queue)):
                row, col, depth = queue.popleft()
                for x, y in dir:
                    if row == m - 1 and col == n -1:
                            ans = min(ans, depth)
                            continue
                    new_row, new_col = x + row, y + col
                    if inbound(new_row, new_col) and grid[new_row][new_col] == 0:
                        grid[new_row][new_col] = -1
                        queue.append([new_row, new_col, depth + 1])
        if ans > m*n:
            return -1
        return ans


