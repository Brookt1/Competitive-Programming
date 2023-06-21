#Leetcode problem
#2089. Find Target Indices After Sorting Array
# shortes answer in python ---> return [i for i, j in enumerate(sorted(nums)) if j==target]



class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums=sorted(nums)
        ans=[]
        for i in range(len(nums)):
            if(nums[i]==target):
                ans.append(i)
        return ans
