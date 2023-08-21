# sliding windows problem

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res=0
        ave=0.0
        for i in range(k):
            ave+=nums[i]
        res=float(ave)

        h=k
        l=0
        while h<len(nums):
            ave+=(-nums[l]+nums[h])
            res=max(res,ave)
            l+=1
            h+=1
        return res/k
