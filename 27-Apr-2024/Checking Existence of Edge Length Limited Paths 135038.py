# Problem: Checking Existence of Edge Length Limited Paths - https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        for i in range(len(queries)):
            queries[i].append(i)
        edgeList.sort(key = lambda x: x[2])
        queries.sort(key = lambda x: x[2])

        root = [i for i in range(n)]
        rank = [0]*n
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
        ans = [False]*len(queries)
        first = second = 0
        while first < len(queries) and second < len(edgeList):

            while first < len(queries) and edgeList[second][2] >= queries[first][2]:
                if find(queries[first][0]) == find(queries[first][1]) and edgeList[second - 1][-1] < queries[first][2]:
                    ans[queries[first][3]] = True
                else:
                    ans[queries[first][3]]
                first += 1    
            union(edgeList[second][0], edgeList[second][1])
            second += 1
        for i in range(first, len(queries)):
            if edgeList[-1][-1] < queries[i][2]:
                ans[queries[i][-1]] = True
        return ans
        