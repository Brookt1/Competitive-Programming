# Problem: Heaters  - https://leetcode.com/problems/heaters/

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
    
        ans = 0
        heaters.sort()
        for num in houses:
            left, right = 0, len(heaters) - 1
            dis = float('inf')
            while left <= right:
                mid = left + (right - left)//2
                dis = min(dis, abs(num - heaters[mid]))  
                if num - heaters[mid] < 0:
                    right = mid - 1
                else:
                    left = mid + 1
            print(num, dis)
            ans = max(ans, dis)
        return ans
