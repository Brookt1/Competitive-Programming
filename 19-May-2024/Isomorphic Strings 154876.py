# Problem: Isomorphic Strings - https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        dic = {}
        mapped  = set()
        for i in range(len(s)):
            if (s[i] in  dic and dic[s[i]] != t[i] ) or t[i] in mapped and s[i] not in dic:
                return False
            if s[i] not in dic:
                dic[s[i]] = t[i]
                mapped.add(t[i])
        return True