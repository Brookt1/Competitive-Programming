# Problem: Min Cost to Connect All Points - https://leetcode.com/problems/min-cost-to-connect-all-points/

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        

        n = len(points)
        edges = []
        root = [i for i in range(n)]
        rank = [0]*n  
        for i in range(n):
            for j in range(i + 1, n):
                dis = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append([dis, i, j])
        edges.sort()
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
        ans = 0
        for cost, a, b in edges:
            if find(a) != find(b):
                ans += cost
                union(a, b)
        return ans

