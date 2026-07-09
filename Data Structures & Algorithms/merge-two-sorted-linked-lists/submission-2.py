# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = list1
        l2 = list2
        if l1 is None and l2 is None: 
            return None

        dummy = ListNode()
        cur = dummy;

        while (l1 and l2):
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next

            cur = cur.next
        
        if l1 is not None:
            cur.next = l1
        if l2 is not None:
            cur.next = l2
        
        return dummy.next
            

        


        
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        # dummy = ListNode()
        # current = dummy
        # next1, next2 = list1, list2
        # while next1 and next2:
        #     if next1.val <= next2.val:
        #         current.next = next1
        #         next1 = next1.next
        #     else:
        #         current.next = next2
        #         next2 = next2.next
        #     current = current.next
        # if next1:
        #     current.next = next1
        # if next2:
        #     current.next = next2
        # return dummy.next
