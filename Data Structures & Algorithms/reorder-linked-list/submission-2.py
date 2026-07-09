# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find mid
        # reverse  
        # alternate
        
        mid, end = head, head
        while end and end.next:
            mid = mid.next
            end = end.next.next
        
        #mid right in front of the node of the second half

        reverse = mid.next
        prev = mid.next = None # separate both Lists

        while reverse:
            tmp = reverse.next
            reverse.next = prev
            prev = reverse
            reverse = tmp

        # prev = head of new list
        l1 = head
        l2 = prev

        while l2:
            tmp1, tmp2 = l1.next, l2.next
            l1.next = l2
            l2.next = tmp1
            l1, l2 = tmp1, tmp2






        # # mid
        # fast, mid = head, head
        # while fast and fast.next:
        #     fast = fast.next.next
        #     mid = mid.next

        # # reverse
        # cur = mid.next
        # prev = mid.next = None #cutting list in 2
        # while cur:
        #     tmp = cur.next
        #     cur.next = prev
        #     prev = cur
        #     cur = tmp
        
        # # prev

        # # alternate merging
        # p1, p2 = head, prev
        # while p2:
        #     tmp1, tmp2 = p1.next, p2.next
        #     p1.next = p2
        #     p2.next = tmp1
        #     p1, p2 = tmp1, tmp2
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # #find mid of list
        # #reverse second half
        # #alternate first and second half

        # mid, fast = head, head
        # while fast and fast.next:
        #     mid = mid.next
        #     fast = fast.next.next
        # # found mid
        # # reverse linked list between mid and fast

        # cur = mid.next
        # prev = mid.next = None
        # while cur:
        #     tmp = cur.next
        #     cur.next = prev
        #     prev = cur
        #     cur = tmp
        
        # # merge with head, and prev
        # first, second = head, prev
        # while second:
        #     tmp1, tmp2 = first.next, second.next
        #     first.next = second
        #     second.next = tmp1
        #     first, second = tmp1, tmp2

            