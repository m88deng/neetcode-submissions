class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False

        s1chars, s2chars = [0] * 26, [0] * 26

        for c in s1:
            s1chars[ord(c) - ord('a')] += 1
        
        for c in s2[:len(s1)]:
            s2chars[ord(c) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            if s1chars[i] == s2chars[i]: matches += 1

        if matches == 26: return True

        start, end = 0, len(s1) - 1
        #[ a b ] c d e
        # end = 1
        while matches != 26:
            print("debug")
            for i in range(26):
                if s1chars[i] != s2chars[i]:
                    print(chr(i + ord('a')), s1chars[i], s2chars[i])
            print("matches: " + str(matches) + '\n')
            if end + 1 == len(s2): return False 
            c1 = s2[start]
            if s1chars[ord(c1) - ord('a')] == s2chars[ord(c1) - ord('a')]: matches -= 1
            s2chars[ord(c1) - ord('a')] -= 1 
            if s1chars[ord(c1) - ord('a')] == s2chars[ord(c1) - ord('a')]: matches += 1
            start += 1
            end += 1
            
            c2 = s2[end]
            if s1chars[ord(c2) - ord('a')] == s2chars[ord(c2) - ord('a')]: matches -= 1
            s2chars[ord(c2) - ord('a')] += 1
            if s1chars[ord(c2) - ord('a')] == s2chars[ord(c2) - ord('a')]: matches += 1

        return True

            
        