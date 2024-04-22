# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:


        graph = defaultdict(list)
        indegree = [0]*numCourses
        requ = [set() for _ in range(numCourses)]

        for pre, course in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1
        queue = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)
        while queue:
            course = queue.popleft()
            for adj in graph[course]:
                requ[adj] = requ[adj] | requ[course] | set([course])
                indegree[adj] -= 1
                if indegree[adj] == 0:
                    queue.append(adj)
        ans = []
        for pre, course in queries:
            if pre in requ[course]:
                ans.append(True)
            else:
                ans.append(False)
        return ans
