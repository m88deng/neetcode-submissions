class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # n pairs
        # n open and n closed
        # in any order 
        # keep track of how many open
        # keep track of how many closed
        # first bracket always open
        # last bracket always closed
        # 
        # 
        stack = []
        res = []

        def backtrack(opened, closed):
            if opened == closed == n:
                res.append("".join(stack))
            if opened < n:
                stack.append("(")
                backtrack(opened + 1, closed)
                stack.pop()
            if closed< opened:
                stack.append(")")
                backtrack(opened, closed + 1)
                stack.pop()
        backtrack(0, 0)
        return res

                


        