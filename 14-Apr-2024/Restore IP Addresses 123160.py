# Problem: Restore IP Addresses - https://leetcode.com/problems/restore-ip-addresses/

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        

        ans = []
        def backtrack(idx, path):
            if len(path) == 3 or idx >= len(s) :
                if idx < len(s) and (idx == len(s) - 1 or s[idx] != '0') and int(s[idx:]) <= 255:
                    path.append(s[idx:])
                    ans.append('.'.join(path))
                return 
            path.append(s[idx])
            backtrack(idx + 1, path.copy())
            path.pop()
            for i in range(2, 4):
                if s[idx] != '0' and int(s[idx:idx + i]) <= 255:
                    path.append(s[idx:idx + i])
                    backtrack(idx + i, path[:])
                    path.pop()
        backtrack(0, [])
        return ans
            