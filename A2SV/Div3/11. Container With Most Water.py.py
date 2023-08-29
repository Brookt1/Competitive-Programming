class Solution:
    def maxArea(self, height: List[int]) -> int:

        l,r=0,len(height)-1
        maxV=0
        while l<r:
            m=height[r] if height[r]<height[l] else height[l]
            maxV=max(maxV,(r-l)*m)
            if height[l]<height[r]:
                l+=1
            else: 
                r-=1
        return maxV


