# Problem: Furthest Building You Can Reach - https://leetcode.com/problems/furthest-building-you-can-reach/

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        

        diff = []
        for i in range(1, len(heights)):
            if heights[i] > heights[i - 1]:
                diff.append(heights[i] - heights[i - 1])
            else:
                diff.append(0)
        heap = []
        idx = 0
        while idx < len(diff):
            if len(heap) < ladders:
                heappush(heap, diff[idx])
            elif not heap or heap[0] >= diff[idx]:
                if diff[idx] > bricks:
                    break
                bricks -= diff[idx]
            else:
                num = heapreplace(heap, diff[idx])
                if num > bricks:
                    break
                bricks -= num
            
            idx += 1
        return idx