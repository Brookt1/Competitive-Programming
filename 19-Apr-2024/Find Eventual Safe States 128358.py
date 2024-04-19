# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        n = len(graph)
        colors = [0 for _ in range(n)]
        safe = [ ]
        def topSort(node):
            if colors[node] == 1:
                return False
            
            colors[node] = 1
            for adj in graph[node]:
                if colors[adj] == 2:
                    continue
                if not topSort(adj):
                    return False
                
            safe.append(node)
            colors[node] = 2
            return True
        for i in range(n):
            if colors[i] != 2:
                topSort(i)
        return sorted(safe)
