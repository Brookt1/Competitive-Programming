# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        
        indegree = [0]*n
        for a, b in edges:
            indegree[b] += 1
        
        count = 0
        for i in range(n):
            if indegree[i] == 0:
                count += 1
        if count == 1:
            return indegree.index(0)
        return -1