# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        memo = {}
        def dp(idx):

            if  idx >= len(nums):
                return 0
            if idx not in memo:
                memo[idx] = max(dp(idx + 2), dp(idx + 3))


            return  memo[idx] + nums[idx]
        return max(dp(0), dp(1))
