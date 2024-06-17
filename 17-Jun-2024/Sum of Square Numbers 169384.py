# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        

        sqrts = set()
        n = 0
        while n * n <= c:
            sqrts.add(n * n)
            n += 1
        
        for i in range(n + 1):
            if c - i * i in sqrts:
                return True
        return False