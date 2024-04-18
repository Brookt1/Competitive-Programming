# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        ans = [set() for _ in range(n)]
        graph = [[] for _ in range(n)]
        incoming = [0]*n
        for _from, to in edges:
            graph[_from].append(to)
            incoming[to] += 1
        queue = deque()
        for i in range(n):
            if incoming[i] == 0:
                queue.append(i)
        while queue:
            node = queue.popleft()
            for adj in graph[node]:
                incoming[adj] -= 1
                if incoming[adj] == 0:
                    queue.append(adj)
                for child in ans[node]:
                    if child not in ans[adj]:
                        ans[adj].add(child)
                ans[adj].add(node)
        for i in range(len(ans)):
            ans[i] = sorted(list(ans[i]))
        return ans

        


