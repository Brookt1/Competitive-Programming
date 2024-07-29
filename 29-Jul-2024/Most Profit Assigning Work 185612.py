# Problem: Most Profit Assigning Work - https://leetcode.com/problems/most-profit-assigning-work/

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        n = len(profit)
        arr = list(zip(difficulty, profit))
        arr.sort()
        worker.sort()
        _max  = ans = ptr = 0
        for i in range(len(worker)):

            while ptr < n and worker[i] >= arr[ptr][0]:
                _max = max(_max, arr[ptr][1])
                ptr += 1
            ans += _max
        return ans