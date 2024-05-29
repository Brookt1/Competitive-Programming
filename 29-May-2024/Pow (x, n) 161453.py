# Problem: Pow (x, n) - https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:

        def pow(n):
            if n == 0:
                return 1
            if n == 1:
                return x
            
            val = pow(n // 2)
            if n % 2 == 0:
                return  val * val
            return pow((n + 1) // 2) * val
        if n > 0:
            return pow(n)
        return 1 / pow(-1 * n)