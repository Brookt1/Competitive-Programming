# Problem: Minimize the Maximum of Two Arrays - https://leetcode.com/problems/minimize-the-maximum-of-two-arrays/

class Solution:
    def minimizeSet(self, d1: int, d2: int, C1: int, C2: int) -> int:
        

        def good(mid):
            return mid - mid // d1 >= C1 and mid - mid // d2 >= C2 and mid - mid // common >= C1 + C2
        left, right, common = 0, int(1e10), lcm(d1, d2)
        while left < right:
            mid = (right + left) // 2
            if good(mid):
                right = mid
            else:
                left = mid + 1
        return left
