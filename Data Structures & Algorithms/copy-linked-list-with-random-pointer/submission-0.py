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
        if not head: 
            return None
        
        d = {}
        cur = head
        
        while cur:
            node = Node(cur.val)
            d[cur] = node
            cur = cur.next
        
        cur = head
        copy = d[cur]
        while cur:
            copy.next = d.get(cur.next)
            copy.random = d.get(cur.random)
            cur = cur.next
            copy = copy.next
        
        return d[head]
            

