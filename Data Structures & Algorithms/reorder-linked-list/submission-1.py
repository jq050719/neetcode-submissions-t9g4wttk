# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        # use slow and fast pointer method to get middle of linked list
        # slow will now be middle of linked list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # split list into two halves
        l1 = head       # l1 = start of list
        second = slow.next      # second list starts after midpoint

        # prevent first list from linking to second
        curr = l1
        while curr:
            if curr.next == second:
                curr.next = None
            curr = curr.next

        l2 = self.reverseLinkedList(second)       # reverse linked list starting at poin after midpoint

        while l1 and l2:
            next_node_l1 = l1.next      # save next node in first half of list
            next_node_l2 = l2.next      # save next node in second half of list
            # reorder
            l1.next = l2
            l2.next = next_node_l1

            l1 = next_node_l1
            l2 = next_node_l2


    def reverseLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next_node = curr.next       # save next node to iterate to
            curr.next = prev        # reverse link order
            prev = curr     # next node in reverse order
            curr = next_node
        
        return prev
