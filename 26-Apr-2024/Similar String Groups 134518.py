# Problem: Similar String Groups - https://leetcode.com/problems/similar-string-groups/

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        
        n = len(strs)
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
                    root[rootA] =  rootB
                else:
                    root[rootB] = rootA
                    rank[rootA] += 1
        for i in range(n):
            for j in range(i + 1, n):
                diff = []
                for k in range(len(strs[i])):
                    if len(diff) > 2:
                        break
                    if strs[i][k] != strs[j][k]:
                        diff.append(k)
                if len(diff) == 0 or len(diff) ==  2 and strs[i][diff[0]] == strs[j][diff[1]] and strs[i][diff[1]] == strs[j][diff[0]]:
                    union(i, j)
        for i in range(n):
            root[i] = find(i)
        return len(set(root))

