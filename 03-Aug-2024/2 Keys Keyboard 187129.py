# Problem: 2 Keys Keyboard - https://leetcode.com/problems/2-keys-keyboard/description/

class Solution:
    def minSteps(self, n: int) -> int:
        

        ans = 0
        fact = 2
        while fact * fact <= n:
            if n % fact == 0:
                n //= fact
                ans += fact
            else:
                fact += 1
        if n > 1:
            ans += n
        return ans