# Problem: Minimum Number of Vertices to Reach All Nodes - https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        

        out_degree = [0] * n
        for a, b in edges:
            out_degree[b] += 1
        ans = []
        for idx,  degree in enumerate(out_degree):
            if degree == 0:
                ans.append(idx)
        return ans 