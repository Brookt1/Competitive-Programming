# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i + 1] =  0
                nums[i] *= 2
        ans = []
        for num in nums:
            if num:
                ans.append(num)
        ans.extend(0 for _ in range(len(nums) - len(ans)))
        return ans