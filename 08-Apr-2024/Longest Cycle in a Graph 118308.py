# Problem: Longest Cycle in a Graph - https://leetcode.com/problems/longest-cycle-in-a-graph/

class Solution:
    def longestCycle(self, edges: List[int]) -> int:

        ans = -1
        def cycle_count(node):
            nonlocal ans

            n = edges[node]
            count = 1
            while n != node:
                n = edges[n]
                count += 1
            ans = max(ans, count)

        n = len(edges)
        colors = [0]*n

        def dfs(node):
                n = edges[node]
                if n == -1:
                    return

                colors[node] = 1
                if colors[n] == 1:
                    cycle_count(n)
                elif not colors[n]:
                    dfs(n)
                colors[node] = 2
        for i in range(n):
            if not colors[i]:
                dfs(i)
        return ans
            



            