# Problem: All Paths From Source to Target - https://leetcode.com/problems/all-paths-from-source-to-target/

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        ans = []
        def dfs(node, path):
            if node == len(graph) - 1:
                ans.append(path.copy())
            
            for adj in graph[node]:
                dfs(adj, path + [adj])
        dfs(0, [0])
        return ans