class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # group anagrams tgt in sublists
        # output in any order

        # make freq dict for each word
        # group maps tgt

        d = defaultdict(list) # freq -> words
        res = []

        for s in strs:
            freq = [0] * 26
            for c in s:
                freq[ord(c)-ord('a')] += 1
            
            d[tuple(freq)].append(s)
            
        return list(d.values())