# Problem: Longest Palindromic Substring - https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        word = ''
        for i in range(l):
            for j in range(i, l):
                if j - i + 1 > len(word) and s[i : j + 1] == s[i:j + 1][::-1]:
                    word = s[i : j + 1]
        return word