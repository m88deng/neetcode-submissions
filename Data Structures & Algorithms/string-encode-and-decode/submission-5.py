class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        strs = []
        while(s):
            i = 0
            n = 0
            while(s[i] != "#"):
                print("char" + s[i])
                n = n * 10 + int(s[i])
                i += 1
            strs.append(s[i+1:i+1+n])
            s = s[i+1+n:]
            
        return strs
        
