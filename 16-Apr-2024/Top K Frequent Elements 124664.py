# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        n = len(nums)
        buckets = [[] for _ in range(n + 1)]
        res = []
        for key, val in count.items():
            buckets[val].append(key)
        for bucket in buckets:
            res.extend(bucket)
        return res[-k:]



