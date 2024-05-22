# Problem: Pacific Atlantic Water Flow - https://leetcode.com/problems/pacific-atlantic-water-flow

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
  
        row, col = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visited, prev):
            if not ((0 <= r < row) and (0 <= c < col)):
                return 
            
            if (r, c) in visited or heights[r][c] < prev:
                return 
            
            visited.add((r, c))
            
            directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs(nr, nc, visited, heights[r][c])

        for r in range(row):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, col-1, atl, heights[r][col-1])
        
        for c in range(col):
            dfs(0, c, pac, heights[0][c])
            dfs(row-1, c, atl, heights[row-1][c])
        
        return list(pac & atl)
