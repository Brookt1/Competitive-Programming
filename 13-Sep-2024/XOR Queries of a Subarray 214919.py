# Problem: XOR Queries of a Subarray - https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        
        pref = [0]
        for num in arr:
            pref.append(pref[-1] ^ num)
        
        ans = []
        for left, right in queries:
            ans.append(pref[right + 1] ^ pref[left])
        return ans

         