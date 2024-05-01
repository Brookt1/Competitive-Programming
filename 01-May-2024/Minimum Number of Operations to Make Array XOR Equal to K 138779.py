# Problem: Minimum Number of Operations to Make Array XOR Equal to K - https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        xor = 0
        for num in nums:
            xor ^= num
        count = 0
        while xor or k:
            if xor & 1 != k & 1:
                count += 1
            xor >>= 1
            k >>= 1
        return count