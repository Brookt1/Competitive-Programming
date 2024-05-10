# Problem: Strange Printer II - https://leetcode.com/problems/strange-printer-ii/

class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        
        dic = {}
        m = len(targetGrid)
        n = len(targetGrid[0])
        for i in range(m):
            for j in range(n):
                key = targetGrid[i][j]
                if key not in dic:
                    dic[key] = [i, j, i, j]
                else:
                   dic[key] = [min(i, dic[key][0]), min(j, dic[key][1]), max(i, dic[key][2]), max(j, dic[key][3])]
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for key, val in dic.items():
            min_i, min_j, max_i, max_j = val
            for i in range(min_i, max_i + 1):
                for j in range(min_j, max_j + 1):
                    color = targetGrid[i][j]
                    if color != key:
                        graph[key].append(color)
                        indegree[color] += 1
        
        queue = deque()
        colors = list(dic.keys())
        for color in colors:
            if indegree[color] == 0:
                queue.append(color)
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                for adj in graph[node]:
                    indegree[adj] -= 1
                    if indegree[adj] == 0:
                        queue.append(adj)
        if max(indegree.values()) == 0:
            return True
        return False