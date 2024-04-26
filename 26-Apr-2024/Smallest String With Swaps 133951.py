# Problem: Smallest String With Swaps - https://leetcode.com/problems/smallest-string-with-swaps/

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        
        n = len(s)
        root = [i for i in range(n)]
        rank = [0]*n

        def find(x):
            while x != root[x]:
                root[x] = root[root[x]]
                x = root[x]
            return x
        def union(a, b):
            rootA = find(a)
            rootB = find(b)
            if rootA != rootB:
                if rank[rootA] > rank[rootB]:
                    root[rootB] = rootA
                elif rank[rootA] < rank[rootB]:
                    root[rootA] = rootB
                else:
                    root[rootB] = rootA
                    rank[rootA]
        for a, b in pairs:
            union(a, b)
        group = defaultdict(list)
        for i in range(n):
            heappush(group[find(root[i])], s[i])
        ans = []
        for val in root:
            ans.append(heappop(group[find(val)]))
        return ''.join(ans)
