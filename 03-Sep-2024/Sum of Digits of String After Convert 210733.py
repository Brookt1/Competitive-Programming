# Problem: Sum of Digits of String After Convert - https://leetcode.com/problems/sum-of-digits-of-string-after-convert/

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        
        def sum(arr):
            temp = 0
            for num in arr:
                temp += int(num)
            return temp 
        
        arr = ''
        for ch in s:
            arr += str(ord(ch) - ord('a') + 1)


        for _ in range(k):
            print(arr)
            temp = ''
            for num in str(sum(arr)):
                temp += num
            arr = temp
        return int(arr)
        

        