# Problem: Long Pressed Name - https://leetcode.com/problems/long-pressed-name/

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        
        if typed[0]!=name[0]: return False
        second=0
        for first in range(len(name)):
            while second<len(typed) and name[first]!=typed[second]:
                if typed[second-1]==typed[second]:
                    second+=1
                else:   
                    return False
            if second==len(typed):
                return False
            second+=1
        if len(set(typed[second-1:]))>1:
            return False
        return True