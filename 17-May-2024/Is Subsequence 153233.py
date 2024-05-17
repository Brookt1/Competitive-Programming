# Problem: Is Subsequence - https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        m = len(t)
        n = len(s)
        j = -1
        for i in range(n):
            j += 1
            while j < m and s[i] != t[j]:
                j += 1
            if j == m:
                return False
        return True

            

