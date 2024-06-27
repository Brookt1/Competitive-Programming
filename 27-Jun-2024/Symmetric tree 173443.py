# Problem: Symmetric tree - https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def helper(node1,node2):
            if node1 is None or node2 is None:
                return node1 == node2
            
            left_right = helper(node1.left,node2.right)
            right_left = helper(node1.right,node2.left)

            return node1.val == node2.val and left_right and right_left
        
        return helper(root.left,root.right)

        