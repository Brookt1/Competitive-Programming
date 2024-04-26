# Problem: Most Stones Removed with Same Row or Column - https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        

        arr = []
        n = len(stones)
        for i in range(n):
            stones[i].append(i)
            arr.append(stones[i])
        
        root = [i for i in range(n)]
        size = [1]*n

        def find(x):
            while x != root[x]:
                root[x] = root[root[x]]
                x = root[x]
            return x
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if size[rootX] > size[rootY]:
                    root[rootY] = rootX
                    size[rootX] += size[rootY]
                else:
                    root[rootX] = rootY
                    size[rootY] += size[rootX]
        stones.sort()
        arr.sort(key = lambda x : x[1])
        for i in range(1, n):
            if stones[i][0] == stones[i - 1][0]:
                union(stones[i][2], stones[i - 1][2])
            if arr[i][1] == arr[i - 1][1]:
                union(arr[i][2], arr[i - 1][2])
        count = 0
        for i in range(n):
            count += size[find(root[i])] - 1
            size[find(root[i])] =  1
        return count

        