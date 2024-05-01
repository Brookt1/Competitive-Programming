# Problem: Longest Nice Substring - https://leetcode.com/problems/longest-nice-substring/

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        
        ans = ''
        for i in range(len(s)):
            small = 0
            capital = 0
            for j in range(i, len(s)):
                if s[j].islower():
                    small = small | (1 << (ord(s[j]) - ord('a')))
                else:
                    capital = capital | (1 << (ord(s[j]) - ord('A')))
                if small == capital and j - i + 1 > len(ans):
                    ans = s[i : j + 1]
        return ans