# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:

        n=len(s)
        prefix=[0]*n
        for l,r,val in shifts:
            if val:
                prefix[l]+=1
                if r+1<n:
                    prefix[r+1]-=1
            else:
                prefix[l]-=1
                if r+1<n:
                    prefix[r+1]+=1
        for i in range(1,n):
            prefix[i]+=prefix[i-1]
        res=[]
        for i in range(n):
            res.append(chr(97 + (ord(s[i])%97+prefix[i]%26)%26))
        return ''.join(res)
        