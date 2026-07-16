class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 1
        
        d = {}
        res = 0
        if len(s) > 0: 
            d[s[start]] = start
            res = 1

        while end < len(s):
            c = s[end]
            if c in d and d[c] >= start:
                start = d[c] + 1
            
            d[c] = end
            end += 1
            res = max(res, end - start)

        return res