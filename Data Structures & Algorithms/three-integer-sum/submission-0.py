class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        my_set = set()
        for i in range(size):
            for j in range(i+ 1, size, +1):
                for k in range(j+1, size, +1):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = tuple(sorted((nums[i], nums[j], nums[k])))
                        my_set.add(triplet)
        
        return list(my_set)
        