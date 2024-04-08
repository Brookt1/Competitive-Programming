# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque()
        visited = set()
        fresh = 0
        count = -1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append([i, j])
                    visited.add((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
        
        dir = [ [1, 0], [-1, 0], [0, -1], [0, 1]]
        print(fresh)
        def inbound(row, col):
            return (0<= row < m ) and (0 <= col < n)
        while queue:
            _len = len(queue)
            count += 1
            for _ in range(_len):
                row, col = queue.popleft()
                for i, j in dir:
                    new_row = row + i
                    new_col = col + j

                    if inbound(new_row, new_col) and (new_row, new_col) not in visited and grid[new_row][new_col] == 1:
                        fresh -=1
                        queue.append([new_row, new_col])
                        visited.add((new_row, new_col))
        if fresh == 0:
            return count
        return -1


        