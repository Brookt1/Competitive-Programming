# Problem: Surrounded Regions - https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        inbound = lambda row, col: (0 <= row < m) and ( 0 <= col < n)
        dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        queue = deque()
        visited = set()
        for i in range(m):
            for j in range(n):
                if (i in (0, m - 1) or j in (0, n - 1)) and board[i][j] == 'O':
                    visited.add((i, j))
                    queue.append([i, j])
        while queue:
            for _ in range(len(queue)):
                row, col = queue.pop()
                for x, y in dir:
                    new_row, new_col = x + row, y + col
                    if inbound(new_row, new_col) and (new_row, new_col) not in visited and board[new_row][new_col] == 'O':
                        visited.add((new_row, new_col))
                        queue.append([new_row, new_col])
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and (i, j) not in visited:
                    board[i][j] = 'X'
        
