class Solution:
    def maxCoins(self, piles: List[int]) -> int:

        piles.sort()
        piles.reverse()
        ans=0
        ptr=1
        while ptr//2+(1)<=len(piles)/3:
            ans+=piles[ptr]
            ptr+=2
        return ans
