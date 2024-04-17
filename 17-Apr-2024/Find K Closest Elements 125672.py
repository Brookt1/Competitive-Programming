# Problem: Find K Closest Elements - https://leetcode.com/problems/find-k-closest-elements/

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        heap = []
        for num in arr:
            heappush(heap, [abs(x - num), num])
        ans = []
        for _ in range(k):
            ans.append(heappop(heap)[1])
        ans.sort()
        return ans