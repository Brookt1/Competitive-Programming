# Problem: Construct String from Binary Tree - https://leetcode.com/problems/construct-string-from-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        

        def dfs(node):
            if node.left is None and node.right is None:
                return str(node.val)
            
            left = right = None
            if node.left:
                left = dfs(node.left)
            if node.right:
                right = dfs(node.right)
            
            if left and right:
                return str(node.val) + '(' + left + ')'+ '(' + right + ')'
            if right:
                return str(node.val) + '()' + '(' + right + ')'
            return str(node.val) + '(' + left + ')'
        return dfs(root) 