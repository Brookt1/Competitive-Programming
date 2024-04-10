# Problem: All Nodes Distance K in Binary Tree - https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        graph = defaultdict(list)
        target = target.val
        stack = [root]
        while stack:
            node =  stack.pop()
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                stack.append(node.left)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                stack.append(node.right)

        queue = deque([[target, 0]])
        visited = set()
        ans = []
        while queue:
            for _ in range(len(queue)):
                node, depth = queue.popleft()
                visited.add(node)
                if depth == k:
                    ans.append(node)
                    continue
                for adj in graph[node]:
                    if adj not in visited:
                        queue.append([adj, depth + 1])    
        return ans

                


        
