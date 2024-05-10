# Problem: Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        min_val = prices[0]
        for num in prices:
            if num < min_val:
                min_val = num
            else:
                ans = max(ans, num - min_val)
        return ans