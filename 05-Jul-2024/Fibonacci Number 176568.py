# Problem: Fibonacci Number - https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        
        if n < 2:
            return n
        n1, n2 = 0, 1
        x = 0
        while n > 0:
            temp = n1
            n1 +=  n2
            n2 = temp
            n -= 1
        return n1