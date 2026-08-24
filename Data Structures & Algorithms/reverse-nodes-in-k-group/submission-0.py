# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            k_node = self.getKnode(group_prev, k)
            if not k_node:
                break
            group_next = k_node.next

            prev, curr = k_node.next, group_prev.next

            while curr != group_next:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            temp = group_prev.next
            group_prev.next = k_node
            group_prev = temp
        return dummy.next
    def getKnode(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr