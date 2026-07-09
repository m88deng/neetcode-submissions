class Solution:
    def findMin(self, nums: List[int]) -> int:
        # if it has been rotated < n time
        # nums[0] < nums[-1]
        # otherwise, nums[0] > nums[-1]
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] < nums[r]:
                return nums[l]
            m = l + (r - l) // 2
            if nums[l] < nums[m] or nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        return nums[l]