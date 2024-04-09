# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:

        queue = deque()
        visited = set()
        red_edges = defaultdict(list)
        blue_edges = defaultdict(list)

        for a,b in redEdges:
            red_edges[a].append(b)
        for a, b in blueEdges:
            blue_edges[a].append(b)
        if 0 in red_edges:
            queue.append([0, 1, 0])
            visited.add((0, 1))
        if 0 in blue_edges:
            queue.append([0, 2, 0])
            visited.add((0, 2))
        ans = [-1]*n
        ans[0] = 0
        while queue:
            for _ in range(len(queue)):
                node, color, depth = queue.popleft()
                if ans[node] == -1:
                    ans[node] = depth
                if color == 1:
                    for adj in red_edges[node]:
                        val = (adj, 1)
                        if val not in visited:
                            queue.append([adj, 2, depth + 1])
                            visited.add(val)
                else:
                    for adj in blue_edges[node]:
                        val = (adj, 2)
                        if val not in visited:
                            queue.append([adj, 1, depth + 1])
                            visited.add(val)
        return ans