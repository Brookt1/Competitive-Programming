# Problem: Snakes and Ladders - https://leetcode.com/problems/snakes-and-ladders/

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        
        n = len(board)
        board.reverse()
        def cellToRC(cell):
            row = (cell - 1)//n
            col = (cell - 1) % n
            if row % 2:
                col = n - 1 - col
            return [row, col]
        
        queue = deque([[1, 0]])
        board[0][0] = 0
        while queue:
            cell, level = queue.popleft()
            if cell == n*n:
                return level
            for i in range(1, 7):
                row, col = cellToRC(cell + i)
                if( cell + i) <= n*n and board[row][col]:
                    val = board[row][col] 
                    if val == -1:
                        queue.append([cell + i, level + 1])
                    elif val:
                        queue.append([val, level + 1])
                    board[row][col] = 0
        return -1

                
            
