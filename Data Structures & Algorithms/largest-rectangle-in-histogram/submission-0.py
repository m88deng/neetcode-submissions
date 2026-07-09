class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #bottleneck is the shortest height
        #stop considering heights if they cannot be expanded right
        stack = []
        max_area = 0
        for i,h in enumerate(heights):
            print (str(i) + " " + str(h))
            print(max_area)
            print(stack)
            index = i
            while stack and h < stack[-1][0]: #cannot extend stack[-1]
                print("inwhile")
                popH, popI = stack.pop()
                index = popI
                max_area = max((i - popI) * popH, max_area)

            stack.append([h, index])
        
        print(stack)
        lastI = len(heights)
        for s in stack:
            area = s[0] * (lastI - s[1])
            max_area = max(max_area, area)
        return max_area
