class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search on first col
        # binary search on row
        m1, n1 = 0, 0
        m2 = len(matrix) - 1
        n2 = len(matrix[0]) - 1
        m, n = 0, 0
        while m1 <= m2:
            m = m1 + (m2 - m1) // 2
            print("m " + str(m) + ", m1: " + str(m1) + ", m2: " + str(m2))
            if matrix[m][0] == target:
                return True
            elif matrix[m][0] > target:
                    m2 = m - 1
            elif matrix[m][0] < target:
                if m < len(matrix) - 1 and matrix[m+1][0] > target:
                    break
                else: m1 = m + 1
            
        print(m)
        while n1 <= n2:
            n = n1 + (n2 - n1)//2
            if matrix[m][n] == target:
                return True
            if matrix[m][n] < target:
                n1 = n + 1
            if matrix[m][n] > target:
                n2 = n - 1
        print(n)
        return False
        

        