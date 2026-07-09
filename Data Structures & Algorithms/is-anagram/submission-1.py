class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_dict = {}
        for c in s:
            if c in my_dict:
                my_dict[c] += 1
            else:
                my_dict[c] = 1
        
        for c in t:
            if c in my_dict:
                my_dict[c] -= 1
                if my_dict[c] == 0:
                    my_dict.pop(c)
            else: 
                return False
        return len(my_dict) == 0
        
        