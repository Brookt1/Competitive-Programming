# Problem: Integer Break - https://leetcode.com/problems/integer-break/

class Solution:
    def integerBreak(self, n: int) -> int:
        

        memo = {}
        def dp(num, dec):
            if num == 0:
                return 1
            if n < 0 or dec > num or dec == n:
                return 0
            
            if num not in memo:
                memo[num] = max(dec * dp(num - dec, dec), dp(num, dec + 1))
            return memo[num]
        return dp(n, 1)
