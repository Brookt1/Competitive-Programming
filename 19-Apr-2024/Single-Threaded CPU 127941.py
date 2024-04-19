# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i in range(len(tasks)):
            tasks[i] = tasks[i] + [i]
        tasks.sort()

        ans = []
        t = tasks[0][0]
        heap = [[tasks[0][1],tasks[0][2]]]
        print(heap)
        idx = 0
        while heap:
            d, i = heappop(heap)
            t += d
            while idx + 1 < len(tasks) and tasks[idx + 1][0] <= t:
                heappush(heap, [tasks[idx + 1][1], tasks[idx + 1][2]])
                idx += 1
            if not heap and idx + 1 < len(tasks):
                heappush(heap, [tasks[idx + 1][1], tasks[idx + 1][2]])
                t = tasks[idx + 1][0]
                idx += 1
            ans.append(i)
        return ans




