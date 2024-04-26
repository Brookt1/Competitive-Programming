# Problem: Minimum Score of a Path Between Two Cities - https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        

        dis = [float('inf')]*n
        root = [i for i in range(n)]
        rank = [0]*n

        roads.sort(key = lambda x: x[2])
        def find(x):
            while x != root[x]:
                root[x] = root[root[x]]
                x = root[x]
            return x
        def union(a, b, x):
            rootA = find(a)
            rootB = find(b)
            if rootA != rootB:
                if rank[rootA] > rank[rootB]:
                    root[rootB] = rootA
                    dis[rootA] = min(dis[rootA], dis[rootB], x)
                elif rank[rootA] < rank[rootB]:
                    dis[rootB] = min(dis[rootA], dis[rootB], x)
                    root[rootA] = rootB
                else:
                    dis[rootA] = min(dis[rootA], dis[rootB], x)
                    root[rootB] = rootA
                    rank[rootA] += 1
        for a, b, x in roads:
            union(a - 1, b - 1, x)
        return dis[find(0)]
        

