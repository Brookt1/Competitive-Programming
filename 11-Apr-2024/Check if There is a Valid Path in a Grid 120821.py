# Problem: Check if There is a Valid Path in a Grid - https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        
        m, n = len(grid), len(grid[0])
        inbound = lambda row, col: (0 <= row < m) and (0 <= col < n)
        stack = [[0, 0]]
        dic = {'right':[1, 3, 5], 'left':[1, 4, 6], 'top':[2, 3, 4], 'bottom':[2, 5, 6]}
        while stack:
            row, col = stack.pop()
            if row == m - 1 and col == n - 1:
                return True
            num = grid[row][col]
            print(row, col, num)
            if num in dic['right'] and inbound(row, col -1) and grid[row][col - 1] in dic['left']:
                stack.append([row, col - 1])
            if num in dic['left'] and inbound(row, col + 1) and grid[row][col + 1] in dic['right']:
                stack.append([row, col + 1])
            if num in dic['top'] and inbound(row + 1, col) and grid[row + 1][col] in dic['bottom']:
                stack.append([row + 1, col])
            if num in dic['bottom'] and inbound(row - 1, col) and grid[row - 1][col] in dic['top']:
                stack.append([row - 1, col])
            grid[row][col] = 'V'
        return False

