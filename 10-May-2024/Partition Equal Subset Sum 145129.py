# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        

        n = len(nums)
        target = sum(nums)
        if target % 2:
            return False
        target //= 2
        memo = {}
        def dp(idx, target):
            if idx == n or target < 1:
                return target == 0
                
            state = (idx, target)
            if state not in memo:
                memo[state] = dp(idx + 1, target - nums[idx]) or dp(idx + 1, target)
            return memo[state]
        return dp(0, target)
