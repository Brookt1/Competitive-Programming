# Problem: Find Building Where Alice and Bob Can Meet - https://leetcode.com/problems/find-building-where-alice-and-bob-can-meet/

class Solution:
    def leftmostBuildingQueries(
        self, heights: List[int], queries: List[List[int]]
    ) -> List[int]:

        n = len(queries)
        for i in range(n):
            x, y = queries[i]
            queries[i] = [min(x, y), max(x, y), i]

        queries.sort(reverse=True, key = lambda x: x[1])
        def get_min(val):

            left = 0
            right = len(stack) - 1
            while left <= right:
                mid = (right + left) // 2
                if heights[stack[mid]] <= val:
                    right = mid - 1
                else:
                    left = mid + 1

            if right != -1:
                return stack[right]
            return -1

        stack = []
        ans = [-1] * n
        idx = len(heights) - 1
        for i in range(n):
            x, y, j = queries[i]
            if heights[y] > heights[x] or x == y:
                ans[j] = y
            else:
                while idx > y:
                    while stack and heights[stack[-1]] < heights[idx]:
                        stack.pop()
                    stack.append(idx)
                    idx -= 1
                ans[j] = get_min(heights[x])

                print(ans[j], j)

        return ans
