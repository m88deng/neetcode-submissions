"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        
        cur = head
        while cur:
            copy = Node(cur.val)
            
            copy.next = cur.next
            copy.random = cur.random
            cur.next = copy
            cur = copy.next
        
        copy_head = head.next
        cur = head

        while cur:
            if cur.next.random is not None:
                cur.next.random = cur.random.next
            cur = cur.next.next
            #cur None, or cur.next None
        
        cur = head
        while cur:
            copy = cur.next
            cur.next = copy.next
            if copy.next:
                copy.next = copy.next.next
            cur = cur.next
        
        return copy_head
        
        # if not head: 
        #     return None
        
        # d = collections.defaultdict(lambda: Node(0))
        # d[None] = None
        
        # cur = head
        # while cur:
        #     d[cur].val = cur.val
        #     d[cur].next = d[cur.next]
        #     d[cur].random = d[cur.random]
        #     cur = cur.next
        
        # return d[head]
            

