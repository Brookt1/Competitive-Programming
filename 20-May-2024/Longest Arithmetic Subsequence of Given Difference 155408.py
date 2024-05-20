# Problem: Longest Arithmetic Subsequence of Given Difference - https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/description/

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        

        dic = defaultdict(int)
        for num in arr:   
            diff = num - difference
            if diff in dic:
                dic[num] = max(dic[num], dic[diff] + 1)
            else:
                dic[num] = 1
        return max(dic.values())
