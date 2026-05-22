class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        r = 0
        res = 0 

        if not s: 
            return 0
        if len(s) == 1: 
            return 1
        while r < len(s): 
            while s[r] in seen: 
                seen.discard(s[l])
                l += 1

            seen.add(s[r])
            res = max(res, r - l + 1)
            r += 1
        return res
