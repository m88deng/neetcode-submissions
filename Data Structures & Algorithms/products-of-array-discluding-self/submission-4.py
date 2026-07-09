class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        has_zero = False
        for n in nums:
            if n == 0 and not has_zero:
                has_zero = True
                continue
            total *= n

        res = []
        for n in nums:
            if not has_zero:
                res.append(total // n)
            else:
                if n == 0:
                    res.append(total)
                else: 
                    res.append(0)
        return res
