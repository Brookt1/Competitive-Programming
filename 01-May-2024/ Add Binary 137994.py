# Problem:  Add Binary - https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        def add(a, b):
            return [a ^ b, a & b]
        
        rem = 0
        ans = []
        first , second = len(a) - 1, len(b) - 1
        while first > -1 and second > -1:
            res, temp = add(int(a[first]), int(b[second]))
            res, rem = add(res, rem)
            rem = max(temp, rem)
            ans.append(res)
            first -= 1
            second -= 1 
        
        while first > -1:
            res, rem = add(int(a[first]), rem)
            ans.append(res)
            first -= 1
        while second > -1:
            res, rem = add(int(b[second]), rem)
            ans.append(res)
            second -= 1
        if rem:
            ans.append(rem)

        return ''.join(str(s) for s in reversed(ans))