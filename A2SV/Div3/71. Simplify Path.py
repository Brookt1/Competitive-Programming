class Solution:
    def simplifyPath(self, path: str) -> str:

        ans=[]
        cur=''

        for elem in path.split('/'):
            if elem=='..':
                if ans: ans.pop()
            elif elem not in ('.',''):
                ans.append(elem)
        
        return '/' + '/'.join(ans)
