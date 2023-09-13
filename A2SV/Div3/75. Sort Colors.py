class Solution:
    def sortColors(self, nums: List[int]) -> None:

        cou=[0,0,0]
        for num in nums:
            cou[num]+=1
        ptr=0
        for i in range(len(nums)):
            while not cou[ptr]: ptr+=1
            nums[i]=ptr
            cou[ptr]-=1
