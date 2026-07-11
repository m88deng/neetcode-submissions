class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mins = set(nums)
        res = 0

        for i in mins:
            # given any number
            # max sequence length is len(nums)
            # if a number is < or > num+len cut number out (cannot be min)
            ans = 1

            if i-1 in mins:
                # mins.remove(i) skip
                continue
            
            #is a min
            while i + 1 in mins:
                ans += 1
                i += 1

            if ans > res :
                res = ans

        return res



            