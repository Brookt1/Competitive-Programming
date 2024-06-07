# Problem: Max Numbers of K sums - https://leetcode.com/problems/max-number-of-k-sum-pairs

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        

        nums.sort()
        left, right = 0, len(nums) - 1

        ans = 0
        while left < right:
            _sum = nums[left] + nums[right]
            if _sum < k:
                left += 1
            elif _sum > k:
                right -= 1
            else:
                ans += 1
                left += 1
                right -= 1
        return ans