# Problem: Minimum XOR Sum of Two Arrays - https://leetcode.com/problems/minimum-xor-sum-of-two-arrays/

class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:

        n = len(nums1)
        memo = defaultdict(lambda : float('inf'))
        def dp(idx, visited):
            if idx == n:
                return 0
            state = (idx, visited)
            if state not in memo:
                for i in range(n):
                    if visited & (1 << i) == 0:
                        memo[state] = min(memo[state],(nums1[idx] ^ nums2[i]) + dp(idx + 1, visited ^ (1 << i)))
            return memo[state]
        return dp(0, 0)