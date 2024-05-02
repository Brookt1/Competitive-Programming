# Problem: Maximum XOR for Each Query - https://leetcode.com/problems/maximum-xor-for-each-query/

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        

        n = len(nums)
        _max = (1 << maximumBit )- 1
        print(_max)
        xor = 0
        for num in nums:
            xor ^= num
        ans = []
        for i in range(n):
            ans.append(xor ^ _max)
            xor ^= nums[n - (i + 1)]
        return ans
        
