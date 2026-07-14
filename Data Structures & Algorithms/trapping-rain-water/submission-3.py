class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_l = [0] * n
        max_r = [0] * n

        max_l[0] = height[0]
        max_r[n-1] = height[n-1]
        max_water = 0

        for i,h in enumerate(height):
            if i == 0:
                max_l[i] = height[i]
            elif h > max_l[i-1]:
                max_l[i] = h
            else:
                max_l[i] = max_l[i-1]

        for i in range(n-1, -1, -1):
            if i == n-1:
                max_r[i] = height[i]
            elif height[i] > max_r[i+1]:
                max_r[i] = height[i]
            else:
                max_r[i] = max_r[i+1]

        for i,h in enumerate(height):
            max_water += min(max_l[i], max_r[i]) - h
        
        return max_water

