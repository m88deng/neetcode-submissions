class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        from collections import defaultdict
        d = defaultdict(int)

        for n in nums:
            d[n] += 1
            if d[n] == 2:
                return True

        return False
