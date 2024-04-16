# Problem: Kth Largest Element in a Stream - https://leetcode.com/problems/kth-largest-element-in-a-stream/

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        for i in range(len(nums)):
            if len(self.heap) < k:
                heappush(self.heap, nums[i])
            elif self.heap[0] < nums[i]:
                heapreplace(self.heap, nums[i])
        self.k = k
    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heappush(self.heap, val)
        elif self.heap[0] < val:
            heapreplace(self.heap, val)
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)