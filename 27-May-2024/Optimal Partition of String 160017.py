# Problem: Optimal Partition of String - https://leetcode.com/problems/optimal-partition-of-string/

class Solution:
    def partitionString(self, s: str) -> int:
        

        substrings = set()
        ans = 1
        for ch in s:
            if ch in substrings:
                substrings = set()
                ans += 1
            substrings.add(ch)
        return ans