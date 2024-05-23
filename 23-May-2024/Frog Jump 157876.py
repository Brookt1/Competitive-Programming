# Problem: Frog Jump - https://leetcode.com/problems/frog-jump/

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        


        dic = {}
        n = len(stones)
        for stone in stones:
            dic[stone] = set()
        dic[stones[0]].add(0)
        for stone in stones:
            for jump in dic[stone]:
                for i in range(1, -2, -1):
                    val = stone + (jump + i)
                    if val in dic and val > stone :
                        dic[val].add(jump + i)

        if dic[stones[-1]]:
            return True
        return False