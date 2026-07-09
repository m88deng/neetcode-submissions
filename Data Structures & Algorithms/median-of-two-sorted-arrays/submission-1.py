class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    # we want to find a left and right partition
    # for each array
    # the median is either the smallest on the right partition
    # or the avg of the smallest right and largest left

        A, B = nums1, nums2
        # for convenience, we want the shortest array to be A

        if len(B) < len(A) : 
            A, B = B, A
        
        total = len(A) + len(B)
        half = total // 2

        l, r = 0, len(A) - 1
        
        while True:
            i = (l + r) // 2 #mid of A
            j = half - i - 2 #mid of B (-2 bc of idx offsets)

            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i + 1] if i + 1 < len(A) else float("inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j + 1] if j + 1 < len(B) else float("inf")
            
            # found partition if
            # Aleft <= Bright and Bleft <= Aright

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 == 1: #odd
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            elif Bleft > Aright:
                l = i + 1
                # [[1 2] 3 4 5] B
                # [[3 4] 5 ] A

        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
        
        # A, B = nums1, nums2
        # total = len(A) + len(B)
        # half = total // 2
        # if len(B) < len(A):
        #     A, B = B, A
        
        # l, r = 0, len(A) - 1
        # while True:
        #     i = (l + r) // 2 #A
        #     j = half - i - 2 #B

        #     Aleft = A[i] if i >= 0 else float("-infinity")
        #     Aright = A[i + 1] if i + 1 < len(A) else float("infinity")
        #     Bleft = B[j] if j >= 0 else float("-infinity")
        #     Bright = B[j + 1] if j + 1 < len(B) else float("infinity")

        #     if Aleft <= Bright and Bleft <= Aright:
        #         if total % 2 == 1:
        #             return min(Aright, Bright)
        #         else:
        #             return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
        #         #found correct partition
        #     elif Aleft > Bright:
        #         r = i - 1
        #     elif Bleft > Aright:
        #         l = i + 1
                
