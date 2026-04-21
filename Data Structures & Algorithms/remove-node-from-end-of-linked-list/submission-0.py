# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        # nth node from END of list is at index (length - n)
        target = length - n
        # Case 1: node to remove is at beginning
        if target == 0:
            #curr = head
            head = head.next
            #curr.next = None
            return head
        # Case 2: node to remove is at end
        # Stop at node before last node and then remove last node
        elif target == length - 1:
            curr = head
            while curr.next.next:
                curr = curr.next
            curr.next = None
            return head

        # Otherwise, node is in middle
        # Stop at node before target node at index length - (n + 1)
        else:
            target = length - (n + 1)
            curr = head
            i = 0
            while curr:
                if i == target:
                    curr.next = curr.next.next
                    return head
                curr = curr.next
                i += 1

