class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans=''
        ind=0
        n=len(spaces)
        for i in range(len(s)):
            if ind<n and spaces[ind]==i:
                ans+=' '
                ind+=1
            ans+=s[i]
        return ans
