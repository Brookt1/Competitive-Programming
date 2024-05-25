# Problem: Minimum Operations to Reduce X to Zero - https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:


        left = 0
        _sum = 0
        total = sum(nums)
        ans = float('inf')
        for right in range(len(nums)):
            _sum += nums[right]
            while left <= right and  _sum + x > total:
                _sum -= nums[left]
                left += 1
            temp = len(nums) - ((right - left) + 1)
            if _sum + x == total and temp <  ans:
                ans = temp
        if ans < float('inf'):
            return ans
        return -1



