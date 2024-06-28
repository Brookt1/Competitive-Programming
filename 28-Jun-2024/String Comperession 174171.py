# Problem: String Comperession - https://leetcode.com/problems/string-compression/

class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return len(chars)
        next = 0
        start = chars[0]
        curr = 1
        count = 1
        while curr <= len(chars):
            if curr < len(chars) and chars[curr] == start:
                count += 1
            else:
                chars[next] = start
                next += 1
                if count > 1:
                    i = 0
                    count_str = str(count)
                    while i < len(count_str):
                        chars[next] = count_str[i]
                        next += 1
                        i += 1
                start = chars[curr] if curr < len(chars) else None
                count = 1
            curr += 1
        return len(chars[:next])