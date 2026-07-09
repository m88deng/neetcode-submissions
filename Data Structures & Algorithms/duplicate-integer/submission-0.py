class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mydict = {}
        for i in nums:
            if i not in mydict:
                mydict[i] = True
            else:
                return True
        return False