# Problem: Longest Subarray With Maximum Bitwise AND - https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        

        ans = 1
        count = 0
        _max = max(nums)

        for num in nums:
            if num == _max:
                count += 1
            else:
                ans = max(ans, count)
                count = 0
        ans = max(ans, count)
        return ans