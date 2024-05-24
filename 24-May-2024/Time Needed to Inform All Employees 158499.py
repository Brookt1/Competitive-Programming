# Problem: Time Needed to Inform All Employees - https://leetcode.com/problems/time-needed-to-inform-all-employees/

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        graph = [[] for _ in range(n)]
        for i in range(n):
            if manager[i] != -1:
                graph[manager[i]].append(i)
        
        def dfs(node): 
            val = 0
            for employ in graph[node]:
                val = max(val, dfs(employ))
            return informTime[node] + val
        return dfs(headID)

