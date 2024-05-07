# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        ans = []
        def backtrack(idx, path):
            if idx == len(s):
                ans.append(''.join(ch for ch in path))
                return
            
            backtrack(idx + 1,path + [s[idx]])
            if s[idx].isalpha():
                if s[idx].isupper():
                    backtrack(idx + 1, path + [s[idx].lower()])
                else:
                    backtrack(idx + 1, path + [s[idx].upper()])
        backtrack(0, [])
        return ans