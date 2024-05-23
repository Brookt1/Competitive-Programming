# Problem: Perfect Squares - https://leetcode.com/problems/perfect-squares/

class Solution:
    def numSquares(self, n: int) -> int:
        
        perfect_sqr = []
        i = 1
        while i * i <= n:
            perfect_sqr.append(i * i)
            i += 1 
        dp = [float('inf')] * (n + 1)
        dp[0]  = 1
        for num in perfect_sqr:
            dp[num] = 1
            for i in range(num + 1, n + 1):
                dp[i] = min(dp[i], dp[num] + dp[i - num ])
        return dp[n]