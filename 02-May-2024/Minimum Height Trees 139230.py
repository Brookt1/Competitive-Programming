# Problem: Minimum Height Trees - https://leetcode.com/problems/minimum-height-trees/

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n < 2:
            return [0]

        indegree = [0] * n
        graph = [[] for i in range(n)]

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            indegree[a] += 1
            indegree[b] += 1
        queue = deque()
        count = 0
        for i in range(n):
            if indegree[i] == 1:
                queue.append(i)
                count += 1
        while queue and count < n:
            for _ in range(len(queue)):
                node = queue.popleft()
                for adj in graph[node]:
                    indegree[adj] -= 1
                    if indegree[adj] == 1:
                        queue.append(adj)
                        count += 1
        return queue

        
