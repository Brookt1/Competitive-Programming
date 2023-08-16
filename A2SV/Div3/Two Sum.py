class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     sum=nums[i]
        #     for j in range(i+1,len(nums)):
        #         sum+=nums[j]
        #         if sum==target:
        #             return [i,j]

        # let's try hashmap solution

        hs={}
        for i,n in enumerate(nums):

            t=target-n
            if t in hs:
                return [hs[t],i]
            else:
                hs[n]=i
