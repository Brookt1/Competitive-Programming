# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        memo = {}
        def dp(idx, sum):
            if idx == len(nums):
                if sum == target:
                    return 1
                return 0
            state = (idx, sum)
            if state not in memo:
                memo[state] = dp(idx + 1, sum + nums[idx]) + dp(idx + 1, sum - nums[idx])
            return memo[state]
        return dp(0, 0)
