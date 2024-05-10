# Problem: Maximum Performance of a Team - https://leetcode.com/problems/maximum-performance-of-a-team/

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        
        arr = []
        for i in range(n):
            arr.append([efficiency[i], speed[i]])

        arr.sort(reverse = True)
        heap = []
        ans = 0
        _sum = 0
        for i in range(n):
            _sum += arr[i][1]
            if len(heap) < k:
                heappush(heap, [arr[i][1], arr[i][0]])
            else:
                _sum -= heappop(heap)[0]
                heappush(heap, [arr[i][1], arr[i][0]])
            ans = max(ans, _sum * arr[i][0])
        return ans % (int(1e9) + 7)