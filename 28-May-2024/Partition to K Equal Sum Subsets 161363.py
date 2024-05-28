# Problem: Partition to K Equal Sum Subsets - https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:

        n = len(nums)
        _sum = sum(nums)
        if _sum % k:
            return False
        target = _sum // k
        memo = defaultdict(bool)
        visited = 0
        def dp(visited, tar):
            if tar < 0:
                return False
            if visited == (pow(2, n) - 1):
                return True
            state = (visited, tar)
            if state not in memo:
                for i in range(len(nums)):
                    if tar == 0:
                        tar = target
                        
                    if visited & (1 << i) == 0:
                        memo[state] = memo[state]  or dp(visited ^  (1 << i), (tar - nums[i])) or dp(visited, tar)
            return memo[state]

        return dp(0, target)