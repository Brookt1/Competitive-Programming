# Problem: Maximum Number of Fish in a Grid - https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        

        def find(x):
            while x != root[x]:
                root[x] = root[root[x]]
                x = root[x]
            return x
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    root[rootY] = rootX
                elif rank[rootX] < rank[rootY]:
                    root[rootX] = rootY
                else:
                    rank[rootX] += 1
                    root[rootY] = rootX
        m, n = len(grid), len(grid[0])
        inbound = lambda row, col: (0 <= row < m) and (0 <= col < n)
        dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        root = [i for i in range(n*m)]
        rank = [0]*(n*m)
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    for x, y in dir:
                        new_row = i + x
                        new_col = j + y
                        if inbound(new_row, new_col) and grid[new_row][new_col]:
                            union(i * n + j, new_row * n + new_col)
        count = defaultdict(int)
        for i in range(n*m):
            count[find(i)] += grid[i // n ][i % n]
        return max(count.values())