# Problem: Parallel Courses III - https://leetcode.com/problems/parallel-courses-iii/

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:


        indegree = [0] * n
        graph = [[] for i in range(n)]
        min_time = [0]*n

        for a, b in relations:
            graph[a - 1].append(b - 1)
            indegree[b - 1] += 1
        queue = deque()
        for i in range(n):
            if indegree[i] == 0:
                min_time[i] = time[i]
                queue.append(i)
        
        while queue:
            node = queue.popleft()
            for adj in graph[node]:
                min_time[adj] = max(min_time[adj], min_time[node])
                indegree[adj] -= 1
                if indegree[adj] == 0:
                    min_time[adj] += time[adj]
                    queue.append(adj)
           
        return max(min_time)

