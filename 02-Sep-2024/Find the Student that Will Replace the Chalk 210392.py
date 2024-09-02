# Problem: Find the Student that Will Replace the Chalk - https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/description/

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        

        _sum = sum(chalk)
        k = k % _sum
        for idx, ch in enumerate(chalk):
            if k < ch:
                return idx
            k -= ch
        