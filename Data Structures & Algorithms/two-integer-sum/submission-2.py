class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        for i in range(len(nums)):
            my_dict[nums[i]] = i
        
        for i, num in enumerate(nums):
            compl = target - num
            if compl in my_dict and my_dict[compl] != i:
                return [i, my_dict[compl]]
        