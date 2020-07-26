# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        rev = ListNode(-1)
        while head:
            next_head = head.next
            to_next = rev.next
            rev.next = head
            head.next = to_next
            head = next_head
        return rev.next