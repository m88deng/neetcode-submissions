class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        from collections import defaultdict
        d = defaultdict(int)

        for i in range(len(nums)):
            d[i] = nums[i]

        res = 0

        for i in range(len(nums)):
            res = target - nums[i]
            for j in range(i+1, len(d)):
                if d[j] == res: 
                    return [i, j]
