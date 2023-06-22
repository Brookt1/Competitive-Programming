#leetcode problem
#56. Merge Intervals


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        arr=intervals
        ans=[]
        for i in range(len(arr)):
            if(i==0):
                ans.append(arr[i])
            else:
                if(arr[i][0]<=ans[-1][1]):
                    if(ans[-1][1] <=arr[i][1]):
                        ans[-1][1]=arr[i][1]
                else:
                    ans.append(arr[i])
        return ans