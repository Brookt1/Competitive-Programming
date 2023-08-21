class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      #sliding windows problem
        # My first code without making the code clean.
        # l,r=0,0
        # ch=set()
        # ans=0
        # while r<len(s):
        #     if s[r] in ch:
        #         while l<=r:
        #             if s[r] in ch:
        #                 ch.remove(s[l])
        #                 l+=1
        #             else:
        #                 ch.add(s[r])
        #                 break
        #     else:
        #         ch.add(s[r])
        #     ans=max(ans,len(ch))
        #     r+=1
        # return ans

      # The shortest code to the above code
        ans=0
        l,r=0,0
        ch=set()
        while r<len(s):
            while s[r] in ch:
                ch.remove(s[l])
                l+=1
            ch.add(s[r])
            ans=max(ans,r-l+1)
            r+=1  
        return ans
            
