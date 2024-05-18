# Problem: Car fleet - https://leetcode.com/problems/car-fleet/

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        arr = []
        n = len(position)
        for  i in range(n):
            arr.append([position[i], (target - position[i])/speed[i]])
        arr.sort(reverse = True)
        stack = []
        res = 0
        for pos, left in arr:
            while stack and stack[-1] < left:
                stack.pop()
            if not stack:
                res += 1
            stack.append(left)
        return res
