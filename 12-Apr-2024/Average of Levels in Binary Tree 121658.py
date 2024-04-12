# Problem: Average of Levels in Binary Tree - https://leetcode.com/problems/average-of-levels-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:


        queue = deque([root])
        visited = set()
        ans = []
        while queue:

            boundery = len(queue)
            cur_level = []

            for _ in range(boundery):
                node = queue.popleft()
                cur_level.append(node.val)
                visited.add(node)
                if node.left and node.left not in visited:
                    queue.append(node.left)
                if node.right and node.right not in visited:
                    queue.append(node.right)
            ans.append(sum(cur_level)/len(cur_level))
        return ans


