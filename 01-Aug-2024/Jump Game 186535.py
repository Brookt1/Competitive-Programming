# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        idx = 1
        pos_move = nums[0]
        while pos_move > 0 and idx < len(nums):
            pos_move -= 1
            pos_move = max(pos_move, nums[idx])
            idx += 1
        return idx == len(nums)