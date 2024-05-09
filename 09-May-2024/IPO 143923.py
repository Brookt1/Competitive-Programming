# Problem: IPO - https://leetcode.com/problems/ipo/

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(capital)
        for i in range(n):
            capital[i] = [capital[i], profits[i]]
        capital.sort()
        heap = []
        idx = 0
        while k > 0:
            while idx < n and capital[idx][0] <= w:
                heappush(heap, -1 * capital[idx][1])
                idx += 1
            if heap:
                p = heappop(heap)
                w += abs(p)
            k -= 1
        return w              