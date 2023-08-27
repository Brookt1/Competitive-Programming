class Solution:
    def arrayChange(self, nums: List[int], oper: List[List[int]]) -> List[int]:
        
        hs,n={},len(nums)
        for i in range(n):
            hs[nums[i]]=i
        for i in range(len(oper)):
            ind=hs[oper[i][0]]
            del hs[oper[i][0]]
            hs[oper[i][1]]=ind
        
        ans=[0]*(n)

        for key,val in hs.items():
            ans[val]=key
        return ans
