# Problem: Climbing Stairs - https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:

        memo = {}
        def dfs(n):
            if n == 0:
                return 1
            if n < 0:
                return 0
            if n in memo:
                return memo[n]
            memo[n] = dfs(n - 1) + dfs(n - 2)
            return memo[n]
        return dfs(n)
            
