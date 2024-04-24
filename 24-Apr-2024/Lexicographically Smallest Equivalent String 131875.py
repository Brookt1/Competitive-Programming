# Problem: Lexicographically Smallest Equivalent String - https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        root = {chr(ord('a') + i):chr(ord('a') + i) for i in range(26)}
        def find(s):
            return root[s]
        
        def union(a, b):
            rootA = find(a)
            rootB = find(b)
            if rootA != rootB:
                if rootA < rootB:
                    for node in root:
                        if root[node] == rootB:
                            root[node] = rootA
                else:
                    for node in root:
                        if root[node] == rootA:
                            root[node] = rootB
        ans = []
        for i in range(len(s1)):
            union(s1[i], s2[i])

        for ch in baseStr:
            ans.append(root[ch])
        return ''.join(ans)
