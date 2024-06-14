# Problem: Minimum Increment to Make Array Unique - https://leetcode.com/problems/minimum-increment-to-make-array-unique/

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        

        nums.sort()
        cur = nums[0]
        ans = 0
        for num in nums[1:]:
            if num <= cur:
                ans +=cur - num + 1
                cur += 1
            else:
                cur = num
        return ans
        