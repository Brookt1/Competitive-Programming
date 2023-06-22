#leetcode problems
#973. K Closest Points to Origin
# best answer````
# class Solution:
    # def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    #     return sorted(points, key = lambda x: (x[0]*x[0] + x[1]*x[1])) [:k]
    


# my answer

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import math
        p=points
        res=[]
        ans=[]
        for i in range(len(points)):
            l=sqrt(p[i][0]*p[i][0]+p[i][1]*p[i][1])
            res.append([l,i])
        res.sort()
        for i in range(k):
            ans.append(p[res[i][1]])
        return ans
