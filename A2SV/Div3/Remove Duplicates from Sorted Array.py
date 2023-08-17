class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k,fir,sec=1,0,1

        for i in range(0,len(nums)-1):
            if nums[fir]!=nums[sec]:
                if (fir+1)!=sec:
                    nums[fir+1]=nums[sec]
                fir+=1
                k+=1
            sec+=1
        return k
