# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        

        ans = []
        def bt(idx, path):
            if idx == len(s):
                ans.append(''.join(path))
                return
            if s[idx].isdigit():
                bt(idx + 1, path + [s[idx]])
            else:
                bt(idx + 1, path + [s[idx].lower()])
                bt(idx + 1, path + [s[idx].upper()])
        bt(0, [])
        return ans