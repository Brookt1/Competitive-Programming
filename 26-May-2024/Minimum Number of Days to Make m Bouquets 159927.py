# Problem: Minimum Number of Days to Make m Bouquets - https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        

        if m * k > len(bloomDay):
            return -1

        def good(mid):
            left = count = 0
            for right in range(len(bloomDay)):
                if bloomDay[right] > mid:
                    left = right + 1
                if (right - left ) + 1 == k:
                    count += 1
                    left = right + 1
            return count >= m
        

        left, right = -1,  max(bloomDay)
        while left < right:
            mid = left + (right - left)//2
            if good(mid):
                right = mid
            else:
                left = mid + 1
        return left
