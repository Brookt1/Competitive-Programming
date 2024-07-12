# Problem: String Compression - https://leetcode.com/problems/string-compression/

class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return len(chars)
        next = 0
        start = chars[0]
        curr = count = 1
        while curr <= len(chars):
            if curr < len(chars) and chars[curr] == start:
                count += 1
            else:
                chars[next] = start
                next += 1
                if count > 1:
                    for ch in str(count):
                        chars[next] = ch
                        next += 1
                start = chars[curr] if curr < len(chars) else None
                count = 1
            curr += 1
        return len(chars[:next])