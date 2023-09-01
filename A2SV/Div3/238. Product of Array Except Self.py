class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        pref=1
        ans=[1]*n
        for i in range(1,n):
            pref*=nums[i-1]
            ans[i]=pref
        post=1
        print(ans)
        for i in range(n-2,-1,-1):
            post*=nums[i+1]
            print(post)
            ans[i]=ans[i]*post
        return ans
