# Problem: Best Time to Buy and Sell Stock III - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        memo = {}
        def dp(idx, buy, count):
            if idx == len(prices) or count > 2:
                return 0
            state = (idx, buy,count)
            if state not in memo:
                if buy:
                    memo[state] = max(-1 * prices[idx] + dp(idx + 1, False, count + 1), dp(idx + 1, True, count))
                else:
                    memo[state] = max(prices[idx] + dp(idx + 1, True, count), dp(idx + 1, False, count))
            return memo[state]
        return dp(0, True, 0)
                