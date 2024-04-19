# Problem: Meeting Rooms III - https://leetcode.com/problems/meeting-rooms-iii/

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        
        meetings.sort()

        heap = []
        idx_heap = []
        val = [0]*n
        for i in range(n):
            heappush(idx_heap, i)

        for start, end in meetings:
            while heap and heap[0][0] <= start:
                heappush(idx_heap, heappop(heap)[1])
            
            if len(heap) < n:
                idx = heappop(idx_heap)
                val[idx] += 1
                heappush(heap, [end, idx])
            else:
                cur, idx = heappop(heap)
                val[idx] += 1
                heappush(heap, [cur + end - start, idx])
        return val.index(max(val))
