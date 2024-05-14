# Problem: Coin Change II - https://leetcode.com/problems/coin-change-ii/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        

        memo = {}
        def dp(amount, idx):
            if amount == 0:
                return 1
            if amount < 0 or idx == len(coins):
                return 0
            state = (amount, idx)
            if state not in memo:
                memo[state] = dp(amount - coins[idx], idx) + dp(amount, idx + 1)
            return memo[state]
        return dp(amount, 0)