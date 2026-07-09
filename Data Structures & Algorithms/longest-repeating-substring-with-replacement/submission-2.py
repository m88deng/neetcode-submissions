class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start, end = 0, 0
        res = 0
        distinct = collections.defaultdict(int) #char, freq in window

        maxf = 0
        while end < len(s):
            distinct[s[end]] += 1 #increase window, increase frequency
            maxf = max(maxf, distinct[s[end]])
            while end - start + 1 - maxf > k:
                distinct[s[start]] -= 1 #reduce window, reduce frequency
                start += 1
            res = max(res, end - start + 1)
            end += 1
        return res

            
