class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start, end = 0, 0
        res = 0
        distinct = collections.defaultdict(int)

        while end < len(s):
            distinct[s[end]] += 1
            while True:
                length = end - start + 1 
                most_common = max(distinct.values())
                print(distinct)
                # print(most_common)
                if length - most_common > k: 
                    distinct[s[start]] -= 1
                    start += 1
                else: break
            res = max(res, length)
            end += 1
        return res

            
