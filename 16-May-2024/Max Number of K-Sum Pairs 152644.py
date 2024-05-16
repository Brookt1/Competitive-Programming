# Problem: Max Number of K-Sum Pairs - https://leetcode.com/problems/max-number-of-k-sum-pairs/

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        left, right = 0, len(nums) - 1
        count = 0
        while left < right:
            _sum = nums[left] + nums[right]
            if _sum == k:
                count += 1
                left += 1
                right -= 1
            elif _sum < k:
                left += 1
            else:
                right -= 1
        return count
