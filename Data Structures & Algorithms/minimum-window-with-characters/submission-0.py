class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # a way to know all chars in t
        if t == "":
            return ""

        def char_to_index(c: str) -> int:
            return ord(c) - ord('A') if c.isupper() else ord(c) - ord('a') + 26
        
        seen = {}
        tchars = {}
        for c in t:
            tchars[c] = 1 + tchars.get(c, 0)
        
        count = len(tchars)
        matches = 0
        length = float("inf")
        res = [0, 0]
        l = 0
        for r in range(len(s)):
            c = s[r]
            seen[c] = 1 + seen.get(c, 0)

            if c in tchars and seen[c] == tchars[c]:
                matches += 1

            print(s[l:r])  

            while count == matches:
                if r - l + 1 < length:
                    length = r - l + 1
                    res = [l, r]

                seen[s[l]] -= 1
                if s[l] in tchars and seen[s[l]] < tchars[s[l]]: matches -= 1
                l += 1
                
        l ,r = res
        return "" if length == float("inf") else s[l:r + 1]
        
        
        # sliding window starting with len(t)

        #[OUZ]
        # if i can find all letters of t here
        # record length >= len(t)
        # return substring window
        
            # increase r
            # check if added char matches
            # decrease l if s[l] not in t
            # if all strings in t are in substr
            # record len, res
            # while s[l] not in t, l += 1


        # if cannot find all letters of t
        # if s[l] not in t: shrink start
        # expand right:

