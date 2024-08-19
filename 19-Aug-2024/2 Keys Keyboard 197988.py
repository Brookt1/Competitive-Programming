# Problem: 2 Keys Keyboard - https://leetcode.com/problems/2-keys-keyboard/description/

class Solution:
    def minSteps(self, n: int) -> int:
 
        div = 2
        ans = 0
        while div * div  <= n:
            if n % div == 0:
                n //= div
                ans += div
            else:
                div += 1
        if n > 1:
            ans += n
        return ans