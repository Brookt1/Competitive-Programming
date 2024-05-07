# Problem: Single Number III - https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        xor = 0
        for num in nums:
            xor ^= num
        bit = 0
        while xor & 1 == 0:
            xor >>= 1
            bit += 1
        one = zero = 0
        for num in nums:
            if (num >> bit) & 1:
                one ^= num
            else:
                zero ^= num
        return [one, zero]


        