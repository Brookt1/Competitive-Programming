# Problem: Last Stone Weight - https://leetcode.com/problems/last-stone-weight/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1
        heapify(stones)
        while len(stones) > 1:
            rock_one = heappop(stones)
            rock_two = heappop(stones)
            diff = abs(rock_one - rock_two)
            if diff != 0:
                heappush(stones, -1*diff)
        if len(stones) == 1:
            return -1*stones[0]
        return 0