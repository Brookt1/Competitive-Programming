# Problem: Find Pivot Index - https://leetcode.com/problems/find-pivot-index/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        


        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        
        for i in range(1, len(prefix)):
            if prefix[i - 1] == prefix[-1] - prefix[i]:
                return i -  1
        return -1