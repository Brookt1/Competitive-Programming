# Problem: Maximum Segment Sum After Removals - https://leetcode.com/problems/maximum-segment-sum-after-removals/description/

class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
            
        def find(x):

            while x != root[x]:
                root[x] =  root[root[x]]
                x = root[x]
            return x
        def union(a, b):
            rootA = find(a)
            rootB = find(b)
            if rootA != rootB:
                if rank[rootA] > rank[rootB]:
                    total[rootA] += total[rootB]
                    root[rootB] = rootA
                elif rank[rootA] < rank[rootB]:
                    total[rootB] += total[rootA]
                    root[rootA] = rootB
                else:
                    total[rootA] += total[rootB]
                    root[rootB] = rootA
                    rank[rootA] += 1
    
        n = len(nums)
        root = [i for i in range(n)]
        rank = [0]* n
        total = [0]*n
        _max = 0
        on = [False]*n
        ans = [0]
        for i in range(n - 1, 0, -1):
            idx = removeQueries[i]
            on[idx] = True
            total[idx] = nums[idx]

            if idx < n - 1 and on[idx + 1]:
                union(idx, idx + 1)
            if idx > 0 and on[idx - 1]:
                union(idx, idx - 1)
            if total[find(idx)] > _max:
                _max = total[find(idx)]
            ans.append(_max)
        return reversed(ans)





        