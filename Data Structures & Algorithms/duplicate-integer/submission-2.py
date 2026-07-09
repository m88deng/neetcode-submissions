class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # seen = set()

        # for n in nums:
        #     seen.add(n)
        
        # return len(nums) != len(seen)
        return len(set(nums)) != len(nums)
        