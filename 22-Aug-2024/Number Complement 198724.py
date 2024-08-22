# Problem: Number Complement - https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        
        ans = [0]*31
        n = 0
        while num > 0: 
            ans[n] =  0 if 1 & num else 1
            num >>= 1
            n += 1
        return int(''.join(str(x) for x in ans[::-1]), 2)