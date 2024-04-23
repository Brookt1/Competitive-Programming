# Problem: Find if Path Exists in Graph - https://leetcode.com/problems/find-if-path-exists-in-graph/

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        

        root = [i for i in range(n)]
        size = [1 for _ in range(n)]

        def find(x):
            if x == root[x]:
                return x
            root[x] = find(root[x])
            return root[x]
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if size[rootX] > size[rootY]:
                    size[rootX] += size[rootY]
                    root[rootY] = rootX
                else:
                    root[rootX] = rootY
                    size[rootY] += size[rootX]
        for x, y in edges:
            union(x, y)
        return find(source) == find(destination)