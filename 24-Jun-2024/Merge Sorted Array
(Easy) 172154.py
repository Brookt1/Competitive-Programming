# Problem: Merge Sorted Array
(Easy) - https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        k,fir,sec=m+n-1,m-1,n-1
        while sec>=0 and fir>=0:
            if nums2[sec]>nums1[fir]:
                nums1[k]=nums2[sec]
                
                sec-=1
            else:
                nums1[k]=nums1[fir]
                fir-=1
            k-=1
        while sec>=0:
            nums1[k]=nums2[sec]
            k-=1
            sec-=1
