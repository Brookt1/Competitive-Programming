# Problem: Minimum Height Trees - https://leetcode.com/problems/minimum-height-trees/

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        

        graph = [[] for _ in range(n)]
        degree = [0 for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            degree[a] += 1
            degree[b] += 1
        queue = deque()
        for i in range(n):
            if degree[i] < 2:
                queue.append(i)
        
        last = []
        while queue:
            last = []
            for _ in range(len(queue)):
                node = queue.popleft()
                last.append(node)
                for neig in graph[node]:
                    degree[neig] -= 1
                    if degree[neig] == 1:
                        queue.append(neig)
        return last

