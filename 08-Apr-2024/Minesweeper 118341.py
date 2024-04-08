# Problem: Minesweeper - https://leetcode.com/problems/minesweeper/

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        row, col = click
        if board[row][col] == 'M':
            board[row][col] = 'X'
            return board
        m, n = len(board), len(board[0])
        dir = [[0,1], [0, -1], [-1, 0], [1, 0], [-1, -1], [-1, 1], [1, -1], [1, 1]]
        def inbound(row, col):
            return (0<= row < m) and (0 <= col < n)
        def count_mine(row, col):
            count = 0
            for x, y in dir:
                new_row = row + x
                new_col = col + y
                if inbound(new_row, new_col) and board[new_row][new_col] == 'M':
                    count += 1
            return count
        def dfs(row, col):
            if board[row][col] == 'E':
                mines = count_mine(row, col)
                if mines:
                    board[row][col] = str(mines)
                else:
                    board[row][col] = 'B'
                    for x, y in dir:
                        new_row = row + x
                        new_col = col + y
                        if inbound(new_row, new_col):
                            dfs(new_row, new_col)
        dfs(row, col)
        return board




