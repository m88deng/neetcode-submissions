class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            print(str(l) + " " + str(r))
            
            m = l + (r - l) // 2
            print(m)
            print(nums[m])

            if target == nums[m]:
                return m
            
            if nums[l] <= nums[m]: # 3 4 5
                if target > nums[m] or target < nums[l]:
                    l = m + 1 #eg 7, 2
                else:
                    r = m - 1 

            else: # 6 1 2 nums[l] > nums[m]
                if target > nums[r] or target < nums[m]:
                    r = m-1
                else:
                    l = m+1
          #ed array
            
        return -1

