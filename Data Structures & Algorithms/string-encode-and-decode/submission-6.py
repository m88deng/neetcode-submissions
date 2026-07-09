class Solution:

    def encode(self, strs: List[str]) -> str:
        # list of strings into string
        # use a delimiter, and escape it using \
        #["add," , "banana\" , "happ,y"]
        # add\,,banana\\,happ\,y
        res = ""

        for s in strs:
            for c in s:
                if c == ',' or c == '\\': #char
                    res += '\\'
                res += c
            res += ','
        return res
                

    def decode(self, s: str) -> List[str]:
        res = []
        escape = False # true if next char is a char
        word = ""

        for c in s:
            if not escape:
                if c == ',': # separation
                    res.append(word)
                    word = ""
                    continue

                if c == '\\': # escape \
                    escape = True
                    continue
                
            word = word + c
            if escape: #next is char to append
                escape = False
        
        return res
                
            

            
