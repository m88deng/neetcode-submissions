class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: 
            return
        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        res = 0
        while l < r:
            if maxL < maxR:
                l += 1
                maxL = max(maxL, height[l])
                res += maxL - height[l]
            else:
                r -= 1
                maxR = max(maxR, height[r])
                res += maxR - height[r]
        return res
        # size = len(height)
        # if size == 0 or size == 1: return 0

        # res = [0] * size
        # maxL = height[0]
        # maxR = height[size - 1]
        # l = 0
        # r = size - 1
        # i = l
        # while True:
        #     if(height[l] <= height[r]):
        #         l += 1
        #         i = l
        #     else:
        #         r -= 1
        #         i = r

        #     if (l >= r):
        #         break

        #     water = min(maxL, maxR) - height[i]
        #     if water <= 0: 
        #         res[i] = 0 
        #     else : 
        #         res[i] = water
            
        #     if i == l:
        #         maxL = max(maxL, height[i])
        #     else:
        #         maxR = max(maxR, height[i])

        # return sum(res)
            
