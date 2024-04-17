# Problem: Top K Frequent Words - https://leetcode.com/problems/top-k-frequent-words/

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        heap = []
        count = Counter(words)
        for key, val in count.items():
            heappush(heap, [-1*val, key])
        ans = []
        for k in range(k):
            ans.append(heappop(heap)[1])
        return ans
        

