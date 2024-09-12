# Problem: Count the Number of Consistent Strings - https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        allowed_set = set(allowed)
        ans = 0
        for word in words:
            count = 0
            for ch in set(word):
                if ch not in allowed_set:
                    break
                count += 1
            if count == len(set(word)):
                ans += 1
        return ans 
            