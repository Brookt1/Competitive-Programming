class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       from collections import Counter
       ha=dict(Counter(s))
       if len(s)!=len(t):
           return False
       for i in s:
           if ha[i]!=t.count(i):
               return False
       return True
