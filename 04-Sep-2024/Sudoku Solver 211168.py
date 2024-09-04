# Problem: Sudoku Solver - https://leetcode.com/problems/sudoku-solver/description/

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        row_dic = defaultdict(set)
        col_dic = defaultdict(set)
        square_dic = defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col] != '.':
                    temp = int(board[row][col])
                    row_dic[row].add(temp)
                    col_dic[col].add(temp)
                    square_dic[(row // 3) * 3 + col//3].add(temp)
     
        flag = [False]
        def bt(row, col):
            if flag[0] or row == 9:
                return
            
            if board[row][col] == '.':
                for num in range(1, 10):
                    if num not in col_dic[col] and num not in row_dic[row] and num not in  square_dic[(row // 3) * 3 +  col // 3]:
                            
                        row_dic[row].add(num)
                        col_dic[col].add(num)
                        square_dic[(row // 3) * 3 + col//3].add(num)
                        board[row][col] = str(num)

                        if row == 8 and col == 8:
                            flag[0]  = True
                            return

                        if col == 8:
                            bt(row + 1, 0)
                        else:
                            bt(row, col + 1)
                        if not flag[0]:    
                            row_dic[row].remove(num)
                            col_dic[col].remove(num)
                            square_dic[(row // 3) * 3 + col//3].remove(num)
                            board[row][col] = '.'

            else:                  
                if row == 8 and col == 8:
                    flag[0]  = True
                    return
                if col == 8:
                    bt(row + 1, 0)
                else:
                    bt(row, col + 1)
        bt(0, 0)



