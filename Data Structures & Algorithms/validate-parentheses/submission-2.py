class Solution:
    def isValid(self, s: str) -> bool:
        my_dict = {
            ")":"(",
            "]":"[",
            "}":"{"
        }
        my_stack = []
        for i,c in enumerate(s):
            if (c == "(" or c == "[" or c=="{"):
                my_stack.append(c)
                print("appending " + c)
            if c in my_dict:
                print("dealing with " + c)
                if(len(my_stack) > 0):
                    if my_stack[len(my_stack) - 1] == my_dict[c]:
                        print("pop " + my_stack[len(my_stack) - 1])
                        my_stack.pop()
                    else:
                        return False
                else:
                    return False
        
        return len(my_stack) == 0
        
        