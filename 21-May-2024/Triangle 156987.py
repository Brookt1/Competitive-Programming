# Problem: Triangle - https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1:
            return triangle[0][0]
        n = len(triangle)
        dp = [[0] * n for _ in range(n) ]
        for i in range(n):
            dp[n - 1][i] = triangle[n - 1][i]
        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                dp[i][j] =triangle[i][j] + min( dp[i + 1][j],  dp[i + 1][j + 1])
 
        return dp[0][0]
