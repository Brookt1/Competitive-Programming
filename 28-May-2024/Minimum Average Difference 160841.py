# Problem: Minimum Average Difference - https://leetcode.com/problems/minimum-average-difference/

class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        

        n = len(nums)
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        
        _min = float('inf')
        ans = 0

        for i in range(1, n + 1):
            if i == n:
                average = (prefix[i]) // i 
            else:
                average = abs((prefix[i]) // i - (prefix[n] - prefix[i]) // (n - i))
            if average < _min:
                ans  = i - 1
                _min = average
        return ans

