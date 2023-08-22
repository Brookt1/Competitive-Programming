class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[0]*n
        for i in range(n):
            for j in range(n):
                if(j!=i and nums[i]>nums[j]):
                    ans[i]+=1
        return ans
