class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sumP={0:1}
        sum=0
        res=0
        for i in range(len(nums)):
            sum+=nums[i]
            if sum-k in sumP: 
                res+=sumP[sum-k]
            sumP[sum]=1+sumP.get(sum,0)
        return res
