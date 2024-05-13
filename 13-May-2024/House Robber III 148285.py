# Problem: House Robber III - https://leetcode.com/problems/house-robber-iii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        memo = {}
        def dfs(node, rob):
            if node is None:
                return 0
            state = (node, rob)
            if state not in memo:
                include = 0
                if rob:
                    include = node.val + ( dfs(node.left, False) if node.left else 0) + (dfs(node.right, False) if node.right else 0)
                exclude = (dfs(node.left, True) if node.left else 0) + (dfs(node.right, True) if node.right else 0)
                memo[state] =  max(include, exclude)
            return memo[state]
        return dfs(root, True)
