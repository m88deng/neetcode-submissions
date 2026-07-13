class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        n = len(numbers)

        for i in range(n):
            num = numbers[i]
            complete = target - num

            l = i + 1
            r = n - 1

            while l <= r:
                mid = (l + r) // 2
                if mid == i:
                    l += 1
                
                if numbers[mid] == complete:
                    return [i+1, mid+1]
                elif complete > numbers[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
                    
            

