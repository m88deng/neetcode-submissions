class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)

        l = 0
        r = n - 1

        max_area = 0
        while l < r :
            left = heights[l]
            right = heights[r]
            area = (r - l) * min(left, right)
            if area > max_area:
                max_area = area
            
            if left <= right:
                l += 1
            elif right < left:
                r -= 1
        return max_area