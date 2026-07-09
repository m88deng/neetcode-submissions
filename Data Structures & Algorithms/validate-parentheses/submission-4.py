class Solution:
    def isValid(self, s: str) -> bool:
        my_dict = {
            ")":"(",
            "]":"[",
            "}":"{"
        }
        my_stack = []
        for c in s:
            if c in my_dict:
                if my_stack and my_stack[-1] == my_dict[c]:
                    my_stack.pop()
                else:
                    return False
            else:
                my_stack.append(c)

            # if (c == "(" or c == "[" or c=="{"):
            #     my_stack.append(c)
            #     print("appending " + c)
            # if c in my_dict:
            #     print("dealing with " + c)
            #     if(len(my_stack) > 0):
            #         if my_stack[len(my_stack) - 1] == my_dict[c]:
            #             print("pop " + my_stack[len(my_stack) - 1])
            #             my_stack.pop()
            #         else:
            #             return False
            #     else:
            #         return False
        
        return True if not my_stack else False
        
        