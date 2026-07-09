class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = ""
        for c in s:
            if c.isalnum():
                ss += c.lower()
        
        if ss == "" or len(ss) == 1: return True
        l = 0
        r = len(ss) - 1
        while(l <= r):
            if ss[l] == ss[r]:
                l += 1
                r -= 1
            else:
                return False
        return True
