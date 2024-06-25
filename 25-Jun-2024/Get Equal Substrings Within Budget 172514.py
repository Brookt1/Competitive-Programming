# Problem: Get Equal Substrings Within Budget - https://leetcode.com/problems/get-equal-substrings-within-budget/

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:


        left = ans = cost = 0
        for right in range(len(t)):
            cost += abs(ord(t[right]) - ord(s[right]))
            while cost > maxCost:
                cost -= abs(ord(t[left]) - ord(s[left]))
                left += 1

            ans = max(ans, right - left + 1)
        return ans