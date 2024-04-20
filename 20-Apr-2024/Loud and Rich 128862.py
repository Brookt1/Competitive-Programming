# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        
        n = len(quiet)
        graph = defaultdict(list)
        incoming = [0]*n
        for rich, poor in richer:
            graph[rich].append(poor)
            incoming[poor] += 1
        ans = [float('inf')]*n
        queue = deque()
        for i in range(n):
            if incoming[i] == 0:
                queue.append(i)
                ans[i] = i
        while queue:
            node = queue.popleft()
            if quiet[node] < quiet[ans[node]]:
                ans[node] = node
            for adj in graph[node]:
                if ans[adj] >= n or quiet[ans[node]] < quiet[ans[adj]]:
                    ans[adj] = ans[node]
                incoming[adj] -= 1
                if incoming[adj] == 0:
                    queue.append(adj)
        return ans