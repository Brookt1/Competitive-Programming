# Problem: First Missing Positive - https://leetcode.com/problems/first-missing-positive/description/

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        

        n = len(nums)

        idx = 0
        while idx < n:
            num = nums[idx]
            if idx + 1 == num:
                idx += 1
            elif 0 < num < n + 1 and nums[num - 1] != num:
                nums[num - 1], nums[idx] = num, nums[num - 1]
            else:
                nums[idx] = 0
                idx += 1

        for i in range(n):
            if nums[i] == 0:
                return i + 1
        return n + 1