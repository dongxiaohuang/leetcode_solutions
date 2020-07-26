# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not k or not head.next:
            return head
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        k = k % length
        if k == 0:
            return head
        fast = head
        for i in range(k):
            prev_fast = fast
            fast = fast.next
        slow = head
        while fast.next:
            fast = fast.next
            slow = slow.next

        dummy = ListNode(-1)
        dummy.next = slow.next
        fast.next = head
        slow.next = None
        return dummy.next
