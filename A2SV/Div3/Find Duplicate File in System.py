class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        hs,ans={},[]
        for path in paths:
            path=path.split()
            dir=path[0]
            for i in range(1,len(path)):
                index=path[i].index('(')
                fileName=path[i][0:index]
                content=path[i][index+1:]
                if content in hs:
                    hs[content].append(dir+'/'+fileName)
                else:
                    hs[content]=[dir+'/'+fileName]
        for value in hs.values():
            if len(value)>1:ans.append(value)
        return ans

