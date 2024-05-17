# Problem: Solving Questions with Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        ans = [0]*(n + 1)
        for i in range(1, n + 1):
            point, brain = questions[i - 1]
            if i != n:
                ans[i + 1] = max(ans[i + 1], ans[i])
            
            ans[i] += point
            if i + brain + 1<= n:
                ans[i + brain + 1] = max(ans[i + brain + 1], ans[i])

        return max(ans)
