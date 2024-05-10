# Problem: N-th Tribonacci Number - https://leetcode.com/problems/n-th-tribonacci-number/description/

class Solution:
    def tribonacci(self, n: int) -> int:
        
        memo = {0: 0, 1:1, 2:1}
        def dp(n):
            if n not in memo:
                memo[n] = dp(n - 1) + dp(n - 2) + dp(n - 3)
            return memo[n]
        return dp(n)