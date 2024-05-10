# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        

        memo = {}

        def dp(idx, amount):
            if amount <= 0 or idx == len(coins):
                if amount == 0:
                    return 0
                return float('inf')

            state = (idx, amount)
            if state not in memo:
                memo[state] = min(dp(idx, amount - coins[idx]) + 1, dp(idx + 1, amount))

            return memo[state]
        ans = dp(0, amount)
        if ans < float('inf'):
            return ans
        return -1
                    

