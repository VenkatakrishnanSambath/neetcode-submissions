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
        if not head: return None

        curr = head
        deep_copy = {}

        while curr:
            deep_copy[curr] = Node(x = curr.val)
            curr = curr.next
        
        curr = head

        while curr:
            new_node = deep_copy[curr]
            new_node.next = deep_copy[curr.next] if curr.next else None
            new_node.random = deep_copy[curr.random] if curr.random else None
            curr = curr.next
        
        return deep_copy[head]
        