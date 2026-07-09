class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # read 2 elements, add to my stack
        # upon reading a symbol
        # pop twice
        # add result
        # int div truncate to zero
        operators = set(["+","-","*","/"])
        my_stack = []
        for token in tokens:
            if token in operators:
                op2 = int(my_stack.pop())
                op1 = int(my_stack.pop())
                print("op1 " + str(op1) + token + "op2 " + str(op2))
                if token == "+":
                    res = int(op1 + op2)
                    my_stack.append(res)
                    print(res)
                elif token == "-":
                    res = int(op1 - op2)
                    my_stack.append(res)
                    print(res)
                elif token == "*":
                    res = int(op1 * op2)
                    print(res)
                    my_stack.append(res)
                elif token == "/":
                    res = int(op1 / op2)
                    print(res)
                    my_stack.append(res)
                #do smth
            else:
                print("token " + token)
                my_stack.append(token)
        ret = int(my_stack[-1])
        return ret
        