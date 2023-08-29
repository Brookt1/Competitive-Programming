class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        m = {val: i for i, val in enumerate(s)}

        l,r,e=0,0,m[s[0]]
        ans=[]
        while r<len(s):
            if r==e:
                ans.append(r-l+1)
                l= r+1 if r+1<len(s) else r
                e=m[s[l]]
            elif m[s[r]]>e:
                e=m[s[r]]
            r+=1
        return ans
