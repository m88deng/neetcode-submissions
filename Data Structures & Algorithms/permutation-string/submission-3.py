class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False

        s1chars, s2chars = [0] * 26, [0] * 26

        for i in range(len(s1)):
            s1chars[ord(s1[i]) - ord('a')] += 1
            s2chars[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            if s1chars[i] == s2chars[i]: matches += 1

        start = 0
        for end in range(len(s1), len(s2)):
            if matches == 26: return True
            
            index = ord(s2[end]) - ord('a')
            s2chars[index] += 1
            if s1chars[index] == s2chars[index]: 
                matches += 1
            elif s1chars[index] + 1 == s2chars[index]: 
                matches -= 1

            idx = ord(s2[start]) - ord('a')
            s2chars[idx] -= 1 
            if s1chars[idx] == s2chars[idx]: 
                matches += 1
            elif s1chars[idx] - 1 == s2chars[idx]: 
                matches -=1
            start += 1
            
        return matches == 26
            
        