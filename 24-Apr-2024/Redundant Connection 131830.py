# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        root = [i for i in range(1, n + 1)]
        rank = [0]*n
        def find(x):
            while x != root[x - 1]:
                root[x - 1] = root[root[x - 1] - 1]
                x = root[x - 1]
            return x
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if rank[rootX - 1] > rank[rootY - 1]:
                    root[rootY - 1] = rootX
                elif rank[rootX - 1] < rank[rootY - 1]:
                    root[rootX - 1] = rootY
                else:
                    rank[rootX - 1] += 1
                    root[rootY - 1] = rootX
        for a, b in edges:
            if find(a) == find(b):
                return [a, b]
            union(a, b)