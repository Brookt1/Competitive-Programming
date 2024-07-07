# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        


        position.sort()
        n = len(position)
        def good(mid):
            count , ptr = 1, 0
            for i in range(n):
                if ptr < n and position[i] - position[ptr] >= mid:
                    count += 1
                    ptr = i
                    if count == m:
                        return True
            return False

        left , right = 0, int(1e9) + 1

        while left <= right:
            mid = left + (right - left) // 2

            if good(mid):
                left = mid + 1
            else:
                right = mid - 1
        return left - 1