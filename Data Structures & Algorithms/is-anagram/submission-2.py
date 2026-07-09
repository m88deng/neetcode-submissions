class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = dict()
    

        for c in s:
            if c not in d:
                d[c] = 0
            else:
                d[c] += 1
        
        for c in t:
            if c not in d:
                return False
            elif d[c] == 0:
                d.pop(c)
            else:
                d[c] -= 1

        return len(d) == 0
            
        