class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        l,r=0,0
        res,ans=0,len(nums)+1
        while r<len(nums):
            res+=nums[r]
            r+=1
            while res>=target:
                ans=min(ans,r-l)
                res-=nums[l]
                l+=1
        return ans if ans<=len(nums) else 0
