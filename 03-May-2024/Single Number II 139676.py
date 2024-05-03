# Problem: Single Number II - https://leetcode.com/problems/single-number-ii/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        n = len(nums)
        bits = [0 for i in range(33)]
        
        for num in nums:
            if num < 0:
                bits[-1] += 1
                num = abs(num)
            _max = num.bit_length()
            idx = 0
            while num and idx < _max:
                if num & 1 == 1:
                    bits[idx] += 1
                idx += 1
                num >>= 1
        
        ans = []
        t = 2147483648
        for bit in bits:
            if bit % 3 != 0:
                ans.append(str(1))
            else:
                ans.append(str(0))
        ans.reverse()
        return int('0b' + ''.join(ans[1:]), 2) * (-1 if ans[0] != '0' else 1 )