# Problem: Assign Cookies - https://leetcode.com/problems/assign-cookies

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        child_ptr = 0
        
        for cook_ptr in range(len(s)):
            if child_ptr < len(g) and s[cook_ptr] >= g[child_ptr]:
                child_ptr += 1
        return child_ptr