class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #set of distinct sets of 3 indices
        res = set()
        n = len(nums)
        nums.sort()
        
        for i in range(n): # O(n) time
            num1 = nums[i]
            complete = 0 - num1

            l = i + 1
            r = n - 1

            while l < r:
                sum = nums[l] + nums[r]
                if sum == complete:
                    triplet = (nums[i],nums[l],nums[r])
                    if triplet not in res:
                        res.add(triplet)
                    l += 1
                    r -= 1
                elif sum < complete:
                    l += 1
                else:
                    r -= 1
            
        return list(res)