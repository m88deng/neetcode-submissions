# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        # while len(lists) > 1:
        #     mergedLists = []
        #     for i in range(0, len(lists), 2):
        #         l1 = lists[i]
        #         l2 = lists[i+1] if (i+1) < len(lists) else None
        #         mergedLists.append(self.mergeLists(l1, l2))
        #     lists = mergedLists
        # return lists[0]

        while len(lists) > 1:
            mergedList = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                mergedList.append(self.mergeLists(l1, l2))
            lists = mergedList
        return lists[0]

    def mergeLists(self, l1, l2):

        # todo merge 2 list
        dummy = ListNode()
        cur = dummy
        next1, next2 = l1, l2
        while next1 and next2:
            if next1.val <= next2.val:
                cur.next = next1
                next1 = next1.next
            else:
                cur.next = next2
                next2 = next2.next
            cur = cur.next
        if next1:
            cur.next = next1
        elif next2:
            cur.next = next2
        return dummy.next
