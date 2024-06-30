# Problem: N Queens II - https://leetcode.com/problems/n-queens-ii/

class Solution:
    def totalNQueens(self, n: int) -> int:
        
        board = [['.']*n for _ in range(n)]
        colums = set()
        forward_diag = set()
        backward_diag = set()


        def backtrack(row,count):
            if row == n:
                count +=1
                return count

            for col in range(n):

                if col not in colums and row - col not in backward_diag and row + col not in forward_diag:

                    colums.add(col)
                    forward_diag.add(row + col)
                    backward_diag.add(row - col)

                    count = backtrack(row + 1, count)

                    colums.remove(col)
                    forward_diag.remove(row + col)
                    backward_diag.remove(row - col)
            return count
        
        return backtrack(0, 0)