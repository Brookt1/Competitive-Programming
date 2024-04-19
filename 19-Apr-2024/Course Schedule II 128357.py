# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        colors = [0 for _ in range(numCourses)]
        order = []

        for course, pre in prerequisites:
            graph[pre].append(course)

        def top_sort(node):
            if colors[node] == 1:
                return False
            colors[node] = 1

            for adj in graph[node]:
                if colors[adj] == 2:
                    continue
                if not top_sort(adj):
                    return False
            order.append(node)
            colors[node] = 2
            return True
        
        for course in range(numCourses):
            if colors[course] != 2:
               if not top_sort(course):
                return []
                top_sort(course)
        order.reverse()
        return order


        
