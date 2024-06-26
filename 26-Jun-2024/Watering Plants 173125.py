# Problem: Watering Plants - https://leetcode.com/problems/watering-plants/

class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:

        steps=0
        c=capacity
        for idx,val in enumerate(plants):
            print(steps)
            if c<val:
                steps+=(idx)*2+1
                c=capacity
            else:
                steps+=1
            c-=val
        return steps

        