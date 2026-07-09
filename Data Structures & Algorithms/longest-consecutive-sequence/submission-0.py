class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # n itself, sequence length = 1
        # if n-1 exists, sequence length += 1
        # hashmaps <n, # in its sequence ending at n>
        num_set = set(nums)
        longest = 0
        
        for n in num_set:
            if (n - 1) not in num_set:
                length = 1
                while (n + length) in num_set:
                    length += 1
                longest = max(length, longest)
        
        return longest