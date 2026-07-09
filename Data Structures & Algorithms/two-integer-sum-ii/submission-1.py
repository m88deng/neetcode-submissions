class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i,m in enumerate(numbers):
            n = target - m
            l = i + 1
            r = len(numbers) - 1
            while l <= r:
                mid = l + (r - l) // 2
                if numbers[mid] == n:
                    return [i + 1, mid + 1]
                elif numbers[mid] < n:
                    l = mid + 1
                elif numbers[mid] > n:
                    r = mid - 1
                else:
                    break

        return [0,0]
    