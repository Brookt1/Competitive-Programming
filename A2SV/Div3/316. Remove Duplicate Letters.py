class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        idx={}
        res=[]
        vis=set()
        for i in range(len(s)):
            idx[s[i]]=i

        for i in range(len(s)):
            if s[i] not in vis:
                while res and res[-1]>s[i] and idx[res[-1]] > i :
                    vis.remove(res.pop())
                res.append(s[i])
                vis.add(s[i])
            
            
        return "".join(res)
