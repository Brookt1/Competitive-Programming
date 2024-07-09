# Problem: Last Stone Weight - https://leetcode.com/problems/last-stone-weight/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heap = []
        for stone in stones:
            heappush(heap, -1 * stone)
        while len(heap) > 1:
            stone_one = heappop(heap)
            stone_two = heappop(heap)
            if stone_one != stone_two:
                heappush(heap, stone_one - stone_two)
        if heap:
            return abs(heap[0])
        return 0