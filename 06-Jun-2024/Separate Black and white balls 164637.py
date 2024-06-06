# Problem: Separate Black and white balls - https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:
        


        count = 0
        ans = 0
        for ch in s:
            if ch == '1':
                count += 1
            else:
                ans += count
        return ans