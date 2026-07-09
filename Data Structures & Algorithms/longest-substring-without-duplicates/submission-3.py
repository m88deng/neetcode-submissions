class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end = 0, 0
        seen = defaultdict(int)
        length = 0

        if len(s) <= 1:
            return len(s)
        
        #abba, start = 2, end = 3, length = 2
        # seen: a:0, b:2
        while end < len(s):
            c = s[end] #a
            if c in seen:
                start = max(start, seen[c] + 1)
            seen[c] = end
            length = max(length, end - start + 1) 
            end += 1
        return length