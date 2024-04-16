# Problem: Remove Stones to Minimize the Total - https://leetcode.com/problems/remove-stones-to-minimize-the-total/

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        for i in range(len(piles)):
            piles[i] *= -1

        heapify(piles)
        for i in range(k):
            num = (-1*heappop(piles) + 1)//2
            heappush(piles, -1*num)
        return sum(abs(num) for num in piles)

