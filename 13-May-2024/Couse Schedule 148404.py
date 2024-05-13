# Problem: Couse Schedule - https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        

        graph = defaultdict(list)
        indegree = defaultdict(int)
        for a, b in prerequisites:
            graph[a].append(b)
            indegree[b] += 1
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        count = 0
        while queue:
            node = queue.popleft()
            count += 1
            for adj in graph[node]:
                indegree[adj] -= 1
                if indegree[adj] == 0:
                    queue.append(adj)
        return count == numCourses
