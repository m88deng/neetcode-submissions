class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #temp[i] = daily temperature on the day i
        #res[i] = #days after i, before warmer tmp appears in future
        # e.g. if tmp = [3, 2 , 5]
        # res = [2, 1, 0]

        # keep a stack of the temp we are looking to surpass
        # (38, 2) 36 35 40
        stack = []
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            print(stack)
            while stack and t > stack[-1][0]:
                day = stack.pop()[1]
                print("day" + str(day))
                res[day] = i - day
            stack.append((t, i))
        
        return res
            


