# Problem: Palindrome Partitioning - https://leetcode.com/problems/palindrome-partitioning/

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        n = len(s)
        memo = {}
        def is_palindrome(s):
            if s not in memo:
                memo[s] = s == s[::-1]
            return memo[s]

        def dfs(idx, cur):
            if idx == n:
                res.append(cur.copy())
                return
            
            for i in range(idx, n):
                if  is_palindrome(s[idx:i + 1]):
                    dfs(i + 1, cur + [s[idx:i + 1]])
        dfs(0, [])
        return res

