# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        memo = {}
        def dp(idx, buy):
            if idx >= len(prices):
                return 0
            state = (idx, buy)
            if state not in memo:
                if buy:
                    memo[state] = max(-prices[idx] + dp(idx + 1, False), dp(idx + 1, True))
                else:
                    memo[state] = max(prices[idx] + dp(idx + 2, True), dp(idx + 1, False))
            return memo[state]
        return dp(0, True)