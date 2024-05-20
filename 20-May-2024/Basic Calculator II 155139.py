# Problem: Basic Calculator II - https://leetcode.com/problems/basic-calculator-ii/

class Solution:
    def calculate(self, s: str) -> int:
        
        def getNum(idx):
            res = []
            while idx < n and s[idx].isdigit() :
                res.append(s[idx])
                idx += 1
            return [int(''.join(res)), idx]

        s = ''.join(s.split())
        n = len(s)
        stack = []
        num, idx = getNum(0)
        stack.append(num)
        while idx < n:
            oper = s[idx]
            num , idx = getNum(idx + 1)
            if oper == '*':
                val = stack.pop()
                stack.append(val* num)
            elif oper == '/':
                val = stack.pop()
                stack.append(val // num)
            else:
                stack.append(oper)
                stack.append(num)
        ans = 0

        stack.reverse()
        while len(stack) > 1:
            num1, oper, num2 = stack.pop(), stack.pop(), stack.pop()
            if oper == '+':
                stack.append(num1 + num2)
            else:
    
                stack.append(num1 - num2)

        return stack[0]
