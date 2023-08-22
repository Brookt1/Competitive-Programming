class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        hs,ans={},[]
        
        for d in cpdomains:
            count, d=d.split()
            count=int(count)
            d=d.split('.')
            cur=''
            for sub in reversed(d):
                if cur=='':
                    cur=sub
                else:
                    cur=sub+'.'+cur
                if cur in hs:
                    hs[cur]+=count
                else:
                    hs[cur]=count
        for key,value in hs.items():
            ans.append(str(value) + ' ' + key)
        return ans
