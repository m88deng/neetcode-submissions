# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = None
        while cur:
            tmp = cur.next
            cur.next = prev 
            prev = cur
            cur = tmp
        return prev

        # [head][p1][p2]

        # [h] cur
        # cur.next [p1]

        # [p1].[h]
















        # current = head
        # prev = None
        # while current: # insert to head
        #     tmp = current.next
        #     current.next = prev
        #     prev = current
        #     current = tmp
        # return prev

