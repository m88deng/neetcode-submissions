# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find mid of list
        #reverse second half
        #alternate first and second half

        mid, fast = head, head
        while fast and fast.next:
            mid = mid.next
            fast = fast.next.next
        # found mid
        # reverse linked list between mid and fast

        cur = mid.next
        prev = mid.next = None
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        # merge with head, and prev
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

            

        