# Problem: Number of Smooth Descent Periods of a Stock - https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        

        last = 0
        ans = 0
        for i in range(1, len(prices)):
            if prices[i - 1] != prices[i] + 1:
                n = i - last
                ans += (n * (n + 1)) // 2
                last = i
        n = len(prices) - last 
        ans +=  (n * (n + 1))// 2
        return ans