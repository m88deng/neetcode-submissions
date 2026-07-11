class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxes = [[set() for _ in range(3)] for _ in range (3)]

        for i in range(9):
            rows = set()
            cols = set()
            for j in range(9):
                r = board[i][j]
                c = board[j][i]
               
                boxi = boxes[i//3][j//3]

                if r in rows or c in cols or r in boxi:
                    return False

                if r != "." :
                    rows.add(r)
                    boxi.add(r)
                
                if c != ".":
                    cols.add(c)


            rows.clear()
            cols.clear()
        
        return True



