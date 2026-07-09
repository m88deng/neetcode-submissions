class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product, zeros = 1, 0
        for n in nums:
            if n == 0:
                zeros += 1
            else:
                product = product * n
        if zeros > 1: return [0] * len(nums)
        
        res = []
        for n in nums:
            if n == 0:
                res.append(product)
            elif zeros >= 1:
                res.append(0)
            else:
                res.append(int(product / n))
        
        return res
        