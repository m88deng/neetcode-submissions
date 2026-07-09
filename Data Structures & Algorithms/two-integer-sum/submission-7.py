class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        res = 0

        for i in range(len(nums)):
            d[nums[i]] = i

        for i,n in enumerate(nums):
            res = target - n
            if res in d and d[res] != i:
                return [i,d[res]]
