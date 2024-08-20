# Problem: Number of Good Pairs - https://leetcode.com/problems/number-of-good-pairs/

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        dic = Counter(nums)
        ans = 0
        for num in dic.values():
            ans += num * (num - 1) // 2
        return ans