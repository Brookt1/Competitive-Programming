# Problem: Merge Intervals (Optional) - https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        

        intervals.sort()
        end = intervals[0][1]
        start = intervals[0][0]
        ans = []
        for right in range(len(intervals)):

            if intervals[right][0] > end:
                ans.append([start, end])
                start = intervals[right][0]
                end = intervals[right][1]
            else:
                end = max(end, intervals[right][1])
        ans.append([start, end])
        return ans
