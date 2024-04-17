# Problem: Find Median from Data Stream - https://leetcode.com/problems/find-median-from-data-stream/

class MedianFinder:

    def __init__(self):
        self.count = 0
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        if self.count % 2:
            heappush(self.min_heap, num)
        else:
            heappush(self.max_heap, -1*num)
        if self.count > 1:
            if self.min_heap[0] < -1*self.max_heap[0]:
                _max = -1*self.max_heap[0]
                _min = self.min_heap[0]
                heapreplace(self.max_heap, -1 * _min)
                heapreplace(self.min_heap, _max)
        self.count += 1

    def findMedian(self) -> float:
        if self.count % 2:
            return -1*self.max_heap[0]
        else:
            return (-1*self.max_heap[0] + self.min_heap[0])/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()